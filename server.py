from ntpath import join
from flask import Flask, render_template, request, jsonify
from referral_form import ReferralForm
from response import message

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

@app.route('/referral', methods=['GET', 'POST'])
def signup():
	form = ReferralForm()
	if form.is_submitted():
		username = form.username.data
		recruiter_name = form.recruiter_name.data
		company_name = form.company_name.data
		job_role = form.job_role.data
		result = message(username, recruiter_name, company_name, job_role)
		return render_template('referral_message.html', text=result)
		# return jsonify(data)
	return render_template('referral_data.html', form=form)

@app.route('/referral')
def response():
	message()
	# return "Done"

if __name__ == '__main__':
	app.run()