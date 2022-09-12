from flask import Flask, redirect, url_for, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_df = pd.DataFrame(movies_list)
movies = movies_df['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))


@app.route('/')
def welcome():
    return render_template('index.html', movie_names=movies)


@app.route('/recommend/<movie_name>')
def recommend(movie_name):
    movie_index = movies_df[movies_df['title'] == movie_name].index[0]
    similarities = similarity[movie_index]
    sorted_sim = list(enumerate(similarities))
    sorted_sim.sort(reverse=True, key=lambda x: x[1])
    movie_list = sorted_sim[1:6]

    recommended_movies = []
    for (i, j) in movie_list:
        film = movies_df['title'][i]
        recommended_movies.append(film)
    return render_template('recommendation.html', recommendation=recommended_movies)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        the_movie = request.form['movie']
    return redirect(url_for('recommend', movie_name=the_movie))


if __name__ == '__main__':
    app.run(debug=True)
