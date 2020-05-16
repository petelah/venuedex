from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email
from wtforms_components import SelectField

class BizPostForm(FlaskForm):
    business_name = StringField('Business Name:', validators=[DataRequired()], render_kw={"placeholder": "Business Name"})
    desc = TextAreaField('Business Info:', validators=[DataRequired()], )
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    address = StringField('Address:', validators=[DataRequired()], render_kw={"placeholder": "200 some St, Sydney CBD, 2000"})
    phone = IntegerField('Phone:', render_kw={"placeholder": "0412 345 678 (if you want to be called)"})
    menu = StringField('Menu: (website link)', render_kw={"placeholder": "www.example.com.au"})
    food = BooleanField('Food:')
    booze = BooleanField('Booze:')
    pickup = BooleanField('Pickup:')
    selfd = BooleanField('Self Delivery:')
    uber = BooleanField('Uber Eats:')
    deliveroo = BooleanField('Deliveroo:')
    bopple = BooleanField('Bopple:')
    instagram = StringField('Instagram:', validators=[DataRequired()], render_kw={"placeholder": "@examplebar"})
    facebook = StringField('Facebook:', validators=[DataRequired()], render_kw={"placeholder": "www.facebook.com/examplebar"})
    spinfo = TextAreaField('Special Info:', validators=[DataRequired()], render_kw={"placeholder": "IE: DM on instagram to order"})

    region = SelectField(u'Area:',
                         choices=(
    ('Sydney', (
        ('SYD-CBD', 'CBD'),
        ('ES', 'Eastern Suburbs'),
        ('IW', 'Inner West'),
        ('SS', 'South Sydney'),
        ('NS', 'North Sydney'),
        ('NB', 'Northern Beaches'),
        ('WS', 'Western Sydney')
    )),
    ('Melbourne', (
        ('MEL-CBD', 'CBD'),
        ('FR', 'Fitzroy'),
        ('CW', 'Collingwood'),
        ('SK', 'St. Kilda')
    )),
    ('Brisbane', (
        ('BRIS-CBD', 'CBD'),
        ('VY', 'Valley'),
        ('RC', 'Red Cliffe'),
        ('RC', 'Red Cliffe'),
    ))
))
    recaptcha = RecaptchaField()

    submit = SubmitField('Submit')