
pipeline {
    agent any
    
    stages {
        
        stage('release prepare') {
            steps {
                sh 'mvn release:prepare'
            }
        }
        stage('release perform') {
            steps {
            sh 'mvn release:perform'
          
            }
                
        }
        stage('clean up') {
            steps {
                sh 'mvn release:clean'
            }
        }
        
    
}
}
