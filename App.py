from idlelib.format import reformat_comment

import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    requests.get()
def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1: 6]

        recommend_movies = []
        for i in movies_list:
            movie_id = i[0]
            #fetch poster from API:-

            recommend_movies.append(movies.iloc[i[0]].title)
        return recommend_movies

movies = pickle.load(open('movies.pkl', 'rb'))
movie_titles = movies['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

print(movies)
st.title('Movie recommender System')

selected_movie_name = st.selectbox(
    'Select a movie',
movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
      st.write(i)
