# README #
This is the back-end infrastructure of Register Service of OpenIELTS.

### Tech Stack ###
IaC is maintained with cloudformation.
Marshmallow python class is used for schema validation and serialization.
Pytest framework leveraged for unit testing.
It is a SaaS architecture.
Deply with AWS Sam.

### Contribution guidelines ###

* This repo is for grad school admission purpose.

### Who do I talk to? ###

* Repo owner: Weiheng(weihengyans@gmail.com)

### TODO ###

* add docstring
* add return type

### NOTES ###

* pipenv install -r requirements.txt
* I had similar problem and root cause of my failure was that I was specifying --template-file template.yml. As per this issue https://github.com/awslabs/aws-sam-cli/issues/1252 SAM CLI looks for the code uri specified in my template.yml and uploads only the function code.
* demo plan: roadmap design(UI->Postman->Gateway->Lambda->DB / File->S3->Gateway->lambda->DB) + UI + Postman + Gateway + DynamoDB + [Schema + Test]