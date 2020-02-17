from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UrlForm(FlaskForm):
    long_url = StringField('URL',[DataRequired()])
    submit = SubmitField('Shorten iT!')
