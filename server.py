from ntpath import join
from flask import Flask, render_template, request, jsonify
from forms import SignUpForm
from response import message

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignUpForm()
	if form.is_submitted():
		username = form.username.data
		recruiter_name = form.recruiter_name.data
		company_name = form.company_name.data
		job_role = form.job_role.data
		result = message(username, recruiter_name, company_name, job_role)
		print("Hello1")
		return render_template('user.html', text=result)
		# return jsonify(data)
	return render_template('signup.html', form=form)

@app.route('/signup')
def response():
	message()
	return "Done"

if __name__ == '__main__':
	app.run()