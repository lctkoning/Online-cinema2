pipeline {
    agent any

    stages {
        stage('Clone github') {
            steps {
                git credentialsId: 'd9647787-ea44-4bcd-9b42-7cbe6e8200f6', url: 'git@github.com:lctkoning/online-cinema.git'
            }
        }
        stage('Build using maven') {
            steps {
                sh 'mvn install'
            }
        }
        stage('Test maven') {
            steps {
                sh 'mvn test'
            }
        }
        stage('deploy in runtime') {
            steps {
               echo 'Succesfull'
            }
        }
    }
}
