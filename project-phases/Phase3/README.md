# Phase 3 : Start - Laying the Foundation

![Project Logo](https://github.com/JemyYousef/HiveBox-Scalable-RESTful-API-for-Beekeepers/blob/main/assets/Phase3.png)

- Define Goals : Clearly define your project goals .
- Prioritize Requirements : Prioritize the requirements for your project .
- Modularity : Focus on code modularity .
- Testing : Implement unit tests and follow Docker best practices .
- Continuous Integration : Explore quality gates in continuous integration with GitHub Actions .

## Running Project 

### Step 1 : Set Up Your Project Environment
    1. Create a Project Directory:
       # mkdir Phase3
       # cd Phase3  
### Step 2 : Running Your Application
    1. # python app.py
    2. Access Your Application : Open Your Browser
      - http://127.0.0.1:5000/version to see the version endpoint .
      - http://127.0.0.1:5000/temperature to see the temperature endpoint ( the data is no older 1 hour ) .
### Step 3 : Dockerizing the Application
    1. # docker build -t phase3:latest .
    2. # docker run --rm phase3:latest