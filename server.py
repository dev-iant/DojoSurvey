from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'bootyliciousforyababe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result')
def postresult():
    return render_template("result.html")

@app.route('/process', methods=['POST'])
def results():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['FavLang'] = request.form['FavLang']
    session['comment'] = request.form['comment']
    print('whoadude')
    return redirect('/result')

# @app.route("/")
# def index():
#     if "count" not in session:
#         session['count'] = 0
#     else:
#         session['count'] += 1
#     return render_template("index.html")

# @app.route("/reset")
# def reset():
#     session.clear()
#     return redirect('/')

if __name__=="__main__":
    app.run(debug=True, port=5005)