To start the docker containers run the start.sh script in the scripts folder.  This will spin up all of the services.

This application will allow launch EC2 instances when triggered by the UI for various purposes.  I'd like to provide
an infranstructure for multiple applications to interface easily with various AWS services.  So far S3 and EC2 are the only
services that are implemented.

When the UI triggers an EC2 instance (so far the EC2 instance spins up and then spins down with each invokation.. should I have
and EC2 instance in a stopped state that can be spun up again??   I will have to implement that further.

The application will be making asynchornous calls using rabbitMQ and celery.