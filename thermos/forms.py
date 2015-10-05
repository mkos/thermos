from flask_wtf import Form
from wtforms.fields import StringField
from flask.ext.wtf.html5 import URLField
from wtforms.validators import DataRequired, url

class BookmarkForm(Form):
    url = URLField('url', validators=[DataRequired(), url()])
    description = StringField('description')

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
