import streamlit as st
from joblib import load
from db_helper import recommend,fetch_movie_poster

load_data = load("artifact/save_model.joblib")
dataframe = load_data['dataframe']
similarity = load_data['similarity']

input_data = dataframe['original_title'].values

st.title('Movies Recommender')
select_input = st.selectbox("Input any film",[""] + input_data)

# The blue button
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50; /* Green background */
        color: white; /* White text */
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px; /* Rounded corners */
    }
    div.stButton > button:first-child:hover {
        background-color: #45a049; /* Darker green on hover */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
#Crete poster corresponding with input title
if st.button("Get Similar Movie Suggestions"):
    call_processing = recommend(select_input)  # Get recommended movies
    st.markdown("### Recommended Movies:")

    # Organize output with posters: 3 posters per row
    cols = st.columns(3)  # Create 3 columns for the first row

    for i, movie in enumerate(call_processing):
        col = cols[i % 3]  # Select the column based on index
        with col:
            poster_url = fetch_movie_poster(movie)  # Fetch the poster for the movie
            st.image(poster_url, caption=movie, use_container_width=True)

        # Create new row every 3 items
        if (i + 1) % 3 == 0 and (i + 1) != len(call_processing):
            cols = st.columns(3)  # Create a new set of 3 columns

