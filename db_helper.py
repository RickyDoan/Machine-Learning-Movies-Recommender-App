import streamlit as st
from joblib import load

load_data = load("artifact/save_model.joblib")
df = load_data['dataframe']
similarity = load_data['similarity']





def recommend(title):
    list_film = []
    index = df[df['original_title']==title].index[0]
    distances = sorted([*enumerate(similarity[index])], key=lambda x: x[1], reverse=True)
    for value in distances[1:10]:
        get = df.iloc[value[0]]['original_title']
        list_film.append(get)
    return list_film


import requests


# Define the function to fetch the poster
def fetch_movie_poster(movie_title):
    """
    Fetch the poster URL for a given movie title from TMDb API.

    Args:
        movie_title (str): The title of the movie.

    Returns:
        str: URL of the movie poster.
    """
    api_key = "b80abaee7590739e7ccaad6750d24910"  # Replace with your actual TMDb API key
    base_url = "https://api.themoviedb.org/3/search/movie"
    image_base_url = "https://image.tmdb.org/t/p/w500"  # Base URL for poster images

    # Send a request to the TMDb API
    response = requests.get(base_url, params={"api_key": api_key, "query": movie_title})

    if response.status_code == 200:  # Check if the request was successful
        data = response.json()
        if data['results']:  # Check if results exist
            poster_path = data['results'][0].get('poster_path')  # Get the first movie's poster path
            if poster_path:
                return f"{image_base_url}{poster_path}"  # Construct the full poster URL
            else:
                return "Poster not available"
        else:
            return "Movie not found"
    else:
        return f"Error: {response.status_code}"


# Example usage:
poster_url = fetch_movie_poster("The Dark Knight")
print(poster_url)
