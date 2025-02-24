
# End-to-End Project : HiveBox 

![Project Logo](https://github.com/JemyYousef/HiveBox-Scalable-RESTful-API-for-Beekeepers/blob/main/assets/hivebox.jpg)

## 📊 Description
As a DevOps Engineer, I successfully led the HiveBox project, which involved building a scalable RESTFUL API around openSenseMap to assist Beekeepers with their chores . This project was part of the Dynamic DevOps Roadmap and covered various phases of the DevOps lifecycle .

## Prerequisites 
Before you begin, ensure you have met the following requirements:

- **Python**
- **AWS CLI**: Configured with appropriate permissions
- **Docker**: Installed and configured
- **kubectl**: Installed and configured to interact with your Kubernetes cluster
- **Terraform**
- **Helm**
- **GitHub CLI**

## Project Phases 

### [Phase 1 : Welcome to the DevOps World](https://github.com/JemyYousef/HiveBox-Scalable-RESTFUL-API-For-Beekeepers/tree/main/project-phases/Phase1)
    • Understand Your Role: Learn about your role in the project and how you'll collaborate with other teams .
    • Agile Methodology: Brush up on agile project management and decide which Agile methodology you'll use (e.g., Scrum, Kanban) .
    • Documentation: Document your progress and decisions as you go .
### [Phase 2 : Basics - DevOps Core](https://github.com/JemyYousef/HiveBox-Scalable-RESTFUL-API-For-Beekeepers/tree/main/project-phases/Phase2)
    • Python Fundamentals: Learn Python basics .
    • Development Tools: Familiarize yourself with common development tools .
    • Git Basics: Get comfortable with Git for version control .
    • Linux Essentials: Gain essential Linux skills and learn common tools .
    • Bash Scripting: Practice writing bash scripts .
    • Docker Fundamentals: Understand the basics of Docker .
### [Phase 3 : Start - Laying the Foundation](https://github.com/JemyYousef/HiveBox-Scalable-RESTFUL-API-For-Beekeepers/tree/main/project-phases/Phase3)
    • Define Goals: Clearly define your project goals .
    • Prioritize Requirements: Prioritize the requirements for your project .
    • Modularity: Focus on code modularity .
    • Testing: Implement unit tests and follow Docker best practices .
    • Continuous Integration: Explore quality gates in continuous integration with GitHub Actions .
### [Phase 4 : Expand - Constructing a Shell](https://github.com/JemyYousef/HiveBox-Scalable-RESTFUL-API-For-Beekeepers/tree/main/project-phases/Phase4)
    • Planning: Review and refine your planning .
    • REST API Best Practices: Apply REST API best practices .
    • Kubernetes: Embrace Kubernetes for container orchestration .
    • Observability: Dive into observability .
    • Continuous Delivery: Explore continuous delivery solutions .
    • Cloud Computing: Get an overview of cloud computing .
### [Phase 5 : Transform - Finishing the Structure](https://github.com/JemyYousef/HiveBox-Scalable-RESTFUL-API-For-Beekeepers/tree/main/project-phases/Phase5)
    • Integration: Integrate your code with external systems .
    • Integration Tests: Write integration tests .
    • Infrastructure as Code: Learn Terraform essentials and Kubernetes configuration management (Helm) .
    • Continuous Delivery Best Practices: Implement CD best practices .
### [Phase 6 : Optimize - Keep Improving](https://github.com/JemyYousef/HiveBox-Scalable-RESTFUL-API-For-Beekeepers/tree/main/project-phases/Phase6)
    • Deploy the Application in Declarative GitOps Style Using Argo CD .
    • Prepare for Production by Setting Up DNS (ExternalDNS) and Certificates (Cert-Manager) .
    • Automate Dependency Updates with Dependabot .
    • Move All External Services to Kubernetes Cluster Using Open-Source Solutions .

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
    2. Open Your Terminal to run the Minio Server using the following Command :
       # docker run -p 9000:9000 -p 9001:9001   --name minio   -e "MINIO_ROOT_USER=minioadmin"   -e "MINIO_ROOT_PASSWORD=minioadmin"   -v /media/jemy/Data/Linux\ Adminstration/Github\ Projects/saraya-project/miniodata/   minio/minio server /data
    2. Access Your Application : Open Your Browser
      - http://127.0.0.1:5000/version to see the version endpoint .
      - http://127.0.0.1:5000/temperature to see the temperature endpoint .
      - http://127.0.0.1:5000/metrics to returns default Prometheus metrics about the app .
      - http://127.0.0.1:5000/readyz to return HTTP 200 unless 50% + 1 of the configured senseBoxes are not accessible and caching content is older than 5 min .
      - http://127.0.0.1:5000/store to make the application store the data every 5 minutes, but by calling this endpoint, it should store the data directly on MinIO .
      - http://172.17.0.2:40047/login to open Minio WebUI, create abucket and its name as written in code (mybucket) and show your stored Data ( Usename: minioadmin & Password: minioadmin ) .
     
### Step 4 : Dockerizing the Application
    1. # docker build -t your-dockerhub-username/hiveBox-scalable-restful-api-for-beekeepers:latest .
    2. # docker run -p 5000:5000 your-dockerhub-username/hiveBox-scalable-restful-api-for-beekeepers:latest
### Step 5 : Push Docker Image to Docker Hub
    1. Log In to Docker Hub:
       # docker login
    2. Push the Docker Image to Docker Hub:
       # docker push your-dockerhub-username/hiveBox-scalable-restful-api-for-beekeepers:latest

## Project EndPoints Outputs
![Project Logo](https://github.com/JemyYousef/HiveBox-Scalable-RESTful-API-for-Beekeepers/blob/main/assets/1.png)
![Project Logo](https://github.com/JemyYousef/HiveBox-Scalable-RESTful-API-for-Beekeepers/blob/main/assets/2.png)
![Project Logo](https://github.com/JemyYousef/HiveBox-Scalable-RESTful-API-for-Beekeepers/blob/main/assets/3.png)
![Project Logo](https://github.com/JemyYousef/HiveBox-Scalable-RESTful-API-for-Beekeepers/blob/main/assets/4.png)
![Project Logo](https://github.com/JemyYousef/HiveBox-Scalable-RESTful-API-for-Beekeepers/blob/main/assets/5.png)
![Project Logo](https://github.com/JemyYousef/HiveBox-Scalable-RESTful-API-for-Beekeepers/blob/main/assets/6.png)
![Project Logo](https://github.com/JemyYousef/HiveBox-Scalable-RESTful-API-for-Beekeepers/blob/main/assets/7.png)
![Project Logo](https://github.com/JemyYousef/HiveBox-Scalable-RESTful-API-for-Beekeepers/blob/main/assets/8.png)
![Project Logo](https://github.com/JemyYousef/HiveBox-Scalable-RESTful-API-for-Beekeepers/blob/main/assets/9.png)
![Project Logo](https://github.com/JemyYousef/HiveBox-Scalable-RESTful-API-for-Beekeepers/blob/main/assets/10.png)