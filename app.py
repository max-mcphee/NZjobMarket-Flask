import asyncio
from flask import Flask, render_template, request, jsonify
from forms import SearchForm
from bs4 import BeautifulSoup
from typing import List
from job import Job, Skill
import requests
from fetch import get_job_titles


skills_list = []
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'


@app.route('/', methods=['GET', 'POST'])
def search():
    global skills_list
    form = SearchForm()
    if form.is_submitted():
        try:
            data = request.get_json()
            if data is not None:
                skills = data["skills"]
                skills_list = skills.split(",")
        except:
            print("An exception occurred")
        if request.form.get('jobTitle') is not None:
            html_text = requests.get(
                    'https://www.seek.co.nz/' + request.form.get('jobTitle') + '-jobs/in-' + request.form.get('location') + '?sortmode=ListedDate').text
            if html_text is not None:
                soup = BeautifulSoup(html_text, 'lxml')
                jobs = soup.find_all('div', class_='yvsb870')
                links = []
                for job in jobs:
                    website = job.find('h3', class_='yvsb870 _14uh9944u _1cshjhy0 _1cshjhyl _1d0g9qk4 _1cshjhys _1cshjhy21')
                    if website is not None:
                        link = 'https://www.seek.co.nz' + website.find('a')['href']
                        if link not in links:
                            links.append(link)
                joblist: List[Job] = asyncio.run(get_job_titles(links,skills_list))
            return render_template('result.html', joblist=joblist, answers=links)
    return render_template('search.html', form=form)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
