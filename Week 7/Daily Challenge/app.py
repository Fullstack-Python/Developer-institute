from flask import Flask, render_template
from flaskext.markdown import Markdown
import markdown.extensions.fenced_code

app = Flask(__name__)
Markdown(app)


@app.route('/exercises')
def exercices():
    readme_file = open("formation.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )

    return md_template_string

@app.route('/cours')
def cours():
    readme_file = open("introduction.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )

    return md_template_string


if __name__ == '__main__':
    app.run()
