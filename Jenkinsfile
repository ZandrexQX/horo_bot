pipeline {
    agent none
    stages {
        stage('Docker image') {
            agent {
                docker { image 'python:3.12.12-alpine3.22' }
            }
            steps {
                sh 'python --version'
            }
        }
        stage('Compose') {
            agent any {
                steps {
                    sh 'docker compose up'
                }
            }
        }
    }
}
