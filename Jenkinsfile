
pipeline {
    agent any
    
    stages {
        stage('Clone github') {
            steps {
                git credentialsId: 'd9647787-ea44-4bcd-9b42-7cbe6e8200f6', url: 'git@github.com:lctkoning/online-cinema.git'
            }
        }
        
        stage('Test clean package') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('deploy in nexus') {
            steps {
            script {
            def pom = readMavenPom file: 'pom.xml'
            def Nexreponame = mavenPom.version.endsWith("SNAPSHOT") ? "Testrepo" : "Testrepo-REL"
          
               nexusArtifactUploader artifacts: [[artifactId: 'cinema', classifier: '',file: "target/cinema-${mavenPom.version}.war", type: 'war']],credentialsId: 'Nexusg', groupId: 'org.springframework.samples.service.service', nexusUrl: '192.168.2.21:8081', nexusVersion: 'nexus3', protocol: 'http', repository: Nexreponame, version: "${mavenPom.version}"
            }
        }
    }
}
}
