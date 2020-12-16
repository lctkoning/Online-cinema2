
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
                sh 'mvn dependency:get -DremoteRepositories=http://192.168.2.21:8081/repository/Testrepo/ -DgroupId=org.foo -DartifactId=project -Dversion=LATEST -Dtransitive=false'
            }
        }
            
        
    
}
}
