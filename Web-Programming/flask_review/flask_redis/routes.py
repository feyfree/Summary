from flask import Flask, url_for, request, render_template
from flasky import app
import redis


r = redis.StrictRedis(host='localhost', port=6379, db=0, charset='utf-8', decode_responses=True)

@app.route('/')
def hello():
	createLink = "<a href='" + url_for('create')+"'>Create a question</a>"
	return """<html>
					<head>
						<title>Hello, world
						</title>
					</head>
					<body>
						""" + createLink + """
					</body>
			  </html>"""

@app.route('/create', methods=['POST', 'GET'])
def create():
	if request.method == 'GET':
		#send the user the form
		return render_template('CreateQuestion.html')
	elif request.method == 'POST':
		#read form data and save it
		title = request.form['title']
		question = request.form['question']
		answer = request.form['answer']


		#Store data in data store
		# key name will ne whatever title they typed in
		r.set(title + ':question', question)
		r.set(title + ':answer', answer)
		return render_template('CreatedQuestion.html', question=question)
	else:
		return "<h2>Invalid request</h2>"

@app.route('/question/<title>', methods=['GET', 'POST'])
def question(title):
	if request.method == 'GET':
		question = r.get(title + ':question')
		return render_template('AnswerQuestion.html', question=question)
	
	elif request.method == 'POST':
		submittedAnswer = request.form['submittedAnswer']

		# read answer from data store
		answer = r.get(title+':answer')
		if submittedAnswer == answer:
			return render_template('Correct.html')
		else:
			return render_template('Incorrect.html', anwser=answer, submittedAnswer=submittedAnswer)
	else:
		return "<h2>Invalid request</h2>"