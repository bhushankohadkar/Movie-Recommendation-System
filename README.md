# **Movie-Recommendation-System**
**URL** : https://movie-recommendation-system11-5f5a9cacdfb7.herokuapp.com/

 **Steps**
**Step 1: Data Loading and Preprocessing**

•	In this project, we begin by loading movie datasets from Kaggle. These datasets contain information about movies, including details like titles, genres, keywords, cast, crew, and overviews.

•	We merge these datasets based on the "title" column to create a comprehensive dataset containing all the relevant movie details.

•	We carefully select the most relevant attributes for our movie recommendation system. This step helps us focus on the critical information for our model.

•	We handle missing values and duplicates to ensure the quality of our data.

**Step 2: Data Transformation**

•	In this step, we transform and clean the textual data in the "genres," "keywords," "cast," "crew," and "overview" columns.

•	Since these columns contain JSON-formatted data, we extract the most relevant information from them to use in our recommendation model.

**Step 3: Model Building**

•	We create a content-based recommendation model based on various movie attributes. This model considers movie descriptions, genres, keywords, cast, and crew.

•	To convert textual data into numerical features that the model can work with, we use the Bag of Words approach. Specifically, we employ the CountVectorizer to transform the text into numerical vectors.

•	Next, we calculate the cosine similarity between movies based on these numerical features. This similarity measure helps us identify how closely related one movie is to another.

**Step 4: Streamlit Web Application**

•	To make our recommendation system accessible and user-friendly, we have created a Streamlit web application.

•	Streamlit is a fantastic tool for deploying machine learning models and projects without the need to worry about the frontend. It simplifies the development process.

•	In the Streamlit app, users can select a movie from a dropdown menu.

•	When the user clicks the "Recommend" button, the app uses the content-based model to suggest similar movies based on the selected movie.

•	As an additional feature, we integrate APIs to fetch dynamic data, such as movie posters. This adds a visually appealing aspect to the user experience.

**Step 5: Deployment on Heroku**

•	Finally, we deployed the Streamlit web application on Heroku.

•	Heroku is a cloud platform that provides a Platform as a Service (PaaS). It supports multiple programming languages and simplifies the deployment process.

•	Once the app is deployed, it becomes accessible via the web, allowing users to interact with the movie recommendation system online.
