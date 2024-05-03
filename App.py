from flask import Flask , render_template ,jsonify

JOBS = [
    {
        'id' : 1,
        'title' : 'Tester',
        'location' : 'Ha Noi',
        'salary' : '10000$'
    },
    {
        'id' : 2,
        'title' : 'Game Developer',
        'location' : 'Ha Noi',
        'salary' : '15000$'
    },
    {
        'id' : 3,
        'title' : 'Game Design',
        'location' : 'Ha Noi',
        'salary' : '20000$'
    },
    {
        'id' : 4,
        'title' : 'Data Analyst',
        'location' : 'Ha Noi',
        'salary' : '30000$'
    },
    {
        'id' : 5,
        'title' : 'Dancer',
        'location' : 'Ha Noi',
        'salary' : '30000$'
    },
    {
        'id' : 6,
        'title' : 'Singer',
        'location' : 'Ha Noi',
        'salary' : '30000$'
    },
    
]

app = Flask(__name__)
@app.route("/")
def HelloWord():
    return render_template("home.html",jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)