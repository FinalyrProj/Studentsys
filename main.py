from flask import Flask,render_template,request


app=Flask(__name__)
app.config['SECRET_KEY'] = "cc7c83c25c81641609b40dbaf2038e12"

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html")

@app.route('/help', methods=['GET', 'POST'])
def help():
    return render_template("help.html")

@app.route('/CheckExam', methods=['GET', 'POST'])
def CheckExam():
    return render_template("exam.html")

@app.route('/FillFees', methods=['GET', 'POST'])
def FillFees():
    return render_template("adminfees.html")

@app.route('/RegisterEvents', methods=['GET', 'POST'])
def RegisterEvents():
    return("this is Events page")

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)