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
        stage('deploy in nexus) {
            steps {
               nexusArtifactUploader artifacts: [[artifactId: 'cinema', classifier: '',file: 'target/cinema-0.0.1-SNAPSHOT.war', type: 'war']],credentialsId: 'Nexusg', groupId: 'org.springframework.samples.service.service', nexusUrl: 'localhost:8081', nexusVersion: 'nexus3', protocol: 'http', repository: 'http://localhost:8081/repository/maven-snapshots/', version: '0.0.1-SNAPSHOT'
            }
        }
    }
}
