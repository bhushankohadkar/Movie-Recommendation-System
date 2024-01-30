import streamlit as st
import pickle
import pandas as pd
import requests
from PIL.Image import Image

movies_list = pickle.load(open('movie_dict.pkl','r'))
similarity = pickle.load(open('similarity.pkl','r'))



movies = pd.DataFrame(movies_list)


st.header("Movie Recommendation System")  # title
select_movie_name = st.selectbox('Select Movie name', movies['title'].values)

def director(movie_id):
    response4 = requests.get(
        'https://api.themoviedb.org/3/movie/{}/credits?api_key=84d4ec28fa85fa521aa54fe07c45f31d&language=en-US'.format(movie_id))
    data4 = response4.json()
    for i in range(0, len(data4["crew"])):
        if data4["crew"][i]["job"] == "Director":
            break
    return data4["crew"][i]["name"]


def cast(movie_id):
    response3 = requests.get(
        'https://api.themoviedb.org/3/movie/{}/credits?api_key=84d4ec28fa85fa521aa54fe07c45f31d&language=en-US'.format(movie_id))
    data3 = response3.json()
    return data3["cast"][0]["name"]


def release_date(movie_id):
    response2 = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=84d4ec28fa85fa521aa54fe07c45f31d&language=en-US'.format(movie_id))
    data2 = response2.json()
    return data2['release_date']


def rating(movie_id):
    response1 = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=84d4ec28fa85fa521aa54fe07c45f31d&language=en-US'.format(movie_id))
    data1 = response1.json()
    # st.text(data1)
    vote_average = data1['vote_average']
    rating = round(vote_average, 1)
    return rating


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=84d4ec28fa85fa521aa54fe07c45f31d&language=en-US'.format(movie_id))
    data = response.json()
    # st.text(data)
    # st.text('https://api.themoviedb.org/3/movie/{}?api_key=84d4ec28fa85fa521aa54fe07c45f31d&language=en-US'.format(movie_id))
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    recommended_movies_release_date = []
    recommended_movies_cast = []
    recommended_movies_director = []
    recommended_movies_rating = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_poster.append((fetch_poster(movie_id)))

        recommended_movies_release_date.append(release_date(movie_id))

        recommended_movies_cast.append(cast(movie_id))

        recommended_movies_director.append(director(movie_id))

        recommended_movies_rating.append(rating(movie_id))

    return recommended_movies, recommended_movies_poster, recommended_movies_release_date, recommended_movies_cast, recommended_movies_director,  recommended_movies_rating


# create button
if st.button('Recommend'):
    names, posters, date, cast, direct, rate = recommend(select_movie_name)

    col1, col2 = st.columns([0.3, 1])
    with col1:
        st.image(posters[0])
    with col2:
        st.info(names[0])
        st.markdown("Release Date: " + date[0])
        st.markdown("Actor: " + cast[0])
        st.markdown("Director: " + direct[0])
        st.markdown("Rating: " + str(rate[0]))

    col3, col4 = st.columns([0.3, 1])
    with col3:
        st.image(posters[1])
    with col4:
        st.info(names[1])
        st.markdown("Release Date: " + date[1])
        st.markdown("Actor: " + cast[1])
        st.markdown("Director: " + direct[1])
        st.markdown("Rating: " + str(rate[1]))

    col5, col6 = st.columns([0.3, 1])
    with col5:
        st.image(posters[2])
    with col6:
        st.info(names[2])
        st.markdown("Release Date: " + date[2])
        st.markdown("Actor: " + cast[2])
        st.markdown("Director: " + direct[2])
        st.markdown("Rating: " + str(rate[2]))

    col7, col8 = st.columns([0.3, 1])
    with col7:
        st.image(posters[3])
    with col8:
        st.info("Movie Name: " + names[3])
        st.markdown("Release Date: " + date[3])
        st.markdown("Cast: " + cast[3])
        st.markdown("Director: " + direct[3])
        st.markdown("Rating: " + str(rate[3]))

    col9, col10 = st.columns([0.3, 1])
    with col9:
        st.image(posters[4])
    with col10:
        st.info(names[4])
        st.markdown("Release Date: " + date[4])
        st.markdown("Actor: " + cast[4])
        st.markdown("Director: " + direct[4])
        st.markdown("Rating: " + str(rate[4]))

