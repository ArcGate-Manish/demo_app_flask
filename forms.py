from email import message
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import input_required, Length, Email, Regexp, EqualTo
from wtforms.validators import ValidationError

# -----------------------login form-----------------------


class loginForm(FlaskForm):
    username = StringField('USERNAME', validators=[input_required(message='A username is required!'), Email(
        message="this is not email")])
    password = PasswordField('PASSWORD', validators=[input_required(message='password is required!'), Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
                                                                                                             message="Password must minimum contain 1 Uppercase 1 Lowercase 1 Number 1 Special Character and min char size must be 8")])
# ------------------------Registration form----------------------


class registrationForm(FlaskForm):
    name = StringField('NAME', validators=[input_required(
        message='This field can not be empty')])
    phone = StringField('PHONE', validators=[input_required(
        message="This field must not be empty"), Length(min=10, max=10)])
    email = EmailField('EMAIL', validators=[input_required(
        message='This field can not be empty'), Email()])
    password = PasswordField('NEW PASSWORD', validators=[input_required(message='This field can not be empty'), Length(
        min=8, max=50), EqualTo('password_confirm', message='Password must match'), Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
                                                                                           message="Password must minimum contain 1 Uppercase 1 Lowercase 1 Number 1 Special Character and min char size must be 8")])
    password_confirm = PasswordField('CONFIRM PASSWORD')

    def validate_phone(form, field):
        if(not field.data.isnumeric() or not int(field.data[0]) != 0):
            raise ValidationError("Phone Number is Invalid.")


# -----------------------Password Reset page----------------------


class resetPasswordForm(FlaskForm):
    new_password = PasswordField('NEW PASSWORD', validators=[input_required(message='This field can not be empty'), Length(
        min=8, max=50), EqualTo('new_password_confirm', message='Password must match'), Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
                                                                                               message="Password must minimum contain 1 Uppercase 1 Lowercase 1 Number 1 Special Character and min char size must be 8")])
    new_password_confirm = PasswordField('CONFIRM PASSWORD')


# -----------------------email_verification-------------------------


class emailVerificationForm(FlaskForm):
    otp_field = StringField('OTP', validators=[input_required(
        message="Can't be empty"), Length(min=6, max=6)])
    submit = SubmitField('Submit OTP')
