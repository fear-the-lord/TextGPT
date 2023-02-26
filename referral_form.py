from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ReferralForm(FlaskForm):
	username = StringField('Username')
	recruiter_name = StringField('Recruiter Name')
	company_name = StringField('Company Name')
	job_role = StringField('Job Role')
	submit = SubmitField('Sign Up')