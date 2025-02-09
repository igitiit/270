pipeline {
    agent any

    environment {
        VENV_NAME = 'venv'  // Name of your virtual environment
    }

    triggers {
        githubPush()  // Trigger job on GitHub push
    }

    stages {
        stage('Setup Python Environment') {
            steps {
                script {
                    // Check if virtual environment already exists
                    if (isUnix()) {
                        sh '''
                            if [ ! -d "${VENV_NAME}" ]; then
                                python3 -m venv ${VENV_NAME}  # Create virtual environment
                            fi
                            . ${VENV_NAME}/bin/activate  # Activate virtual environment
                            pip install --upgrade pip
                            pip install -r requirements.txt  // Install dependencies
                        '''
                    } else {
                        bat '''
                            if not exist %VENV_NAME% (
                                python -m venv %VENV_NAME%  // Create virtual environment
                            )
                            call %VENV_NAME%\\Scripts\\activate.bat  // Activate virtual environment
                            pip install --upgrade pip
                            pip install -r requirements.txt  // Install dependencies
                        '''
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            echo "Current directory in Jenkins:"
                            pwd
                            echo "Listing files in current directory:"
                            ls -alh
                            echo "Activating virtual environment..."
                            . ${VENV_NAME}/bin/activate  # Activate virtual environment
                            echo "Running pytest..."
                            pytest --maxfail=1 --disable-warnings --tb=short --junitxml=./result.xml || true
                            echo "pytest run completed. Checking for result.xml..."
                            ls -alh  # List files to verify result.xml is created
                        '''
                    } else {
                        bat '''
                            echo "Activating virtual environment..."
                            call %VENV_NAME%\\Scripts\\activate.bat
                            echo "Running pytest..."
                            pytest --maxfail=1 --disable-warnings --tb=short --junitxml=.\result.xml || true
                            echo "Tests finished. Checking for result.xml..."
                            dir  # List files to verify result.xml is created
                            echo "pytest run completed"
                        '''
                    }
                }
            }
        }

        stage('Archive Test Results') {
            steps {
                script {
                    // Archive test results so you can view them in Jenkins
                    junit '**/result.xml'
                }
            }
        }
    }
}
