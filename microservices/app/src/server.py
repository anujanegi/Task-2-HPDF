from src import app
from flask import make_response, Response, redirect, request, abort, render_template, url_for
import requests
import json
import sys

#
# Task 1
#
@app.route('/')
def index():
    return 'Hello World -Anuja Negi'

#
# Task 2
#
@app.route('/authors')
def authors():
    url1 = "https://jsonplaceholder.typicode.com/users"
    url2 = "https://jsonplaceholder.typicode.com/posts"
    try:
        author = requests.get(url1)
        count = requests.get(url2)
    except requests.ConnectionError:
        return "Connection Error"

    authorNames = json.loads(author.text)
    postCount = json.loads(count.text)

    text=""
    for i in range(len(authorNames)):
        c=0
        for j in range(len(postCount)):
            if postCount[j]['userId']==authorNames[i]['id']:
                c+=1
        text=text+authorNames[i]['name']+" "+str(c)+"<br>"
    return text

#
# Task 3
#
@app.route('/setcookie')
def setcookie():
    response = make_response(redirect('/'))
    response.set_cookie('anuja', value='19')
    return response

#
# Task 4
#
@app.route('/getcookie')
def getcookie():
    age = request.cookies.get('anuja')
    return age

#
# Task 5
#
@app.route('/robots.txt')
def robots_txt():
    abort(404)

#
# Task 6
#
@app.route('/html')
@app.route('/html/<name>')
def html(name=None):
    return render_template('hello.html', name=name)

#
# Task 7
#
@app.route('/input')
def input():
    return render_template('data.html')

@app.route('/input', methods=['POST'])
def input_post():
    data = request.form['data']
    print(data, file=sys.stdout)        # logging to console
    return redirect(url_for('input'))   # redirecting to /input
