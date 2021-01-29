# AWS Serverless CICD

This project demonstrates how to use [AWS DevOps services](https://aws.amazon.com/devops/) such as CodePipeline, CodeCommit, CodeBuild, CloudFormation and Lambda to create a CI/CD pipeline to orchestrate the deployment of a serverless API.

## Pre-requisites

* An AWS Account - You can get one on the Amazon Web Services [website](https://portal.aws.amazon.com/billing/signup#/start)
* IAM user with CodeCommit credentials
* Git client configured with CodeCommit credentials

Resources

* [Creating an IAM user in your AWS Account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
* [Setup for HTTPS users using Git credentials](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-gc.html)

## Set up

1. Log in to the [CloudFormation Console](https://console.aws.amazon.com/cloudformation/home) and create a stack named Sample-Pipeline using the file from cloudformation/templates/pipeline.yaml as template
2. Once the stack is deployed, go to Outputs and copy "RepoCloneUrlHttp"
3. Using a Git client, clone the repository using the Url from the previous step
4. On the local repository folder (empty repository), paste all the files from this github repo
5. Push the changes to trigger the pipeline on AWS

Resources

* [AWS CloudFormation Designer](https://docs.amazonaws.cn/en_us/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html)
* [Connect to an AWS CodeCommit repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-connect.html)
* [Create a commit using a Git client](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-commit.html#how-to-create-commit-git)

## Authors

* **Isidro Hernandez** - *Initial work* - [Viniza Technologies S.A. de C.V.](https://viniza.mx)

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details
