# from project import app
from .. import login_manager
from flask import flash, redirect, render_template, request, Blueprint, url_for, session
from forms import loginForm, registrationForm, resetPasswordForm, emailVerificationForm
from project.models import User
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from ..helper import sendEmail, generateOTP


app_blueprint = Blueprint('my_view', __name__)
data = {}


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# -----------------------INDEX-----------------------------

@app_blueprint.route('/')
def index():
    return render_template('index.html')

# ---------------------HOME--------------------------------

@app_blueprint.route('/home')
@login_required
def home():
    return render_template('home.html')


# -------------------------LOGIN--------------------------


@app_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(
            email=form.username.data, password=form.password.data).first()
        if user:
            session['email'] = user.email
            if(not user.email_verified):
                data['otp'] = generateOTP()
                sendEmail(user.email, data['otp'])
                data['fromReg'] = False
                login_user(user)
                flash("Enter OTP sent on your mail to verify", "info")
                return redirect(url_for('my_view.email_verification'))
            login_user(user)
            flash('login successful')
            return redirect(url_for('my_view.home'))
        else:
            flash('Login unsuccessful Please check username and password', 'danger')
    return render_template('login.html', form=form)


# ---------------------REGISTRATION-----------------------

@app_blueprint.route('/regi', methods=['GET', 'POST'])
def registrationform():
    form = registrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            u1 = User(name=form.name.data, phone=form.phone.data,
                      email=form.email.data, password=form.password.data)
            u1 = u1.save()
            data['otp'] = generateOTP()
            data['fromReg'] = True
            session['email'] = form.email.data
            sendEmail(form.email.data, data['otp'])
            flash("Enter OTP sent on your mail to verify", "info")
            return redirect(url_for('my_view.email_verification'))
    return render_template('registration.html', form=form)


# ---------------------RESET--------------------------------

@app_blueprint.route('/reset', methods=['GET', 'POST'])
def reset():
    form = resetPasswordForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return '<h1> The  New Password is {}'.format(form.new_password.data)
        return render_template('reset.html', form=form)
    return render_template('reset.html', form=form)

# ------------------------EMAIL_VERIFICATION--------------------------

@app_blueprint.route('/email_verification', methods=['GET', 'POST'])
def email_verification():
    form = emailVerificationForm()
    otp = data['otp']
    if request.method == 'POST':
        if form.validate_on_submit():
            if(otp == form.otp_field.data):
                user = User.query.filter_by(email=session['email']).first()
                user.email_verified = 1
                user.update()
                if(data['fromReg']):
                    return redirect(url_for('my_view.login'))
                flash("Email Verified!!")
                return redirect(url_for('my_view.home'))
            flash("Invalid OTP!!")
            return redirect(url_for('my_view.email_verification'))
    return render_template('email_verification.html', form=form)

# -----------------------------LOGOUT---------------------------------------

@app_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout Successful!!')
    return redirect (url_for('my_view.login'))

