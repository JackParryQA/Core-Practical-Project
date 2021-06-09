pipeline {
    agent any
    environment {
        DOCKER_USERNAME = credentials('DOCKER_USERNAME')
        DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
        install = false
    }
    stages {
        stage('Install Requirements'){
            steps{
                script{
                    if (env.install == 'true'){
                        sh 'bash jenkins/install-requirements.sh'
                    }
                }
            }
        }
        stage('Test'){
            steps{
                sh 'bash jenkins/tests.sh'
            }
        }
        stage('Build'){
            steps{
                sh 'docker-compose build'
            }
        }
        stage('Push'){
            steps{
                sh 'docker-compose push'
            }
        }
        stage('Configuration Management(Ansible)'){
            steps{
                sh 'cd ansible && ansible-playbook -i inventory.yaml playbook.yaml'
            }
        }
        // stage('Deploy'){
            
        // }
    }
}
