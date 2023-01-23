import mysql.connector

db = mysql.connector.connect(
    host="nzjobsinstance.ciectykagwlh.ap-southeast-2.rds.amazonaws.com",
    user="admin",
    passwd="adminpassword",
    database="jobsDB"
)

mycursor = db.cursor()
mycursor.execute("CREATE TABLE softwareJobs(title VARCHAR(255))")
