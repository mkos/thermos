from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from flask.ext.wtf.html5 import URLField
from wtforms.validators import DataRequired, url

class BookmarkForm(Form):
    url = URLField('The URL for your bookmark', validators=[DataRequired(), url()])
    description = StringField('Add an optional description')

    def validate(self):

        # add protocol suffix if not present
        if not self.url.data.startswith('http://') or \
               self.url.data.startswith('https://'):
            self.url.data = 'http://' + self.url.data

        # perform normal valiations
        if not Form.validate(self):
            return False

        # if description field is empty, fill it with url string
        if not self.description.data:
            self.description.data = self.url.data

        return True


class LoginForm(Form):
    username = StringField('Your username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
