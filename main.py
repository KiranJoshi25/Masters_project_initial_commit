from flask import Flask, request, render_template
import processing
app = Flask(__name__,template_folder='template')

@app.route('/')
def my_form():
    return render_template('form.html',some_var = '')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = processing.process(text)
    print(processed_text)
    new_text = []
    for i in processed_text:

        new_text.append(i)
    #some_var = new_text
    return render_template('form.html',some_var = new_text)

#if __name__=='__main__':
app.run()