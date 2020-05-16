from flask import render_template, Blueprint, redirect, request, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from vd import db, bcrypt
from vd.models import User, Business
from vd.admin.forms import LoginForm

admin = Blueprint('admin', __name__)

@admin.route("/admin", methods=['GET','POST'])
@login_required
def admin_panel():
    venues = Business.query.order_by(Business.date_posted.desc())
    return render_template('admin_panel.html', venues=venues)

@admin.route("/admin/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.admin_panel'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user=form.user.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('admin.admin_panel'))
        # else:
        #     flash('Login not work. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@admin.route("/admin/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@admin.route("/admin/delete/<int:id>", methods=['POST'])
@login_required
def delete_business(id):
    business = Business.query.get_or_404(id)
    db.session.delete(business)
    db.session.commit()
    flash('Post Deleted', 'success')
    return redirect(url_for('admin.admin_panel'))

@admin.route("/admin/approve/<int:id>", methods=['POST'])
@login_required
def approve_business(id):
    business = Business.query.get_or_404(id)
    business.approved = True
    db.session.commit()
    flash('Post Approved', 'success')
    return redirect(url_for('admin.admin_panel'))
