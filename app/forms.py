from flask_wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required, Length

class LoginForm(Form):
    user_login = TextField('login', validators = [Required()])
    user_password = TextField('password', validators = [Required()])
    user_email = TextField('email', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)
    #https://openid.stackexchange.com/
    #https://openid-provider.appspot.com/rolanlane
    #http://google.com/profiles/rolanlane

class EditForm(Form):
    nickname = TextField('nickname', validators = [Required()])
    about_me = TextAreaField('about_me', validators = [Length(min = 0, max = 140)])

    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        if self.nickname.data != User.make_valid_nickname(self.nickname.data):
            self.nickname.errors.append(gettext('This nickname has invalid characters. Please use letters, numbers, dots and underscores only.'))
            return False
        user = User.query.filter_by(nickname = self.nickname.data).first()
        if user != None:
            self.nickname.errors.append(gettext('This nickname is already in use. Please choose another one.'))
            return False
        return True

class PostForm(Form):
    post = TextField('post', validators = [Required()])

class SearchForm(Form):
    search = TextField('search', validators = [Required()])