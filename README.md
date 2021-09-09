Aim: Salary prediction ML model with deployment in heroku cloud platform

Prerequisites: Scikit Learn, Pandas (for Machine Learning Model) and Flask (for API) installed.

Description: Implementation of end to end salary prediction with simple Linear Regression model in python. Performed EDA,preprocessing,training the model and dumped the trained model to a pickle file.Created a simple flask web framework and deployed using heroku cloud platform.

Running the project: 

1. Move to the project home directory. 
2. Run the machine learning model by running below command - python model.py. This would create a serialized version of our model into a file finalized_model.pkl
3. Run app.py using below command to start Flask API - python app.py
   By default, flask will run on port 5000.

4. Navigate to URL http://localhost:5000

Enter valid numerical values in input boxes and hit Predict. You will be able to see the predicted results in the web page

Link for accessing the model: https://salary-predict-api.herokuapp.com
