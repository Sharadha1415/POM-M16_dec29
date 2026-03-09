pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Regression Suite') {
            steps {
                sh 'pytest'
            }
        }
    }
}