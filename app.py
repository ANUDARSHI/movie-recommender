from tkinter import image_names
from flask import Flask,render_template,request
import requests
import pickle
import pandas as pd
import zipfile

df2 = pd.read_csv('tmdb_5000_movies.csv')

df2 = df2.reset_index()
all_titles = [df2['title'][i] for i in range(len(df2['title']))]
movies = pickle.load(open('movie_list.pkl','rb'))
with zipfile.ZipFile('similarity.zip', 'r') as zip_ref:
    zip_ref.extractall('similarity')

similarity = pickle.load(open('./similarity/similarity.pkl','rb'))

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=69b78a69e3fd67e2141566d7ba44b36a&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
    
def fetch_imdb(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=69b78a69e3fd67e2141566d7ba44b36a&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    imdb_id = data['imdb_id']
    imdb_path = "https://www.imdb.com/title/" + imdb_id
    return imdb_path

def fetch_desc(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=69b78a69e3fd67e2141566d7ba44b36a&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    desc = data['overview']
    return desc

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_desc=[]
    imdb_link=[]

    for i in distances[1:7]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_desc.append(fetch_desc(movie_id))
        imdb_link.append(fetch_imdb(movie_id))



    return recommended_movie_names,recommended_movie_posters,recommended_movie_desc,imdb_link


app = Flask(__name__)
app.config['SECRET_KEY']='little phuchki'


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == "POST":
        input_name=request.form['movie_name']
        input_name=input_name.title()

        if input_name not in all_titles:
            return(render_template('404.html',name=input_name))

        else:
            recommended_movie_names,recommended_movie_posters,recommended_movie_desc,imdb_link=recommend(input_name)
            # print(recommended_movie_names)
            # print(recommended_movie_posters)

            return(render_template('success.html',image1=recommended_movie_posters[0],image2=recommended_movie_posters[1],image3=recommended_movie_posters[2],image4=recommended_movie_posters[3],image5=recommended_movie_posters[4],image6=recommended_movie_posters[5],name1=recommended_movie_names[0],name2=recommended_movie_names[1],name3=recommended_movie_names[2],name4=recommended_movie_names[3],name5=recommended_movie_names[4],name6=recommended_movie_names[5],desc1=recommended_movie_desc[0],desc2=recommended_movie_desc[1],desc3=recommended_movie_desc[2],desc4=recommended_movie_desc[3],desc5=recommended_movie_desc[4],desc6=recommended_movie_desc[5],url1=imdb_link[0],url2=imdb_link[1],url3=imdb_link[2],url4=imdb_link[3],url5=imdb_link[4],url6=imdb_link[5]))
            
        
    else:
       return(render_template('home.html',movies=all_titles))


if __name__ == '__main__':
    app.run()
