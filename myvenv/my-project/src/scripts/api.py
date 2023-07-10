# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, render_template, redirect, url_for

#import the user defined function to transform the user input
from transformation import transform

# creating a Flask app and importing the html from templates folder
app = Flask(__name__,template_folder='../templates/')


# on the terminal type: curl http://127.0.0.1:5000/
@app.route('/')
def home():
    return render_template('index.html',leftTextAreaValue='Your code here',rightTextAreaValue='Your result here')


@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        userCode=request.form['leftTextArea']
        document=transform(userCode).getResult()
    
    return redirect(url_for('output',inp=userCode,out=document))


@app.route('/output', methods=['get'])
def output():
    inp1 = request.args.get('inp')
    out1 = request.args.get('out')
    return render_template('index.html',leftTextAreaValue=inp1,rightTextAreaValue=out1)


# driver function
if __name__ == '__main__':
    app.run(debug = True)
