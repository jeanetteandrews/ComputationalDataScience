import pandas as pd
import difflib

filename1 = 'movie_list.txt'
filename2 = 'movie_ratings.csv'

movie_list = pd.read_csv(filename1, sep="\n", header=None)
movie_ratings = pd.read_csv(filename2)

titles_list = movie_list[0].tolist()

def close_matches(word):
    match = difflib.get_close_matches(word, titles_list, n=1, cutoff=0.6)
    match = ''.join(match)
    if (match == ''):
        return None
    else:
        return match
    
movie_ratings['matched'] = movie_ratings['title'].apply(close_matches)
movie_ratings = movie_ratings.dropna()

temp = movie_ratings.groupby(['matched'], as_index=False).sum()
temp2 = movie_ratings.groupby(['matched'], as_index=False).count()
temp['count'] = temp2['rating']

d = {'title': temp['matched'], 'rating': round(temp['rating'].div(temp['count']),2)}
finaldf = pd.DataFrame(data=d)

finaldf.to_csv('output.csv')

