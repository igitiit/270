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
                            # Create the virtual environment if it doesn't exist
                            if [ ! -d "${VENV_NAME}" ]; then
                                python3 -m venv ${VENV_NAME}  # Create the virtual environment
                            fi
                            . ${VENV_NAME}/bin/activate  # Activate the environment
                            pip install --upgrade pip  # Upgrade pip (optional but recommended)
                            pip install -r requirements.txt  # Install dependencies
                        '''
                    } else {
                        bat '''
                            # Create the virtual environment if it doesn't exist
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
                    // Run pytest with debugging output
                    if (isUnix()) {
                        sh '''
                            echo "Activating virtual environment..."
                            . ${VENV_NAME}/bin/activate  # Activate the virtual environment
                            echo "Running pytest..."
                            pytest --maxfail=1 --disable-warnings --tb=short --junitxml=${WORKSPACE}/result.xml || true
                            echo "Tests finished. Checking for result.xml..."
                            ls -alh ${WORKSPACE}  # List files to verify result.xml is created
                        '''
                    } else {
                        bat '''
                            echo "Activating virtual environment..."
                            call %VENV_NAME%\\Scripts\\activate.bat  # Activate the virtual environment
                            echo "Running pytest..."
                            pytest --maxfail=1 --disable-warnings --tb=short --junitxml=%WORKSPACE%\\result.xml || true
                            echo "Tests finished. Checking for result.xml..."
                            dir %WORKSPACE%
                        '''
                    }
                }
            }
        }

    }
    post {
        always {
            // Archive test results
            junit '**/result.xml'  // Publish the JUnit test result report
        }
    }
}
