# Title of Project: Skin Disease Detection Using Deep Learning.

## Team Members:
1. Abhishek Singh
2. Adarsh Pathak
3. Aditya Kumar

## Steps for Execution:
Step 1 Setup for Python:<br /> 
          &emsp;Install Python <br /> 
          &emsp;Install Python packages<br /> 
              &emsp;pip3 install -r training/requirements.txt<br /> 
              &emsp;pip3 install -r api/requirements.txt<br /> 
              &emsp;Install Tensorflow Serving (Setup instructions)<br /> 
Step 2  Setup for ReactJS<br /> 
          &emsp;Install Nodejs <br /> 
          &emsp;Install NPM <br /> 
          &emsp;Install dependencies<br /> 
           &emsp;   cd frontend<br /> 
           &emsp;   npm install --from-lock-json<br /> 
            &emsp;  npm audit fix<br /> 
            &emsp;  Copy .env.example as .env.<br /> 
            &emsp;  Change API url in .env.<br /> 

Step 3  Training the Model<br /> 
           &emsp;Download the data from kaggle.<br /> 
           &emsp;Only keep folders related to Potatoes.<br /> 
          &emsp; Run Jupyter Notebook in Browser.<br /> 
          &emsp; Open training/Skin-disease-training.ipynb in Jupyter Notebook.<br /> 
       &emsp;In cell #2, update the path to dataset.<br /> 
          &emsp; Run all the Cells one by one.<br /> 
           &emsp;Copy the model generated and save it with the version number in the models folder.<br /> 
Step 4   Running the API<br /> 
          &emsp; Using FastAPI<br /> 
           &emsp;Get inside api folder<br /> 
           &emsp;cd api<br /> 
           &emsp;Run the FastAPI Server using uvicorn<br /> 
         &emsp;  uvicorn main:app --reload --host 0.0.0.0<br /> 
           &emsp;Your API is now running at 0.0.0.0:8000<br /> 
Step 5    Get inside api folder<br /> 
             &emsp;cd frontend<br /> 
             &emsp;Copy the .env.example as .env and update REACT_APP_API_URL to API URL if needed.<br /> 
             &emsp;Run the frontend<br /> 
            &emsp; npm run start<br /> 
              
## Checklist:
1. Final Project Report
2. Certificate VII Semester (Dated: December 2024).
3. Certificate VIII Semester (Dated: May 2025).
4. Synopsis
5. Final Presentation
6. Source Code
7. README (This file)
