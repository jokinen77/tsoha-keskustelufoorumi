from flask_wtf import FlaskForm
from wtforms import validators, PasswordField, StringField, IntegerField
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

# class UpdateEmailForm(FlaskForm):
#     email = EmailField("New email", [validators.Email(message='Not valid email!')])
#
#     class Meta:
#         csrf = False
#
# class UpdatePasswordForm(FlaskForm):
#     password_new = PasswordField("New password", [validators.Length(min=4, max=255)])
#     password_new_re = PasswordField("Re-enter new password", [validators.EqualTo('password_new', message='Passwords much match!')])
#     password_old = PasswordField("Old password")
#
#     class Meta:
#         csrf = False
#
# class NewUserFrom(FlaskFrom):
#     name = StringField("name", [validators.Length(min=4, max=255)])
#     username = StringField("username", [validators.Length(min=4, max=255)])
#     email = EmailField("New email", [validators.Email(message='Not valid email!')])
#     password = PasswordField("New password", [validators.Length(min=4, max=255)])
#     password_re = PasswordField("Re-enter new password", [validators.EqualTo('password', message='Passwords much match!')])
#     usertype_id = IntegerField('')
