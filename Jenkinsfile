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
        
        // Add more stages as needed (e.g., tests, build, etc.)
    }
}
