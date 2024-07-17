pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('dockerhub_credentials')
        DOCKER_IMAGE = 'oscararodriguez/pyapi:latest'
        SONARQUBE_SERVER = 'localhost:9000'
        SONARQUBE_TOKEN = credentials('apipytoken')
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/develop']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/AndresKenji/pyapi.git']])
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    try {
                        sh 'pytest'
                    } catch (e) {
                        echo "Tests failed: ${e}"
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }

        stage('SonarQube Analysis') {
            environment {
                SCANNER_HOME = tool name: 'SonarQube', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
            }
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh "${SCANNER_HOME}/bin/sonar-scanner -Dsonar.projectKey=apipy \
                    -Dsonar.projectName=apipy \
                    -Dsonar.projectVersion=1.0 \
                    -Dsonar.language=py"
                }
                
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${env.DOCKER_IMAGE}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub_credentials') {
                        docker.image("${env.DOCKER_IMAGE}").push()
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
