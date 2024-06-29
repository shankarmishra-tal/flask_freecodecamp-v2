from flask import Flask , render_template
from database import load_jobs


app = Flask(__name__)


JOBS = load_jobs()

@app.route('/')
def hello_world():
    return render_template('index_1.html' , jobs = JOBS)




if __name__ == '__main__':
    app.run(debug=True)
