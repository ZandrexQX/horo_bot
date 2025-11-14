pipeline {
    agent { docker { image 'python:3.12.12-alpine3.22' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}
