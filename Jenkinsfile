
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
                sh 'wget "http://192.168.2.21:8081/repository/Testrepo/service/local/artifact/maven/content?r=snapshots&g=com&a=appp&v=LATEST&p=war" --content-disposition'
            }
        }
            
        
    
}
}
