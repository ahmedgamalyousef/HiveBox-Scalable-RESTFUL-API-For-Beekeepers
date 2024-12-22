
# End-to-End Project : HiveBox ( Under Construction )

![Project Logo](https://github.com/JemyYousef/HiveBox-Scalable-RESTful-API-for-Beekeepers/blob/main/assets/hivebox.jpg)

## Description
As a DevOps Engineer, I successfully led the HiveBox project, which involved building a scalable RESTful API around openSenseMap to assist beekeepers with their chores . This project was part of the Dynamic DevOps Roadmap and covered various phases of the DevOps lifecycle .

## Project Phases 

### Phase 1 : Welcome to the DevOps World
    • Understand Your Role: Learn about your role in the project and how you'll collaborate with other teams .
    • Agile Methodology: Brush up on agile project management and decide which Agile methodology you'll use .
    • Documentation: Document your progress and decisions as you go .
### Phase 2 : Basics - DevOps Core
    • Python Fundamentals: Learn Python basics .
    • Development Tools: Familiarize yourself with common development tools .
    • Git Basics: Get comfortable with Git for version control .
    • Linux Essentials: Gain essential Linux skills and learn common tools .
    • Bash Scripting: Practice writing bash scripts .
    • Docker Fundamentals: Understand the basics of Docker .
### Phase 3 : Start - Laying the Foundation
    • Define Goals: Clearly define your project goals .
    • Prioritize Requirements: Prioritize the requirements for your project .
    • Modularity: Focus on code modularity .
    • Testing: Implement unit tests and follow Docker best practices .
    • Continuous Integration: Explore quality gates in continuous integration with GitHub Actions .
### Phase 4 : Expand - Constructing a Shell
    • Planning: Review and refine your planning .
    • REST API Best Practices: Apply REST API best practices .
    • Kubernetes: Embrace Kubernetes for container orchestration .
    • Observability: Dive into observability .
    • Continuous Delivery: Explore continuous delivery solutions .
    • Cloud Computing: Get an overview of cloud computing .
### Phase 5 : Transform - Finishing the Structure
    • Integration: Integrate your code with external systems .
    • Integration Tests: Write integration tests .
    • Infrastructure as Code: Learn Terraform essentials and Kubernetes configuration management (Helm) .
    • Continuous Delivery Best Practices: Implement CD best practices .

### Summary

Each phase builds on the previous one, gradually covering all aspects of the DevOps lifecycle, from planning and coding to testing, continuous integration, continuous delivery and infrastructure . The goal is to learn industry best practices while implementing a real system .

## Running Project 

### Step 1 : Set Up Your Project Environment
    1. Create a Project Directory:
       # mkdir hiveBox
       # cd hiveBox
    2. Create a Virtual Environment:
       # python3 -m venv env
       # source env/bin/activate   
### Step 2 : Install Dependencies
       # pip install -r requirements.txt
### Step 3 : Running Your Application
    1. # python app.py
    2. Access Your Application : Open Your Browser
      - http://127.0.0.1:5000/version to see the version endpoint .
      - http://127.0.0.1:5000/temperature to see the temperature endpoint .
      - http://127.0.0.1:5000/metrics to returns default Prometheus metrics about the app .
      - http://127.0.0.1:5000/readyz to return HTTP 200 unless 50% + 1 of the configured senseBoxes are not accessible and caching content is older than 5 min .
      - http://127.0.0.1:5000/store to make the application store the data every 5 minutes, but by calling this endpoint, it should store the data directly on MinIO .      
### Step 4 : Dockerizing the Application
    1. # docker build -t your-dockerhub-username/hiveBox-scalable-sESTful-api-for-beekeepers:latest .
    2. # docker run -p 5000:5000 your-dockerhub-username/hiveBox-scalable-sESTful-api-for-beekeepers:latest
### Step 5 : Push Docker Image to Docker Hub
    1. Log In to Docker Hub:
       # docker login
    2. Push the Docker Image to Docker Hub:
       # docker push your-dockerhub-username/hiveBox-scalable-sESTful-api-for-beekeepers:latest