#Cloud-Resume-Challenge

The [Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/) was created by [Forrest Brazeal](https://forrestbrazeal.com/) and was designed to help individuals demonstrate and enhance their practical AWS skills. The challenge involves creating a resume website hosted on AWS that demonstrates various cloud-related skills.

To complete this challenge, I built my website utilizing AWS and its products such as S3, CloudFront, Route 53, Certificate Manager, Lambda, DynamoDB, API Gateway, and the Boto3 Python. The FrontEnd part of the website was built using HTML, CSS, and JavaScript and IaC was implemented using Terraform, while CI/CD pipelines are triggered and executed using GitHub Actions.

Before reading more, take a look at my website here: (https://resume.seanhproperties.net/)

-----

## Challenge Steps & Notes:


- [x]  1. Earn an **AWS Certification**
    - Passed the Cloud Practitioner in November 2023 and the Solutions Architect Associate in November 2023 as well.

- [x]  2. Write Resume in **HTML**
    - Utilized a HTML5 UP template and built my website on top of it.

- [x]  3. Style Resume in **CSS**
    - Implemented specific overrides on the framework's foundation.

- [x]  4. Deploy Resume to Static Website with **AWS S3**
    - ![alt text](https://github.com/Seanhui2000/aws-cloud-resume-challenge/blob/main/Screenshots/s3-bucket.png)
    - Utilized OAC (origin access control) to improve security by restricting access to CloudFront distribution
    - Left public access blocked & static website feature disabled for compatibility with OAC

- [x]  5. Use HTTPS Protocol with **AWS CloudFront**
    - ![alt text](https://github.com/Seanhui2000/aws-cloud-resume-challenge/blob/main/Screenshots/cloudfront.png)
    - Redirects any HTTP requests to HTTPS

- [x]  6. Point Custom DNS Domain Name with **AWS Route 53**
    - ![alt text](https://github.com/Seanhui2000/aws-cloud-resume-challenge/blob/main/Screenshots/dns.png)
    - Custom domain purchased through **Route 53** 
    - Validation CNAME records needed in Route 53 DNS settings
    - Website successfully loads from multiple browsers, with & without `www.` subdomain

- [x]  7. Create a Webpage Visitor Counter with **Javascript**
    - POST request sent to Lambda function using Fetch API
    - Latest number of page views displayed to visitor located at the bottom of the page

- [x]  8. Create a Visitor Counter Database with **AWS DynamoDB**
    - ![alt text](https://github.com/Seanhui2000/aws-cloud-resume-challenge/blob/main/Screenshots/dynamoddb.png)
    - noSQL database holds single record with single attribute which is updated by Lambda function

- [x]  9. Connect Webpage to Database with **AWS API Gateway + Lambda**
    - REST API exposes Lambda URL, allowing for GET and POST requests
    - API call invokes Lambda function, relaying function return value as API response to website

- [x] 10. Write a Lambda Function with **Python + AWS Boto3 SDK**
    - ![alt text](https://github.com/Seanhui2000/aws-cloud-resume-challenge/blob/main/Screenshots/lambda.png)
    - Boto3 SDK manages DynamoDB table, retrieving and updating value of view count record
    - Lambda function checks latest count from table, increments +1, and puts new value back to table
    - IAM role for Lambda function is set to allow admin access to dynamoDB table.

- [x] 11. Perform **Tests** on Python Code
    - I did not perform frequent tests but they were run on pytest framework, with lambda function imported locally to be tested

- [x] 12. Configure Resources with **IaC Using Terraform**
    - Terraform used to automatically provision and configure AWS Lambda, DynamoDB, API Gateway
    - Lambda Python code uploaded as .zip file

- [x] 13. Utilize **Source Control** with GitHub
    - The GitHub repository houses all website-related code.
    - Version control is employed to monitor changes and document the evolution of development over time.

- [x] 14. Implement **Backend CI/CD** for Terraform with GitHub Actions
    - Event trigger defined when specific .py lambda function file is pushed to main branch
    - Workflow runs on GitHub-hosted Linux runner

- [x] 15. Implement **Frontend CI/CD** for Webpage Content with GitHub Actions
    - ![alt text](https://github.com/Seanhui2000/aws-cloud-resume-challenge/blob/main/Screenshots/github%20workflow.png)
    - Event trigger defined when any frontend files are included in a push to main branch
    - S3 bucket is synchronized to GitHub repo to contain latest .HTML, .CSS, and .JS files

- [x] 16. Share Your Challenges and Learnings with a **Blog Post**
    - Published article is on Dev.to
