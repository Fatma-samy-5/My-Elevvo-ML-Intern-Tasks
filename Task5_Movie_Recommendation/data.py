import pandas as pd

# Adding 'r' before the path string to handle backslashes
movies = pd.read_csv(r"D:\Elevvo_ML\dataset of task5\ml-100k\u.item", sep='|', encoding='latin-1', header=None, 
                     names=['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_URL', 'unknown', 'Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western'])

ratings = pd.read_csv(r"D:\Elevvo_ML\dataset of task5\ml-100k\u.data", sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])

print("Data loaded successfully!")