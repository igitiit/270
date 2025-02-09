pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.11'
        VENV_NAME = 'venv'
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
        timeout(time: 1, unit: 'HOURS')
        timestamps()
    }

    stages {
        stage('Setup Python') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            python${PYTHON_VERSION} -m venv ${VENV_NAME}
                            . ${VENV_NAME}/bin/activate
                            python -m pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            python -m venv %VENV_NAME%
                            call %VENV_NAME%\\Scripts\\activate.bat
                            python -m pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Code Quality') {
            parallel {
                stage('Lint') {
                    steps {
                        script {
                            if (isUnix()) {
                                sh '''
                                    . ${VENV_NAME}/bin/activate
                                    pylint src/ tests/ || true
                                    black --check src/ tests/
                                '''
                            } else {
                                bat '''
                                    call %VENV_NAME%\\Scripts\\activate.bat
                                    pylint src\\ tests\\ || true
                                    black --check src\\ tests\\
                                '''
                            }
                        }
                    }
                }

                stage('Type Check') {
                    steps {
                        script {
                            if (isUnix()) {
                                sh '''
                                    . ${VENV_NAME}/bin/activate
                                    mypy src/
                                '''
                            } else {
                                bat '''
                                    call %VENV_NAME%\\Scripts\\activate.bat
                                    mypy src\\
                                '''
                            }
                        }
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . ${VENV_NAME}/bin/activate
                            pytest tests/ --junitxml=test-results/junit.xml
                        '''
                    } else {
                        bat '''
                            call %VENV_NAME%\\Scripts\\activate.bat
                            pytest tests\\ --junitxml=test-results/junit.xml
                        '''
                    }
                }
            }
            post {
                always {
                    junit 'test-results/junit.xml'
                    cobertura coberturaReportFile: 'coverage.xml'
                    publishHTML(target: [
                        allowMissing: false,
                        alwaysLinkToLastBuild: false,
                        keepAll: true,
                        reportDir: 'htmlcov',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report'
                    ])
                }
            }
        }

        stage('Build Package') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . ${VENV_NAME}/bin/activate
                            python setup.py sdist bdist_wheel
                        '''
                    } else {
                        bat '''
                            call %VENV_NAME%\\Scripts\\activate.bat
                            python setup.py sdist bdist_wheel
                        '''
                    }
                }
            }
            post {
                success {
                    archiveArtifacts artifacts: 'dist/*', fingerprint: true
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        failure {
            emailext (
                subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                body: "Something is wrong with ${env.BUILD_URL}",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']]
            )
        }
    }
}
