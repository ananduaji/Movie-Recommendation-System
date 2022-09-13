# Movie Recommendation System
### link : https://movie-recommendation-system-07.herokuapp.com/

## Overview
Movie Recommendation System is a machine learning based web application for recommending movies based on the film you like. This web application will predict five films according to you film taste. This type of movie recommendation is used in various streaming platforms like Netflix, Amazon Prime, Sonyliv etc.. This system is also integrated in different applications for better user experience. Like in Spotify for song recommendation.

## Demo
![](https://user-images.githubusercontent.com/90780162/189946025-b8cddd05-5f2d-430e-ba34-edcf16e937bd.jpeg)
![](https://user-images.githubusercontent.com/90780162/189946021-8e7706ea-5c70-4027-bf59-6a64d74f9110.jpeg)
![](https://user-images.githubusercontent.com/90780162/189946018-bd5f43f7-4a7a-4f79-85d9-455ac8914e9a.jpeg)
![](https://user-images.githubusercontent.com/90780162/189946015-83f4669c-4afe-4ad5-8a45-c23aec9356e1.jpeg)
![](https://user-images.githubusercontent.com/90780162/189946012-dff5b72f-6ee9-4727-8ff5-68f4df7c7d7f.jpeg)
![](https://user-images.githubusercontent.com/90780162/189946007-1a02cc3a-14dc-4913-810f-2f40f15a6e55.jpeg)

## Recommender Systems
Recommender systems use algorithms to provide users with useful recommendations for products or services. Recently, these systems have been using machine learning algorithms from the field of artificial intelligence. Recommendation system is categorized in four classes: 
1. Simple System using popularity
2. Collaborative Filtering
3. Content based
4. Hybrid based Approach

A recommendation system is being highly recognized as a part of our social life due to its strength in providing enhanced entertainment. Such a system will predict what movies a user will like based on various criterias like the attributes of previously liked movies by that user or the popularity of the movies. Although a set of movie recommendation systems have been proposed and implemented.

Here, in [my project](https://movie-recommendation-system-07.herokuapp.com/) I used Content based movie recommendation system. 
### Content-Based Recommendations systems 
Content-Based Recommendations systems are the systems that look for similarity before recommending something. The similarity of different movies is computed to the one you are currently watching and all the similar movies are recommended to us. 

## Project Roadmap
This project is divided into two part:
1. Training a machine learning model using scikit-learn.
   * Loaded the dataset.
   * Done some Feature engineering like, feature selection, handling null values.
   * Made a column which contain all the keywords of that specific film.
   * By using 'nltk' library done stemming and lemmatization.
   * Using CountVectoriser from sklearn vectorized the words.
   * By finding the Cosine similarity got a list contains every similarity between every movies. 
      - we find the similarity by calculating the angle distances from each vectors.
      - distance is the inverse of the similarity
      - if distance is less then similarity is higher
      - if distance is higher the similarity is less
   * Finally made a function that recommends 5 film according to the film that we choose.
2. Building and hosting a Flask web app on Heroku.
   * User can simply type and find the movie that they like. When they tap recommend it shows 5 movies that are similar to that film. 
   
 ## Technologies Used
 <div style="display:flex">
   <img src="https://user-images.githubusercontent.com/90780162/189960536-19dccc7d-710f-4771-b00e-8cbc31bceda7.png" width=480 height=140 />
   <img src="https://user-images.githubusercontent.com/90780162/189960533-af11f611-fff7-47e6-98e9-e09d21895ad3.png" width=300 height=121 />
   <img src="https://user-images.githubusercontent.com/90780162/189960530-5b19fa69-4d10-4ace-9054-9f048baa8333.png" width=179 height=195 />
   </div>
    <div style="display:flex">   
   <img src="https://user-images.githubusercontent.com/90780162/189960540-37c01d5f-936b-4632-a220-3fe883abad9a.png" width=320 height=172 />
   <img src="https://user-images.githubusercontent.com/90780162/189960506-d565a0ed-2973-47d1-8d1a-37da2c8dd856.png" width=320 height=125 />
   <img src="https://user-images.githubusercontent.com/90780162/189960528-1c73eb83-2aa7-4997-93ce-3a1dbe0b6d4d.jpg" width=262 height=150 />
   </div>
   <br><br>
   <div style="display:flex"> 
   <img src="https://user-images.githubusercontent.com/90780162/189960520-7aff317b-d1b1-48d9-8e72-78b066ef5159.png" width=398 height=113 />
   <img src="https://user-images.githubusercontent.com/90780162/189960527-81729ea3-bc6e-493f-8cb0-e107c53e6290.png" width=277 height=117 />
   </div>
   
   
