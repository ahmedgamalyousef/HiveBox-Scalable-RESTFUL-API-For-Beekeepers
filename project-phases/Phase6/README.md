# Phase 6 : Optimize - Keep Improving

![Project Logo](https://github.com/JemyYousef/HiveBox-Scalable-RESTful-API-for-Beekeepers/blob/main/assets/Phase6.png)

- Deploy the Application in Declarative GitOps Style Using Argo CD : Utilize Argo CD to manage application deployments in a declarative manner, ensuring consistency and reliability .
- Prepare for Production by Setting Up DNS (ExternalDNS) and Certificates (Cert-Manager) : Configure DNS using ExternalDNS and manage SSL/TLS certificates with Cert-Manager to prepare the application for a production environment .
- Automate Dependency Updates with Dependabot : Use Dependabot to automate the process of keeping dependencies up-to-date, enhancing security and stability .
- Move All External Services to Kubernetes Cluster Using Open-Source Solutions : Integrate external services, like Grafana.comand Terraform Cloud, into the Kubernetes cluster using open-source tools, promoting a cohesive and manageable infrastructure .


## Requirements in this Phase : 

### 1-Deploy the Application in Declarative GitOps Style using Argo CD

    1. Install Argo CD :
       # kubectl create namespace argocd
       # kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

    2. Access Argo CD UI :
       # kubectl port-forward svc/argocd-server -n argocd 8081:443
    Access the Argo CD UI at https://localhost:8081

    3. Login to Argo CD :
       # kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
    
    4. Create Argo CD Application :
       Define an Argo CD Application manifest ( application.yaml )
    
    5. Apply the Argo CD Application :
       # kubectl apply -f application.yaml

### 2-Prepare for Production by Setting Up DNS (ExternalDNS) and Certificates (Cert-Manager)
      - ExternalDNS manages DNS records for your Kubernetes cluster . Cert-Manager automates the creation and management of certificates .
    
    1. Install ExternalDNS & Deploy ExternalDNS-deployment.yaml File:
       # kubectl create namespace externaldns
       # kubectl apply -f externaldna-deployment.yaml

    2. Install Cert-Manager & Create a ClusterIssuer for Let's Encrypt File (clusterissuer.yaml) :
       # kubectl create namespace cert-manager
       # kubectl apply -f https://github.com/jetstack/cert-manager/releases/download/v1.6.1/cert-manager.yaml
       # kubectl apply -f clusterissuer.yaml

### 3-Automate Dependancy Updates with Dependabot
      - Dependabot automatically checks for and updates dependencies in your project 
      - Create Dependabot Configuration File (Create a .github/dependabot.yaml file in your Repository)

### 4-Move All External Services to Kubernetes Cluster Using Open-Source Solutions
    1. Grafana :
       - Create a deployment for Grafana (grafana-deployment.yaml)
       - Create a service for Grafana (grafana-service.yaml)
       - Apply the Grafana mainfests :
         # kubectl apply -f grafana-deployment.yaml
         # kubectl apply -f grafana-service.yaml

    2. Prometheus :
       - Create a deployment for Prometheus (prometheus-deployment.yaml)
       - Create a service for Prometheus (prometheus-deployment.yaml)
       - Apply the Prometheus mainfests :
         # kubectl apply -f prometheus-deployment.yaml
         # kubectl apply -f prometheus-service.yaml

    2. Terraform Cloud Equivalent (e.g., Terraformer) :
       - Deploy Terraformer in your cluster (terraformer-deployment.yaml)
       - Apply the Terraformer manifests :
         # kubectl apply -f terraformer-deployment.yaml

### 5-Extra Suggestions
    1. Setup Kyverno for Policy as Code
       - Kyverno is a Kubernetes native policy management tool .
       - Install Kyverno :
         # kubectl create -f https://raw.githubusercontent.com/kyverno/kyverno/main/definitions/release/install.yaml
        - Create a Policy (kyverno-policy.yaml)
        - Apply the Policy :
          # kubectl apply -f kyverno-policy.yaml
    2. Build Multi-environment Kubernetes Clusters with Terraform and Kustomize
       - Terraform Configuration 
       - Kustomize Configuration

    3. Use TestKube for Better Testing Execution
       - Install TestKube :
         # kubectl apply -f https://github.com/kubeshop/testkube/releases/download/v1.0.0/testkube-operator.yaml
       - Create a Test: Create a test definition file (testkube-test.yaml)
       - Apply the Test :
         # kubectl apply -f testkube-test.yaml
       - Execute The Test :
         # kubectl testkube run test <<name you entered inside the Test file>>

    4. Develop a Kubernetes Operator to Handle the App Operations
       Kubernetes Operators simplify the management of complex applications on Kubernetes by extending the Kubernetes API .
       - Install Operator SDK :
         # curl -Lo /usr/local/bin/operator-sdk https://github.com/operator-framework/operator-sdk/releases/download/v1.16.0/operator-sdk_linux_amd64
         # chmod +x /usr/local/bin/operator-sdk
       - Create a New Operator Project :
         # operator-sdk init --domain hivebox.io --repo github.com/YourUsername/hivebox-operator
       - Create a Custom Resource Definition (CRD) :
         # operator-sdk create api --group hivebox --version v1 --kind Hive
       - Define the CRD (api/v1/hive_types.go) 
       - Implement the Controller Logic (controllers/hive_controller.go)  
       - Deploy the Operator :
         # make insall
         # make deploy







