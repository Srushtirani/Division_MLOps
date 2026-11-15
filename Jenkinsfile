
pipeline {
    agent any

    stages {

        stage('GitHub Checkout') {
            steps {
                checkout scm
                echo 'Code downloaded from GitHub'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat 'python evidently_monitor.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html',
                             allowEmptyArchive: true
        }

        success {
            echo 'Division MLOps Pipeline Successful!'
        }

        failure {
            echo 'Division MLOps Pipeline Failed!'
        }
    }
}
