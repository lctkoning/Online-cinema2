
pipeline {
    agent any
    
    stages {
        
        stage('Test clean package') {
            steps {
                sh 'mvn clean install'
            }
        }
        stage('deploy in nexus') {
            steps {
            script {
            def pom = readMavenPom file: 'pom.xml'
            def Nexreponame = pom.version.endsWith("SNAPSHOT") ? "Testrepo" : "Testrepo-REL"
            echo pom.version
          
               nexusArtifactUploader artifacts: [[artifactId: 'cinema', classifier: '',file: "target/cinema-${pom.version}.war", type: 'war']],credentialsId: 'Nexusg', groupId: 'org.springframework.samples.service.service', nexusUrl: '192.168.2.21:8081', nexusVersion: 'nexus3', protocol: 'http', repository: Nexreponame, version: "${pom.version}"
            }
        }
    }
}
}
