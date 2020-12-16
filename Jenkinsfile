
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
            sh 'mvn clean deploy'
          
            }
                
        }
        stage('Download from snapshot') {
            steps {
                sh 'curl -X GET "192.168.2.21:8081:8081/service/rest/v1/search/assets/download?sort=version&repository=maven-snapshots&maven.groupId=org.foo.bar&maven.artifactId=project&maven.baseVersion=1.2.3-SNAPSHOT&maven.extension=war" -H "accept: application/json"'
            }
        }
            
        
    
}
}
