from typing import Text
from flask_wtf import FlaskForm
from wtforms import StringField, validators, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskportfolio.models import Message


class MessageForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    company = StringField("Company Name", validators=[DataRequired()])
    message = TextAreaField("Leave some feedback...", validators=[DataRequired()])
    submit = SubmitField("Send Message")