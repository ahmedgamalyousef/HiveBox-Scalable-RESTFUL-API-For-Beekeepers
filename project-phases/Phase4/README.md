# Phase 4 : Expand - Constructing a Shell

![Project Logo](https://github.com/JemyYousef/HiveBox-Scalable-RESTful-API-for-Beekeepers/blob/main/assets/Phase4.png)

- Planning : Review and refine your planning .
- REST API Best Practices : Apply REST API best practices .
- Kubernetes : Embrace Kubernetes for container orchestration .
- Observability : Dive into observability .
- Continuous Delivery : Explore continuous delivery solutions .
- Cloud Computing : Get an overview of cloud computing .

## Running Project 

### Step 1 : Set Up Your Project Environment
    1. Create a Project Directory:
       # mkdir Phase4
       # cd Phase4  
### Step 2 : Running Your Application
    1. # python app.py
    2. Access Your Application : Open Your Browser
      - http://127.0.0.1:5000/version to see the version endpoint .
      - http://127.0.0.1:5000/temperature to see the temperature endpoint ( < 10 : Too Cold , Between 11-36 : Good , > 37 : Too Hot  .
      - http://127.0.0.1:5000/metrics to returns default Prometheus metrics about the app .

### Step 3 : Dockerizing the Application
    1. # docker build -t phase4:latest .
    2. # docker run --rm phase4:latest