"""HW2: Application that supports campus study spaces:
    1) Building name 2)Building code 3)Building Floor 4)Closeest room number
    5) Rating is stored
    

    
"""
from flask import Flask, redirect, url_for, request, render_template
from index import Index
from sign import Sign

app = Flask(__name__)       # our Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=['GET','POST'])
  
    
app.add_url_rule('/sign',
                 view_func=Sign.as_view('sign'),
                 methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
