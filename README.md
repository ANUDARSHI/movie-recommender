
# Movie Recommendation System
  ## Frameworks and languages used 

![Python](https://img.shields.io/badge/Python-3.8-blueviolet)

![Framework](https://img.shields.io/badge/Framework-Flask-blue)

![Frontend](https://img.shields.io/badge/Frontend-HTML/CSS/JS-pink)

[![PyPI version shields.io](https://img.shields.io/pypi/v/trains-jupyter-plugin.svg)](https://img.shields.io/pypi/v/trains-jupyter-plugin.svg)

This is a Movie Recommendation system based on similarity based filtering using cosine similarity .

I used **[tmdb movie data set](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)** 

In this website type or choose a movie name from the list of movies and it will provide the name poster and url link of top 6 movies which are fetched using an API by TMDB, https://www.themoviedb.org/documentation/api

## How does the project works 

   How does it decide which item is most similar to the item user likes? Here come the similarity scores.
   
   It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

   ### How Cosine Similarity works?
  Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

## How to use

1. Clone this repository to your local machine.
2. Install all the libraries mentioned in the [requirements.txt](https://github.com/kishan0725/Movie-Recommendation-System-with-Sentiment-Analysis/blob/master/requirements.txt) file with the command `pip install -r requirements.txt`
4. Open your terminal/command prompt from your project directory and run the file `main.py` by executing the command `python main.py`.
5. Go to your browser and type `http://127.0.0.1:5000/` in the address bar.

## Screenshots of My project

### Home Page of My website to search for Movies
![home](https://user-images.githubusercontent.com/89626174/170729941-2fcc6098-c1a7-4f66-895e-4902083e1605.jpg)

### Recommendation Page of My website (showcasing top 6 recommended movies of the selected movie)
![success](https://user-images.githubusercontent.com/89626174/170729955-c646a7b5-699c-4897-aa7c-c484da30f5a4.jpg)
