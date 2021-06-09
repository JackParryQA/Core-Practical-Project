#!/bin/bash
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@manager-1:~/docker-compose.yaml
ssh -i ~/.ssh/ansible_id_rsa jenkins@manager-1 << EOF
    export DATABASE_URI=${DATABASE_URI}
    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml service-1 service-2 service-3 service-4 
EOF