from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField


class SearchForm(FlaskForm):
    jobTitle = StringField('jobTitle')
    location = StringField('location')
    submit = SubmitField('submit')
