from flask import Flask, render_template, send_from_directory
import pandas as pd
import os

app = Flask(__name__)

# Load the CSV file
df = pd.read_csv('./static/images/review.csv')

@app.route('/')
def home():
    return render_template('home.html')

# Route for the homepage
@app.route('/review')
def index():
    films = df.to_dict(orient='records')
    return render_template('index.html', films=films)

# Route for the individual film review page
@app.route('/review/<int:film_id>')
def review(film_id):
    film = df.iloc[film_id]
    return render_template('review.html', film=film)

# Route to serve images
@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory(os.path.dirname(df['images'][0]), os.path.basename(filename))

@app.route('/yiyi')
def yiyi():
    return render_template('yiyi.html')

if __name__ == '__main__':
    app.run(debug=True)

