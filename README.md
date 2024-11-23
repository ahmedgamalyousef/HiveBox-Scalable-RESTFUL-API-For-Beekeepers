# RESTFUL-API for Beekeepers is Under Construction

# Step 1 : Set Up Your Project Environment
    1. Create a Project Directory:
       # mkdir hiveBox
       # cd hiveBox
    2. Create a Virtual Environment:
       # python3 -m venv env
       # source env/bin/activate   
# Step 2 : Install Dependencies
       # pip install -r requirements.txt
# Step 3 : Running Your Application
    1. # python app.py
    2. Access Your Application : Open your web browser and go to http://127.0.0.1:5000/version to see the version endpoint. You can also access the temperature endpoint at http://127.0.0.1:5000/temperature.
# Step 4 : Dockerizing the Application
    1. # docker build -t your-dockerhub-username/hivebox:latest .
    2. # docker run -p 5000:5000 your-dockerhub-username/hivebox:latest
# Step 5 : Push Docker Image to Docker Hub
    1. Log In to Docker Hub:
       # docker login
    2. Push the Docker Image to Docker Hub:
       # docker push your-dockerhub-username/hivebox:latest
