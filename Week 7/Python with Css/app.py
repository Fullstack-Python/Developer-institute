from flask import Flask
import flask
import database_manager
database_manager.create_database()

app = flask.Flask(__name__)
app.run(debug=True)
app = Flask(__name__)


@app.route("/")
@app.route("/products")
def products_page():

    data = database_manager.load_database()
    template = open('HTML.html', 'r').read()
    css = open('templates/CSS.css', 'r').read()
    return flask.render_template_string(template_file=template, products=data, additional_css=css)


if __name__ == '__main__':
    app.run()
