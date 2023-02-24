from app import app
###############################################
#          Import some packages               #
###############################################
from flask import Flask, render_template, request, flash
from flask_datepicker import datepicker
from forms import ContactForm
from forms import NewsLetterForm
import pandas as pd
import datetime

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/specials')
def specials():
    return render_template('specials.html', title='Specials')
@app.route('/products')
def products():
    return render_template('products.html', title='Products')

@app.route('/raspcheese')
def raspcheese():
    return render_template('raspcheese.html', title = 'Products')

@app.route('/custardtart')
def custardtart():
    return render_template('custardtart.html', title = 'Products')

@app.route('/vanilaslice')
def vanilaslice():
    return render_template('vanilaslice.html', title = 'Products')

@app.route('/donuts')
def donuts():
    return render_template('donuts.html', title = 'Products')

@app.route('/randytart')
def randytart():
    return render_template('randytart.html', title = 'Products')
    
@app.route('/applecake')
def applecake():
    return render_template('applecake.html', title = 'Products')


###############################################
#       Render Contact page                   #
###############################################
@app.route('/contactus', methods=["GET","POST"])
def get_contact():
    form = ContactForm()
    if request.method == 'POST' and form.validate_on_submit():
        name =  request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
        res.to_csv('./contactusMessage.csv', mode ='a')
        
        return render_template('index.html', form=form)
    else:
        return render_template('contact.html', form=form)

###############################################
#       Render News letter page               #
###############################################
@app.route('/newsletter', methods=["GET","POST"])
def get_newsletter():
    form = NewsLetterForm()
    if request.method == 'POST' and form.validate_on_submit():
        name =  request.form["name"]
        email = request.form["email"]
        preference = request.form["preference"]
        birthday = request.form["birthday"]
        radio = request.form["radio"]
        res = pd.DataFrame({'name':name, 'email':email,'birthday':birthday,'preference':preference,'radio': radio}, index=[0])
        res.to_csv('./newsletter.csv', mode ='a')

        return render_template('index.html', form=form)
    else:
        return render_template('newsletter.html', form=form)