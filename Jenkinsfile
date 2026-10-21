pipeline {
    agent any

    environment {

        DOCKER_HUB_USER = 'malkamanuranga'
        IMAGE_NAME     = "local-social-media-app"
        CONTAINER_NAME = "social-app"
        APP_PORT       = "5000"
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
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Test Image') {
            steps {
                echo '🧪 Quick smoke test...'
                sh """
                    # CLEANUP: Force remove any old test container using this name
                    docker rm -f test-${CONTAINER_NAME}-${BUILD_NUMBER} || true
                    
                    # Run the test container
                    docker run -d --name test-${CONTAINER_NAME}-${BUILD_NUMBER} -p 5055:5000 ${IMAGE_NAME}:${BUILD_NUMBER}
                    sleep 5
                    curl -f http://host.docker.internal:5055/login || (docker logs test-${CONTAINER_NAME}-${BUILD_NUMBER} && exit 1)
                    
                    # CLEANUP: Stop and remove after successful test
                    docker stop test-${CONTAINER_NAME}-${BUILD_NUMBER}
                    docker rm test-${CONTAINER_NAME}-${BUILD_NUMBER}
                """
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo '☸️ Deploying to Kubernetes...'
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                    sh """
                        # Update the deployment.yaml with the new build number
                        sed -i 's|local-social-media-app:latest|local-social-media-app:${BUILD_NUMBER}|g' k8s/deployment.yaml
                        
                        # Apply the Kubernetes manifests
                        kubectl apply -f k8s/deployment.yaml -f k8s/service.yaml
                        
                        # Wait for the rollout to finish successfully
                        kubectl rollout status deployment/social-media-app
                    """
                }
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline succeeded. App live at http://localhost:30081"
        }
        failure {
            echo "❌ Pipeline failed. Check logs above."
        }
    }
}