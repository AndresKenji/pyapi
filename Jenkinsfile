pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('dockerhub_credentials')
        DOCKER_IMAGE = 'oscararodriguez/pyapi:latest'
        SONARQUBE_SERVER = 'localhost:9000'
        SONARQUBE_CREDENTIALS = credentials('sonarqube_token')
    }

    stages {
        stage('Clone Repository') {
            steps {
                git clone 'https://github.com/AndresKenji/pyapi.git'
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
                    sh "${SCANNER_HOME}/bin/sonar-scanner -Dsonar.projectKey=tu_proyecto -Dsonar.sources=."
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
