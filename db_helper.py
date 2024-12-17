from joblib import load

load_data = load("artifact/save_model.joblib")
df = load_data['dataframe']
similarity = load_data['similarity']


import requests

# Function to recommend movies
def recommend(selected_movie):
    # Logic to compute recommendations based on similarity
    # Example: similarity is precomputed
    idx = df[df['original_title'] == selected_movie].index[0]
    movie_scores = list(enumerate(similarity[idx]))
    sorted_scores = sorted(movie_scores, key=lambda x: x[1], reverse=True)
    recommended_indices = [x[0] for x in sorted_scores[1:10]]  # Top 10 movies
    return df['original_title'].iloc[recommended_indices].tolist()




# Function to fetch movie poster
def fetch_movie_poster(movie_title):
    # Replace API_KEY with your actual API key
    API_KEY = "b80abaee7590739e7ccaad6750d24910"
    base_url = "https://api.themoviedb.org/3/search/movie"
    image_base_url = "https://image.tmdb.org/t/p/w500"
    try:
        # Make request to TMDB API
        response = requests.get(base_url, params={"api_key": API_KEY, "query": movie_title})
        data = response.json()
        if data["results"]:
            poster_path = data["results"][0].get("poster_path")
            if poster_path:
                return f"{image_base_url}{poster_path}"
        return "https://via.placeholder.com/300x450?text=No+Poster+Available"  # Placeholder
    except Exception as e:
        return "https://via.placeholder.com/300x450?text=Error+Fetching+Poster"
