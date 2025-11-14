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
                    appuser \
                    --mount=type=cache,target=/root/.cache/pip \
                    --mount=type=bind,source=requirements.txt,target=requirements.txt \
                    python -m pip install -r requirements.txt \
                    chown -R appuser:appuser /app'
            }
            
        }
    }
}
