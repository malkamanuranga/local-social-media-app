<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venom&color=0:00f2fe,100:4facfe&height=200&section=header&text=Local%20Social%20Media&fontSize=50&fontAlignY=35&desc=Flask%20%7C%20Docker%20%7C%20Jenkins%20%7C%20Kubernetes&descAlignY=55&descSize=20&fontColor=ffffff" width="100%" />

<br>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.herokuapp.com?font=Outfit&weight=600&size=24&pause=1000&color=00F2FE&center=true&vCenter=true&width=600&lines=Welcome+to+my+Social+Media+App!;Dockerized+%2B+Jenkins+CI%2FCD;Deployed+on+Kubernetes;Let's+Improve+This+App+Together;Star+%26+Follow+Me!" alt="Typing SVG" />
</a>

<br><br>

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)](https://www.jenkins.io/)

<br><br>

**A modern, fully automated Local CI/CD Pipeline Project.**

</div>

---

## 🚀 About This Project & How You Can Help!

This is a small **Flask-based social media application** that serves as the foundation for a fully automated, local CI/CD pipeline. It features user authentication, post creation, likes, and comments. 

**We have to build this app more!** It is an evolving project, and I am actively looking for contributors to help me expand the basic features of the application, as well as improve the DevOps pipeline.

### 🤝 Help Me Improve This App!
I would love your help to improve:
*   **App Basics:** Adding profiles, follower systems, image uploads, or chat features.
*   **Docker & Kubernetes:** Optimizing images, adding Helm charts, or improving scaling.
*   **Jenkins:** Adding automated tests, code quality checks (SonarQube), or security scans.

If you have knowledge in any of these areas, **please fork the repo and submit a Pull Request!** 

**🔗 Repository Link:** [https://github.com/malkamanuranga/local-social-media-app](https://github.com/malkamanuranga/local-social-media-app)

---

## ⭐ Show Your Support!
If you find this project interesting or helpful for learning DevOps:
1. Please give this repository a **Star ⭐**! It means a lot.
2. **Follow me** ([@malkamanuranga](https://github.com/malkamanuranga)) on GitHub to follow my journey and see more projects covering Docker, Kubernetes, and Jenkins!

---

## 🏗️ CI/CD Architecture

When code is pushed to this repository, the following automated pipeline runs:
1. **Jenkins** detects the push (via SCM Polling) and starts the pipeline.
2. **Docker** builds a new image and runs a smoke test.
3. **Docker Hub** stores the verified image securely.
4. **Kubernetes** performs a zero-downtime rolling update to deploy the new version.

---

## 🐳 How to Run This App

### Option 1: Run with Docker Hub (Fastest)
You can pull the latest image directly from Docker Hub and run it:

```bash
docker pull malkamanuranga/local-social-media-app:latest
docker run -d -p 5000:5000 malkamanuranga/local-social-media-app:latest
Option 2: Run Locally with Docker Compose
Clone the repo and spin it up locally:

bash
git clone https://github.com/malkamanuranga/local-social-media-app.git
cd local-social-media-app
docker compose up -d --build
Access the application in your browser at http://localhost:5000 or via Kubernetes at http://localhost:30081.

<div align="center"> <i>Built with ❤️ for learning DevOps, CI/CD, Docker, and Kubernetes.</i> </div><img src="https://capsule-render.vercel.app/api?type=venom&color=0:00f2fe,100:4facfe&height=100&section=footer&text=Happy%20Coding!&fontSize=24&fontAlignY=50&fontColor=ffffff" width="100%" /> ```
