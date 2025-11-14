pipeline {
    agent { docker { image 'python:3.12.12-alpine3.22' } }
    stages {
        stage('Python version') {
            steps {
                sh 'python --version'
            }
        }
        stage('Git clone') {
            steps {
                sh 'apk update && apk add git'
                script {
                    try {
                        sh 'git clone https://github.com/ZandrexQX/horo_bot.git'
                    } catch(Exception e) {
                        echo 'Repository already exists or cloning failed.'
                    }
                }
            }
        }
        stage('Pip install') {
            steps{
                dir('horo_bot'){
                    sh 'python -m pip install -r requirements.txt'
                }
            }
        }
    }
}
