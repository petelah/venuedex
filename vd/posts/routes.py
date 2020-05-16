from flask import render_template, url_for, flash, redirect, request, abort
from vd import db
from vd.posts.forms import BizPostForm
from vd.models import Business
from vd.utilities.utils import webhandler, fbhanlder, instahandler
#from flask_login import current_user, login_required

from flask import Blueprint

posts = Blueprint('posts', __name__)

@posts.route("/add_business", methods=['GET', 'POST'])
def add_business():
    form = BizPostForm()
    # Submit form and check everything is valid
    if form.validate_on_submit():
        post = Business(business_name=form.business_name.data,
                    desc=form.desc.data,
                    email=form.email.data,
                    address=form.address.data,
                    phone=form.phone.data,
                    menu=form.menu.data,
                    food=form.food.data,
                    booze=form.booze.data,
                    pickup=form.pickup.data,
                    selfd=form.selfd.data,
                    uber=form.uber.data,
                    deliveroo=form.deliveroo.data,
                    bopple=form.bopple.data,
                    instagram=form.instagram.data,
                    facebook=form.facebook.data,
                    spinfo=form.spinfo.data,
                    region=form.region.data)
        # Handle web addresses
        if len(post.facebook) > 1:
            post.facebook = str(fbhanlder(post.facebook))
        if len(post.instagram) > 1:
            post.instagram = str(instahandler(post.instagram))
        if len(post.menu) > 1:
            post.menu = str(webhandler(post.menu))
        # Add post
        db.session.add(post)
        # Commit post
        db.session.commit()
        # Add flash function later
        #flash('', 'success')
        return redirect(url_for('main.home'))
    return render_template('add_business.html', form=form)

@posts.route("/venues/sydney")
def sydney():
    venues = Business.query.order_by(Business.date_posted.desc())
    #vencount = Business.count()
    return render_template('sydney.html', venues=venues)
