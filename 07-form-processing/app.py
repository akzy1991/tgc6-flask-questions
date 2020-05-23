from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.template.html')

@app.route('/book')
def book():
    return render_template('book.template.html')

@app.route('/process_booking', methods=['POST'])
def process_booking():
    name = request.form.get('name')
    sitting = request.form.get('sitting')
    time = request.form.get('time')
    services = request.form.getlist('services')
    hear_about_us = request.form.get('hear-about-us')

    return render_template('form-process.template.html',
                            name=name,
                            sitting=sitting,
                            time=time,
                            services=", ".join(services),
                            hear_about_us=hear_about_us)



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
