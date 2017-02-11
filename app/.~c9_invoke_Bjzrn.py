"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import smtplib
from app import app
from flask import render_template, request, redirect, url_for, flash


###
# Routing for your application.
###
message = """From: {} <{}>
            To: {} <{}> Subject: {}
            {}
            """



app.secret_key = 'some_secret'

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/')
@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/contact/', methods= ['GET','POST'])
def contact():
    if request.method == 'POST':
            name= request.form['name']
            flash("")
            subject= request.form['subject']
            message= request.form['message']
            
            send_email(name,email,subject,message)
            
            flash("Message Successfull Sent")
            
            return render_template({{ url_for('home') }}) 
           
    else:
            error = 'MADNIS!'
            return render_template('contact.html', error=error)

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
    
    
def send_email(from_name, from_email, subject, msg):
    to_addr= 'jhenaidixon@ymail.com'
    to_name= "jhenai"
    message_to_send = message.format(from_name, from_email, to_name, to_addr, subject, msg)
    username = 'jhenaidixon@gmail.com'
    password = 'jfcvzbgjrppunznp'
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_addr, message_to_send)
    server.quit()
    
    

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")