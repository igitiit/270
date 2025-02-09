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
                                python3 -m venv ${VENV_NAME}  # Create the virtual environment
                            fi
                            . ${VENV_NAME}/bin/activate  # Activate the environment
                            pip install --upgrade pip  # Upgrade pip (optional but recommended)
                            pip install -r requirements.txt  # Install dependencies
                        '''
                    } else {
                        bat '''
                            if not exist %VENV_NAME% (
                                python -m venv %VENV_NAME%  # Create the virtual environment
                            )
                            call %VENV_NAME%\\Scripts\\activate.bat  # Activate the environment
                            pip install --upgrade pip  # Upgrade pip
                            pip install -r requirements.txt  # Install dependencies
                        '''
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Debugging to check current directory and files
                    sh '''
                        echo "Current working directory in Jenkins:"
                        pwd
                        echo "Listing files in current directory:"
                        ls -alh
                    '''
                    
                    // Run pytest with debugging output
                    if (isUnix()) {
                        sh '''
                            echo "Activating virtual environment..."
                            . ${VENV_NAME}/bin/activate  # Activate the virtual environment
                            echo "Running pytest..."
                            pytest --maxfail=1 --disable-warnings --tb=short --junitxml=result.xml || true
                            echo "Tests finished. Checking for result.xml..."
                            ls -alh  # List files to verify result.xml is created
                        '''
                    }
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                // Publish JUnit Test Results
                junit '**/result.xml' // This matches any result.xml file in subdirectories
            }
        }
    }
}
