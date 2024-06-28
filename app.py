from flask import Flask , render_template

app = Flask(__name__)


JOBS = [
   {
       'id': 1,
       'title': 'Software Engineer',
       'company': 'ABC Corp',
       'description': 'We are looking for a talented software engineer with experience in Python and JavaScript.',
       'image': 'cabin.png',
       'location': 'Pune'
   },
   {
       'id': 2,
       'title': 'Data Scientist Engineer',
       'company': 'Talentica Corp',
       'description': 'We are looking for a talented Data engineer with experience in Python and JavaScript.',
       'image': 'cake.png',
       'location': 'Hyderabad'
   },
    {
       'id': 3,
       'title': 'Sr Developer ',
       'company': 'Talentica Corp',
       'description': 'We are looking for a talented Data engineer with experience in Python and JavaScript.',
       'image': 'circus.png',
       'location': 'Mumbai'
   },
    {
       'id': 4,
       'title': 'DevOps Engineer ',
       'company': 'Talentica Corp',
       'description': 'We are looking for a talented Data engineer with experience in Python and JavaScript.',
       'image': 'safe.png',
       'location': 'Pune'
   },
    {
       'id': 5,
       'title': 'Director of Cloud Engg ',
       'company': 'Talentica Corp',
       'description': 'We are looking for a talented Data engineer with experience in Python and JavaScript.',
       'image': 'cake.png',
       'location': 'Pune'
   },
   {
       'id': 6,
       'title': 'Director of Cloud Engg ',
       'company': 'Talentica Corp',
       'description': 'We are looking for a talented Data engineer with experience in Python and JavaScript.',
       'image': 'submarine.png',
       'location': 'Noida'
   }
]

@app.route('/')
def hello_world():
    return render_template('index_1.html' , jobs = JOBS)




if __name__ == '__main__':
    app.run(debug=True)
