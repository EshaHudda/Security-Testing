from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            message = f"Hello, {name}!"
        else:
            message = "Please enter your name."
    return render_template('index.html', message=message)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)