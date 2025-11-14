pipeline {
    agent { docker { image 'python:3.12.12-alpine3.22' } }
    stages {
        stage('Python version') {
            steps {
                sh 'python --version'
            }
        }
        stage('Build') {
            steps {
                sh 'adduser \
                    --disabled-password \
                    --gecos "" \
                    --home "/nonexistent" \
                    --shell "/sbin/nologin" \
                    --no-create-home \
                    --uid "${UID}" \
                    appuser'
                sh '--mount=type=cache,target=/root/.cache/pip \
                    --mount=type=bind,source=requirements.txt,target=requirements.txt \
                    python -m pip install -r requirements.txt'
                sh 'chown -R appuser:appuser /app'
            }
            
        }
    }
}
