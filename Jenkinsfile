pipeline {
    agent { docker { image 'python:3.12.12-alpine3.22' } }
    stages {
        stage('Test python') {
            steps {
                sh 'python --version'
            }
        }
        stage('Compose') {
            steps {
                sh 'docker compose up'
            }
        }
    }
}
