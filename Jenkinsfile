pipeline {
    agent any

    environment {
        // Your Docker Hub username and repository name
        DOCKER_HUB_USER = 'malkamanuranga'
        IMAGE_NAME      = "${DOCKER_HUB_USER}/local-social-media-app"
        IMAGE_TAG       = "${BUILD_NUMBER}"
        CONTAINER_NAME  = "social-app"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📦 Code checked out from Git'
                sh 'ls -la'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Test Image') {
            steps {
                echo '🧪 Quick smoke test...'
                sh """
                    docker rm -f test-${CONTAINER_NAME} || true
                    docker run -d --name test-${CONTAINER_NAME} -p 5055:5000 ${IMAGE_NAME}:${IMAGE_TAG}
                    sleep 5
                    curl -f http://host.docker.internal:5055/login || (docker logs test-${CONTAINER_NAME} && exit 1)
                    docker stop test-${CONTAINER_NAME}
                    docker rm test-${CONTAINER_NAME}
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo '📤 Pushing image to Docker Hub...'
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                    sh "docker push ${IMAGE_NAME}:latest"
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo '☸️ Deploying to Kubernetes...'
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                    sh """
                        # Update the deployment.yaml with the full image name and new tag
                        sed -i 's|image:.*|image: ${IMAGE_NAME}:${IMAGE_TAG}|g' k8s/deployment.yaml
                        
                        # Apply the manifests
                        kubectl apply -f k8s/deployment.yaml -f k8s/service.yaml
                        
                        # Wait for the rollout
                        kubectl rollout status deployment/social-media-app
                    """
                }
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline succeeded. New image ${IMAGE_NAME}:${IMAGE_TAG} deployed."
        }
        failure {
            echo "❌ Pipeline failed. Check logs above."
        }
    }
}