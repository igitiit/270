stage('Run Tests') {
    steps {
        script {
            // Run pytest with debugging output
            if (isUnix()) {
                sh '''
                    echo "Activating virtual environment..."
                    . ${VENV_NAME}/bin/activate  # Activate the virtual environment

                    echo "Verifying pytest installation..."
                    pip show pytest  # Check if pytest is installed

                    echo "Listing files in the workspace..."
                    ls -alh  # List files to check test files are present

                    echo "Running pytest..."
                    pytest --maxfail=1 --disable-warnings --tb=short --cov=src --cov-report=html --cov-report=xml || true

                    echo "pytest run completed. Checking for result.xml..."
                    ls -alh  # List files to verify result.xml is created
                    cat result.xml  # Output the contents of result.xml for debugging
                '''
            } else {
                bat '''
                    echo "Activating virtual environment..."
                    call %VENV_NAME%\\Scripts\\activate.bat  # Activate the environment

                    echo "Verifying pytest installation..."
                    pip show pytest  # Check if pytest is installed

                    echo "Listing files in the workspace..."
                    dir  # List files to check test files are present

                    echo "Running pytest..."
                    pytest --maxfail=1 --disable-warnings --tb=short --cov=src --cov-report=html --cov-report=xml || exit /b

                    echo "pytest run completed. Checking for result.xml..."
                    dir  # List files to verify result.xml is created
                    type result.xml  # Output the contents of result.xml for debugging
                '''
            }
        }
    }
}
