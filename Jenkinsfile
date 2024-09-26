pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                git 'https://github.com/amrikiitj/Jtest_1.git'
            }
        }       

        stage('Build') {
            steps {
                // Build your application (if needed)
                echo 'Building application...'
                python3 'test1.py'
            }
        }

        
    }

    post {
        always {
            cleanWs() // Clean workspace after every build
        }
        success {
            echo 'Build and deployment completed successfully.'
        }
        failure {
            echo 'Build or deployment failed.'
        }
    }
}

