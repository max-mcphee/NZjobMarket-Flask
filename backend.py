import mysql.connector
import asyncio
from bs4 import BeautifulSoup
from typing import List
from job import Job
import requests
from fetch import get_job_titles
db = mysql.connector.connect(
    host="nzjobsinstance.ciectykagwlh.ap-southeast-2.rds.amazonaws.com",
    user="admin",
    passwd="adminpassword",
    database="jobsDB"
)


def get_jobs(title):
    job_list = []
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM jobs WHERE title LIKE " + title +"limit 5")
    row = mycursor.fetchone()
    while row is not None:
        column_list = []
        for columns in row:
            column_list.append(columns)
        job_list.append(Job(column_list.index(1),column_list.index(4),column_list.index(3),0,column_list.index(2)))
        row = mycursor.fetchone()
    return job_list