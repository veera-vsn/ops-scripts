pipeline {
    agent none
    triggers {
        cron('H/15 * * * *')
    }
    options {
        timeout(time: 5, unit: "MINUTES")
    }
    stages {
        stage ("disk_space") {
            parallel {
                stage ("agent-1") {
                    agent {
                        label "maven"
                    }
                    steps {
                        sh "python disk_space.py"
                    }
                }
                stage ("agent-2") {
                    agent {
                        label "docker"
                    }
                    steps {
                        sh "python disk_space.py"
                    }
                }
            }
        }
        post {
            failure {
                echo 'ALERT: disk check failed on at least one agent'
        }
    }
}
