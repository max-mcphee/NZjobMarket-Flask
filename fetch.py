import asyncio
import aiohttp
import re
from bs4 import BeautifulSoup
import datetime
from job import Job, Skill


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_job_titles(links,skills):
    job_titles = []
    job_location = []
    job_date = []
    joblist = []
    list = []
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in links]
        html_texts = await asyncio.gather(*tasks)
        for html_text in html_texts:
            soup = BeautifulSoup(html_text, 'lxml')
            description = soup.find('div', class_='yvsb870 _14uh9946q _14uh9947q _14uh99496 _14uh9949v _14uh99486 _14uh9948v _1cshjhy18 _1cshjhy1b _14uh99432 _14uh99435')
            skill_list = []
            for skill in skills:
                if skill.lower() == "c++":
                    skill = "c\+\+"
                if re.search(skill.lower(), description.text.lower()):
                    skill_list.append(Skill(skill, True))
                else:
                    skill_list.append(Skill(skill, False))
            list.append(skill_list)
            job_titles.append(description.find('h1', class_='yvsb870 _14uh9944u _1cshjhy0 _1cshjhyl _1d0g9qk4 _1cshjhyp '
                                                     '_1cshjhy21').text)
            date = description.find('span', class_="yvsb870 _14uh9944u _1cshjhy0 _1cshjhy1 _1cshjhy22 _1d0g9qk4 _1cshjhya").text
            if re.search("h", date.lower()):
                job_date.append(datetime.datetime.now().date())
            elif re.search("d", date.lower()):
                match = re.search(r'\d+', date)
                if match:
                    number = int(match.group())
                job_date.append((datetime.datetime.now() - datetime.timedelta(days=number)).date())
            else:
                job_date.append(0)
            job_location.append(description.find('span', class_='yvsb870 _14uh9944u _1cshjhy0 _1cshjhy1 _1cshjhy21 '
                                                                '_1d0g9qk4 _1cshjhya').text)

        for x in range(len(job_titles)):
            joblist.append(Job(job_titles.pop(), links.pop(),job_location.pop(),list.pop(),job_date.pop()))
    return joblist
