import flask
from flask import Flask, render_template

from forms import Form

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/myform', methods=("GET","POST"))
def myform():
    form = Form()
    if form.validate_on_submit(): # Check if the form has been filled

        username = form.username.data # Get
        password = form.password.data #   The
        bio      = form.bio.data      #     Data

        print("Here is what I got from the form:")
        print("username:", username)
        print("password:", password)
        print("bio:", bio)

        return flask.redirect('/')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()
