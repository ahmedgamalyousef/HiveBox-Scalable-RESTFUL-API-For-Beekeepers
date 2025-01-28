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
    2. Install Docker & Kind & Kubectl

### Step 2 : Create KIND Cluster
       # kind create cluster --config clustername.yaml

### Step 3 : Prepare Deployment and Service files
    1. Create Deployment File ( Deployment.yaml )
    2. Create Service File ( Service.yaml )

### Step 4 : Apply Deployment and Service
    1. Apply Deployment and Service files
       # kubectl apply -f deployment.yaml
       # kubectl apply -f service.yaml
    2. verify Deployment
       # kubectl get deployments
       # kubectl get pods
    3. Verify Service
       # kubectl get services
       # kubectl describre service 

### Step 5 : Running and Accessing Your Application
    1. # export 
    1. # python Phase4.py
    2. Access Your Application : Open Your Browser
      - http://127.0.0.1:5000/version to see the version endpoint .
      - http://127.0.0.1:5000/temperature to see the temperature endpoint ( < 10 : Too Cold , Between 11-36 : Good , > 37 : Too Hot ) .
      - http://127.0.0.1:5000/metrics to returns default Prometheus metrics about the app .

### Step 6 : Dockerizing the Application
    1. # docker build -t phase4:latest .
    2. # docker run --rm phase4:latest