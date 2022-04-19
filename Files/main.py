from flask import Flask, request, render_template
#import processing
app = Flask(__name__,template_folder='template')

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text,new_text = request.form['topic']
    new_var = text#processing.process(text)
    return render_template('index.html',new_var = new_var)



app.run()