from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField, StringField, SelectField, RadioField
from wtforms.validators import DataRequired, InputRequired, Length, Email, ValidationError
from datetime import date
from wtforms.fields.html5 import DateField


class ContactForm(FlaskForm):
    name = StringField("Name",[DataRequired()])
    email = StringField('Email',[Email(message=('* Not a valid email address.')),DataRequired()])
    subject = TextField("Subject",[DataRequired()])
    message = TextAreaField('Message',[DataRequired(),Length(min=4,message=('* Your message is too short.'))])
    submit = SubmitField("Send")
    

class NewsLetterForm(FlaskForm):
    name = TextField("Name",[DataRequired()])
    birthday = DateField("Birthday", format="%Y-%m-%d",validators=[DataRequired(message="You need to select your birthday")])
    email = StringField("Email",[Email(message=('* Not a valid email address.')),DataRequired()])
    submit = SubmitField("Subscribe")
    preference =  SelectField("Preference",[DataRequired()],choices=[
            ('donuts', 'Donuts'),
            ('vanila slice', 'Vanila Slice'),
            ('randy tart', 'Randy Tart'),
            ('custard tart', 'Custard Tart'),
            ('raspberry cheesecake', 'Raspberry Cheesecake'),
            ('apple cake slice', 'Apple Cake Slice')
        ]
    )
    
    radio = RadioField('radio', choices=[('Subscribe','Yes'),('Not Subscribe','No')])
    
    