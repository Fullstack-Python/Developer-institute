import flask_wtf
import wtforms

class Form(flask_wtf.FlaskForm):
    username     = wtforms.StringField("Name")
    password = wtforms.PasswordField("Password")
    bio      = wtforms.StringField("Bio")
    submit   = wtforms.SubmitField("Submit")