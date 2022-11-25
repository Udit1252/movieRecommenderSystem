import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    response = response.json()
    poster_path = response['poster_path']
    poster = "https://image.tmdb.org/t/p/w500/" + poster_path
    return poster





def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse = True, key = lambda x:x[1])[1:6]
    
    recommend_movies = []
    recommend_movies_poster = []
    for i in distances:
        movie_id = movies_df.iloc[i[0]].id
        # Fetch poster from api
        recommend_movies.append(movies_df.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))
    
    return recommend_movies,recommend_movies_poster




movies_df = pickle.load(open('movies.pkl','rb'))

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
selectedMovieName = st.selectbox("TYPE MOVIE FOR RECOMMENDATION", movies_df['title'].values)

if st.button('RECOMMEND'):
    recommendations,poster = recommend(selectedMovieName)
    for i in range(len(recommendations)):
        st.header(recommendations[i])
        st.image(poster[i])
    # col1, col2, col3, col4, col5 = st.columns(5)
    # with col1:
    #     st.text(recommendations[0])
    #     st.image(poster[0])
    # with col2:
    #     st.text(recommendations[1])
    #     st.image(poster[1])
    # with col3:
    #     st.text(recommendations[2])
    #     st.image(poster[2])
    # with col4:
    #     st.text(recommendations[3])
    #     st.image(poster[3])
    # with col5:
    #     st.text(recommendations[4])
    #     st.image(poster[4])


