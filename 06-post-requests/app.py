from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


# your code here!
@app.route("/")
def hello():
    return render_template("index.template.html")


@app.route("/", methods=['POST'])
def processHello():
    fn = request.form.get('first-name')
    ln = request.form.get('last-name')
    return render_template('process-hello.template.html', fn=fn, ln=ln)


@app.route("/calculate")
def calculate():
    return render_template("calculate.template.html")


@app.route("/calculate", methods=['POST'])
def calculate_results():
    number1 = int(request.form.get('number1'))
    number2 = int(request.form.get('number2'))
    sum = number1 + number2
    return render_template("results.template.html", result=sum)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
