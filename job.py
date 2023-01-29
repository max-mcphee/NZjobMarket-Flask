class Skill:
    def __init__(self, skill, found):
        self.skill = skill
        self.found = found


class Job:
    def __init__(self, name, link, location, skills, date):
        self.name = name
        self.link = link
        self.location = location
        self.skills = skills
        self.date = date
