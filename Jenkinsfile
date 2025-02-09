pipeline {
    agent any

    environment {
        VENV_NAME = 'venv'  // Adjust if your virtual environment is named differently
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    // Setup Virtualenv if not already set
                    sh 'python3 -m venv ${VENV_NAME}'  // Only do this once, or if necessary
                    sh './${VENV_NAME}/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run pytest with debugging output
                    echo "Running pytest..."
                    if (isUnix()) {
                        // Activate virtual environment and run pytest
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

        stage('Publish JUnit Results') {
            steps {
                echo "Looking for result.xml in workspace"
                // Make sure the correct path is used here for the result.xml
                junit '**/result.xml'  // Adjust path if result.xml is in a subfolder like 'tests/'
            }
        }
    }
}
