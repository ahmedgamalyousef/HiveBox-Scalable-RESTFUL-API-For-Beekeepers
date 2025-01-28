# Phase 5 : Transform - Finishing the Structure

![Project Logo](https://github.com/JemyYousef/HiveBox-Scalable-RESTful-API-for-Beekeepers/blob/main/assets/Phase5.png)

- Integration: Integrate your code with external systems .
- Integration Tests: Write integration tests .
- Infrastructure as Code: Learn Terraform essentials and Kubernetes configuration management (Helm) .
- Continuous Delivery Best Practices: Implement CD best practices .

## Running Project 

### Step 1 : Set Up Your Project Environment
    1. Create a Project Directory:
       # mkdir Phase5
       # cd Phase5  
    2. Install Docker & Kind & Kubectl & Redis & Minio

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
    1. # python Phase5.py
    2. Access Your Application : Open Your Browser
      - http://127.0.0.1:5000/version to see the version endpoint .
      - http://127.0.0.1:5000/temperature to see the temperature endpoint ( < 10 : Too Cold , Between 11-36 : Good , > 37 : Too Hot ) .
      - http://127.0.0.1:5000/metrics to returns default Prometheus metrics about the app .
      - http://127.0.0.1:5000/readyz to ensures the application is ready to handle traffic .
      - http://127.0.0.1:5000/store to triggers immediate storage of data in MinIO, by passing the 5 minute interval .

### Step 6 : Dockerizing the Application
    1. # docker build -t phase5:latest .
    2. # docker run --rm phase5:latest