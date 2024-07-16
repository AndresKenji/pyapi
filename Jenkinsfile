pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('dockerhub_credentials')
        DOCKER_IMAGE = 'oscararodriguez/pyapi:latest'
        SONARQUBE_SERVER = 'localhost:9000'
        SONARQUBE_CREDENTIALS = 'apipy'
        PYTHONPATH = "C:/Users/andre/AppData/Local/Programs/Python/Python310/python.exe"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/AndresKenji/pyapi.git', branch: 'develop'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('SonarQube Analysis') {
            environment {
                SCANNER_HOME = tool 'SonarQube Scanner'
            }
            steps {
                withSonarQubeEnv('SonarQube') {
                    bat "${SCANNER_HOME}/bin/sonar-scanner -Dsonar.projectKey=tu_proyecto -Dsonar.sources=."
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