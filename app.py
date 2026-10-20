import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User, Post, Comment, Like

app = Flask(__name__)
# Use environment variable for secret key, fallback to dev key
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-123')
# Database configuration (SQLite for local demo)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///social.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db.init_app(app)

# Initialize Login Manager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ---------- Authentication Routes ----------

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('feed'))
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'danger')
            return redirect(url_for('signup'))
            
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('feed'))
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('feed'))
        flash('Invalid username or password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

# ---------- Main App Routes ----------

@app.route('/')
@login_required
def feed():
    # Get all posts, newest first
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('feed.html', posts=posts)

@app.route('/post', methods=['POST'])
@login_required
def create_post():
    content = request.form.get('content', '').strip()
    image_url = request.form.get('image_url', '').strip()
    
    if content or image_url:
        new_post = Post(content=content, image_url=image_url if image_url else None, author=current_user)
        db.session.add(new_post)
        db.session.commit()
        flash('Post created!', 'success')
    else:
        flash('Post cannot be empty.', 'danger')
        
    return redirect(url_for('feed'))

@app.route('/like/<int:post_id>', methods=['POST'])
@login_required
def like_post(post_id):
    post = Post.query.get_or_404(post_id)
    like = Like.query.filter_by(user_id=current_user.id, post_id=post.id).first()
    
    if like:
        # If already liked, unlike it
        db.session.delete(like)
        db.session.commit()
    else:
        # Otherwise, like it
        new_like = Like(user_id=current_user.id, post_id=post.id)
        db.session.add(new_like)
        db.session.commit()
        
    return redirect(url_for('feed'))

@app.route('/comment/<int:post_id>', methods=['POST'])
@login_required
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    content = request.form.get('comment', '').strip()
    
    if content:
        new_comment = Comment(content=content, author=current_user, post=post)
        db.session.add(new_comment)
        db.session.commit()
        flash('Comment added!', 'success')
        
    return redirect(url_for('feed'))

@app.route('/delete/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author == current_user:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted.', 'success')
    else:
        flash('You cannot delete someone else\'s post.', 'danger')
    return redirect(url_for('feed'))

# ---------- Initialize DB & Run ----------
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)