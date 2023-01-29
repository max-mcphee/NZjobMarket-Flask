import mysql.connector

db = mysql.connector.connect(
    host="nzjobsinstance.ciectykagwlh.ap-southeast-2.rds.amazonaws.com",
    user="admin",
    passwd="adminpassword",
    database="jobsDB"
)

mycursor = db.cursor()



















"""
mycursor.execute("CREATE TABLE jobs(`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,title VARCHAR(255), Posted_date date,location VARCHAR(255) ,link VARCHAR(255))")
first_list = ["Python", "JavaScript", "SQL", "Java", "C++", "C#", "PHP", "Ruby", "Swift", "Go", "Kotlin", "TypeScript", "Scala", "R", "Shell Scripting", "Perl", "Lua", "Groovy", "Rust", "Elixir", "Crystal", "Dart", "Julia", "Erlang", "F#", "Objective-C", "COBOL", "FORTRAN", "Pascal", "Prolog", "Smalltalk", "Lua", "Common Lisp", "Scheme", "Haskell", "OCaml", "Racket", "Clojure"]
second_list = ["AWS", "Azure", "Google Cloud Platform", "Git", "GitHub", "GitLab", "Bitbucket", "Jenkins", "Travis CI", "CircleCI", "AWS CodePipeline", "AWS CodeDeploy", "AWS Elastic Beanstalk", "Docker", "Kubernetes", "Ansible", "Terraform", "Packer", "Vagrant", "Prometheus", "Grafana", "Nagios", "Logstash", "Kibana", "Elasticsearch", "Datadog", "New Relic", "Sentry", "AppDynamics", "Dynatrace", "CloudFormation", "CloudFront", "CloudTrail", "CloudWatch", "Elastic Transcoder", "Elastic Load Balancing", "Direct Connect", "Lambda", "RDS", "SNS", "SQS", "S3", "EC2", "VPC", "IAM", "ECS", "ECR", "EKS", "Cloud9", "CodeStar"]

combined_list = list(set(first_list + second_list))
for skill in combined_list:
    mycursor.execute("SELECT skill FROM skills WHERE skill = %s", (skill,))
    result = mycursor.fetchone()
    if result is None:
        mycursor.execute("INSERT INTO skills (skill) VALUES (%s)", (skill,))
db.commit()
"""

