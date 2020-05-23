from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.template.html')

<<<<<<< HEAD
=======

>>>>>>> 78a6ef75ac1bb4fe166038e4635ca0ef524a5b40
@app.route('/gallery')
def gallery():
    return render_template('gallery.template.html')

<<<<<<< HEAD
=======


>>>>>>> 78a6ef75ac1bb4fe166038e4635ca0ef524a5b40
# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)