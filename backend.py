import mysql.connector
from job import Job

def get_jobs(title):
    db = mysql.connector.connect(
        host="",
        user="",
        passwd="",
        database="jobsDB"
    )
    job_list = []
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM jobs WHERE title LIKE '%{}%'".format(title))
    row = mycursor.fetchone()
    while row is not None:
        column_list = []
        for columns in row:
            print(columns)
            column_list.append(columns)
        job_link = column_list.pop()
        job_location = column_list.pop()
        job_date = column_list.pop()
        job_title = column_list.pop()
        column_list.pop()
        job_list.append(Job(job_title, job_link, job_location, "java", job_date))
        row = mycursor.fetchone()
    return job_list
