pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                git branch: 'main', url: 'https://github.com/amrikiitj/Jtest_1.git'                
            }
        }       

        stage('Build') {
            steps {
                // Build your application (if needed)
                echo 'Building application...'
                sh 'python3 test1.py'
            }
        }

        
    }
    
}

