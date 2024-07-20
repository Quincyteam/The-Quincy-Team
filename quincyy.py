from flask import Flask, render_template

app = Flask("QUINCY")

@app.route('/')
def home():
    return render_template('index.html')

if QUINCY =='_main_':
    app.run(debug=True)

