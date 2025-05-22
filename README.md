# Title of Project: Skin Disease Detection Using Deep Learning.

## Team Members:
1. Abhishek Singh
2. Adarsh Pathak
3. Aditya Kumar

## Steps for Execution:
Step 1 Setup for Python:
          Install Python 
          Install Python packages
              pip3 install -r training/requirements.txt
              pip3 install -r api/requirements.txt
              Install Tensorflow Serving (Setup instructions)
Step 2  Setup for ReactJS
          Install Nodejs (Setup instructions)
          Install NPM (Setup instructions)
          Install dependencies
              cd frontend
              npm install --from-lock-json
              npm audit fix
              Copy .env.example as .env.
              Change API url in .env.

Step 3  Training the Model
           Download the data from kaggle.
           Only keep folders related to Potatoes.
           Run Jupyter Notebook in Browser.
           Open training/Skin-disease-training.ipynb in Jupyter Notebook.
       In cell #2, update the path to dataset.
           Run all the Cells one by one.
           Copy the model generated and save it with the version number in the models folder.
Step 4   Running the API
           Using FastAPI
           Get inside api folder
           cd api
           Run the FastAPI Server using uvicorn
           uvicorn main:app --reload --host 0.0.0.0
           Your API is now running at 0.0.0.0:8000
Step 5    Get inside api folder
             cd frontend
             Copy the .env.example as .env and update REACT_APP_API_URL to API URL if needed.
             Run the frontend
             npm run start
              
## Checklist:
1. Final Project Report
2. Certificate VII Semester (Dated: December 2024).
3. Certificate VIII Semester (Dated: May 2025).
4. Synopsis
5. Final Presentation
6. Source Code
7. Database dump (.sql file)
8. If a web project, then a Docker file for deployment
9. README (This file)
