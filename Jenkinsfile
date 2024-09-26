pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                git 'https://github.com/amrikiitj/Jtest_1.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Create a virtual environment and install dependencies
                // sh 'python3 -m venv venv'
                // sh './venv/bin/pip install -r requirements.txt'
            }
        }

        //stage('Run Tests') {
            //steps {
                // Run your tests
                // sh './venv/bin/pytest'
            //}
        //}

        stage('Build') {
            steps {
                // Build your application (if needed)
                echo 'Building application...'
            }
        }

        stage('Deploy') {
            steps {
                // Deploy the application using SSH
                sshPublisher(publishers: [sshPublisherDesc(
                    configName: 'my-ssh-server',
                    transfers: [sshTransfer(
                        sourceFiles: 'Jtest_1/*',
                        remoteDirectory: '/home/mukesh/amrik/Jtest_1',
                        execCommand: 'python3 test1.py'
                    )],
                    usePromotionTimestamp: false,
                    useWorkspaceInPromotion: false,
                    useWorkspaceInSubdir: false
                )])
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

