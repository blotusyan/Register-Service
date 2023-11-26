# README #
pipenv install -r requirements.txt
I had similar problem and root cause of my failure was that I was specifying --template-file template.yml. As per this issue https://github.com/awslabs/aws-sam-cli/issues/1252 SAM CLI looks for the code uri specified in my template.yml and uploads only the function code.
This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact