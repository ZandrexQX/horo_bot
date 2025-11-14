pipeline {
    agent { docker { image 'python:3.12.3-alpine3.22' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}
