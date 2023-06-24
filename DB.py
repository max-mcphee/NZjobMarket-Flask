import pandas as pd
import mysql.connector
import os
import asyncio
from bs4 import BeautifulSoup
from typing import List
from job import Job
import requests
from fetch import get_job_titles
db = mysql.connector.connect(
    host="",
    user="",
    passwd="",
    database="jobsDB"
)

mycursor = db.cursor()

mycursor.execute("SELECT skill FROM skills")

skills = mycursor.fetchall()
skills = [skill[0] for skill in skills]


mycursor = db.cursor()
html_text = requests.get('https://www.seek.co.nz/software-developer-jobs?sortmode=ListedDate').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_='yvsb870')
links = []
for job in jobs:
    website = job.find('h3', class_='yvsb870 _14uh9944u _1cshjhy0 _1cshjhyl _1d0g9qk4 _1cshjhys _1cshjhy21')
    if website is not None:
        link = 'https://www.seek.co.nz' + website.find('a')['href']
        if link not in links:
            links.append(link)
    joblist: List[Job] = asyncio.run(get_job_titles(links, skills))

for job in joblist:
    mycursor.execute("SELECT link FROM jobs WHERE link = %s", (job.link,))
    result = mycursor.fetchone()
    if result is None:
        mycursor.execute("INSERT INTO jobs (title, Posted_date, location, link) VALUES (%s,%s,%s,%s)",
                            (job.name, job.date, job.location, job.link,))
        db.commit()

mycursor.close()
mycursor = db.cursor()
for job in joblist:
    mycursor.execute("SELECT id FROM jobs WHERE link = %s", (job.link,))
    result = mycursor.fetchone()
    result = result[0]
    for skill in job.skills:
        if skill.found:
            mycursor.execute("SELECT * FROM jobs_skills WHERE job_id = %s && skill = %s", (result,skill.skill))
            found = mycursor.fetchone()
            if found is None:
                mycursor.execute("INSERT INTO jobs_skills (job_id, skill) VALUES (%s,%s)",(result,skill.skill))
                db.commit()

mycursor = db.cursor()
mycursor.execute("SELECT title, Posted_date, location FROM jobs")

alldata = mycursor.fetchall()

all_tittles = []
all_dates = []
all_locations =[]

for title, Posted_date, location in alldata:
    all_tittles.append(title)
    all_dates.append(Posted_date)
    all_locations.append(location)

dic = {'title': all_tittles, 'Posted_date': all_dates, 'location': all_locations}
df = pd.DataFrame(dic)
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
df_csv = df.to_csv(dir_path + '/jobs.csv')










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

