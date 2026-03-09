pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Regression Suite') {
            steps {
                sh 'pytest'
            }
        }
    }
}