pipeline {
    agent any

    environment {
        IMAGE_NAME = "microlending-app"
        DOCKER_TAG = "latest"
        DEPLOY_ENV = "dev"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/aizawilson8888/microlending-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${DOCKER_TAG} ."
            }
        }

        stage('Run Tests') {
            steps {
                sh "docker run --rm ${IMAGE_NAME}:${DOCKER_TAG} pytest"
            }
        }

        stage('Deploy with Ansible') {
            steps {
                sh """
                echo "$WORKSPACE"
                ls -l "$WORKSPACE"
                docker run --rm \
                  -v \$WORKSPACE:/work \
                  -v \$HOME/.ssh:/root/.ssh \
                  -w /work \
                  my-ansible-runner:latest \
                  ansible-playbook playbook.yml \
                  -i inventory.ini \
                  -e env=dev
                """
             }
        }
    }

    post {
        always {
            echo 'Cleaning up Docker containers'
            sh "docker system prune -f"
        }
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs!"
        }
    }
}
