from flask import Flask, render_template, request
from backend import get_jobs
from forms import SearchForm
from typing import List
from job import Job



skills_list = []
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'


@app.route('/', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.is_submitted():
        try:
            data = request.get_json()
            if data is not None:
                skills = data["skills"]
                skills_list = skills.split(",")
        except:
            print("An exception occurred")
        joblist: List[Job] = get_jobs(request.form.get('jobTitle'))
        return render_template('result.html', joblist=joblist)
    return render_template('search.html', form=form)


if __name__ == '__main__':
    app.run(port=5000)
