pipeline {
    agent any

    environment {
        APP_DIR = '/var/www/django-todoapp'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ndongchrist/django-todoapp.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                echo 'Building Docker images...'
                sh 'docker compose build'
            }
        }

        stage('Run Containers') {
            steps {
                echo 'Starting application...'
                sh '''
                chmod +x deploy.sh
                ./deploy.sh
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                script {
                    def response = sh(script: "curl -s -o /dev/null -w '%{http_code}' http://localhost:8000", returnStdout: true).trim()
                    if (response != '200') {
                        error "❌ Deployment failed! HTTP ${response}"
                    } else {
                        echo "✅ App is up and running on port 8000"
                    }
                }
            }
        }
    }
}
