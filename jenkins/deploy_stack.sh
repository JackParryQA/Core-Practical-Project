#!/bin/bash
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@manager-1:~/docker-compose.yaml
ssh -i ~/.ssh/ansible_id_rsa jenkins@manager-1 << EOF
    export DATABASE_URI=${DATABASE_URI}
    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml
EOF