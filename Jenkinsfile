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
                    if (isUnix()) {
                        sh '''
                            if [ ! -d "${VENV_NAME}" ]; then
                                python3 -m venv ${VENV_NAME}
                            fi
                            . ${VENV_NAME}/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            if not exist %VENV_NAME% (
                                python -m venv %VENV_NAME%
                            )
                            call %VENV_NAME%\\Scripts\\activate.bat
                            pip install --upgrade pip
                            pip install -r requirements.txt
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
                            echo "Running tests..."
                            . ${VENV_NAME}/bin/activate
                            pytest --maxfail=1 --disable-warnings --tb=short --junitxml=result.xml
                            echo "Tests finished. Checking files in current directory..."
                            ls -alh  # Make sure result.xml is generated
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            // Publish JUnit test results
            junit '**/result.xml'  // This should now correctly point to result.xml in the workspace
        }
    }
}
