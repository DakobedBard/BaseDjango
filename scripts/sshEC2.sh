#! /bin/bash
#ssh ec2
ssh -i ${HOME}/.ssh/ec2-key-pair.pem i-0cda155df506a18d1 $1
