# K8s Application Deployment Pipeline
## Overview
This readme file outlines an end-to-end CI/CD pipeline that automates the deployment of a Fastapi application connected to Mysql, running in a Kubernetes environment. The pipeline integrates Jenkins for continuous integration, Docker for containerization, Helm for package management and Argo CD for continuous deployment. 

Technologies Used: 
- Kubernetes: Container orchestration platform.
- Docker: Containerization technology.
- Fastapi: Python web framework.
- Mysql: SQL database.
- Jenkins: Automation server for continuous integration.
- Helm: Package manager for Kubernetes.
- Argo CD: Declarative GitOps continuous delivery tool.

Before starting this readme , make sure you have a A functional application and you have read the previous readme of how to check your app locally!!

The structure and essential files: (before adding pytest)
```
/payment_app/
├── app
│   └── backend
│       ├── paymentapp_server.py
│       ├── paymentapp.py
│       ├── PaymentObjects.py
│       └── validation.py
├── ConfigFiles
│   ├── ArgoCD
│   │   └── guestbook.yaml
│   ├── Helm
│   │   |── payment-app
│   │   └── payment-app-0.1.0.tgz
│   └── k8s-configuration
│       ├── connection-secret.yaml
│       └── deployment.yaml
├── agent.yaml
├── Dockerfile
├── jenkinsfile
├── README.md
└── requirements.txt
``` 
### Explanation of the File Structure
- app/backend: Contains the backend source code for the payment application.

  - paymentapp_server.py: Main server file to run the application.
  - paymentapp.py: Application logic.
  - PaymentObjects.py: Definitions for payment objects.
  - validation.py: Validation logic for the application.

- ConfigFiles: Contains configuration files for different tools and services.

  - ArgoCD: ArgoCD-specific configuration files.
    - guestbook.yaml: Example configuration file for ArgoCD.
  - Helm: Helm chart configuration for deploying the application.
    - payment-app: Directory containing Helm chart.
    - payment-app-0.1.0.tgz: Packaged Helm chart.
 - k8s-configuration: Kubernetes-specific configuration files.
   - connection-secret.yaml: Secret configuration for connections.
   - deployment.yaml: Deployment configuration for Kubernetes.
- agent.yaml: Configuration file for an agent, potentially for monitoring or sidecar containers.

- Dockerfile: Dockerfile to containerize the application.

- jenkinsfile: Jenkins pipeline configuration for CI/CD.

- README.md: Documentation file.

- requirements.txt: List of Python dependencies for the project.

### Create a Jenkins Agent
- Setup Jenkins Kubernetes Plugin: Configure the Jenkins Kubernetes plugin and docker plugin to manage Jenkins agents that run as pods within your Kubernetes cluster.

- Configure Pod Template: Define a pod template in Jenkins to specify the Docker image and necessary tools (like Docker and Helm) required for building and deploying your application. (this is a part of the jenkins file we will go over later in this readme)

### Create a Helm Chart for the Application (using gitbash)
- Initialize Helm Chart: Use helm create to generate a new chart template for your application, which will include Kubernetes deployment, service, and ingress resources. (in our exemple the name of the chart is "payment-app")
make sure you in the correct folder before doing this command:
```sh
$ helm create payment-app
```
- Customize Values: Edit the values.yaml file to define application-specific configurations like the image repository, tag, and other environment-specific settings. (you can see the adjusted files in the repository)

### Create a Helm package (using gitbash)
- To create a Helm package called payment-app and upload it to Docker Hub as an OCI artifact, follow these steps:
```
$ cd / your root folder (this case is ConfigFiles/Helm)

$ helm package payment-app

$ docker login --username <username> --password <password>

$ helm push payment-app-0.1.0.tgz oci://registry-1.docker.io/<username>

```
You can verify that the Helm chart has been pushed successfully by checking your Docker Hub repository.



### Step 3: Configuring ArgoCD to Use the OCI Helm Chart (Using the ArgoCD Web UI)
1. Add the Docker Hub Repository
    - Go to Settings -> Repositories -> Connect Repo.
    - Choose Helm as the repository type.
    - Name: the name of the repository
    - Project : defult
    - Repository URL: registry-1.docker.io/< username >
    - Enable OCI at the bottom of the page
    - User name and password - leave empty
    - Fill in your Docker Hub credentials.

2. Add the git Repository
   - Go to Settings -> Repositories -> Connect Repo.
   - Choose Git as the repository type.
   - Project: defult
   - Repository URL: < your git repository URL >
   - Username: < Git username >
   - password: < Git password >

![ArgoCD Repositoriest]()

2. Create the Application
    - Go to Applications and click New App
    - Application Name: root (whatever you want)
    - Project: default
    - sync policy Automatic (check the PRUNE RESOURCES and SELF HEAL)
    - SOURCE: 
        - Repository URL: < your git repository URL >
        - Path: the path to the to the ArgoCD configuration file (gusestbook.yaml)
    - DESTINATION:
        - Cluster URL - check the correct one
        - Namespace - the name space you want to deploy the app 

press create!! 

![ArgoCD Applications]()
![Guestbook Application]()
![Application Deployment]()



### Step 4: Automate Deployment Using Jenkins Pipeline

Pipeline Overview: The Jenkins pipeline automates the entire process of building and deploying the FastAPI application using a Jenkinsfile. It ensures that every code commit triggers a new build, updates Docker images, modifies Helm values, pushes the helm to docker hub and pushes changes to GitLab to facilitate automatic deployment by Argo CD.

### Jenkinsfile Breakdown:
1. Agent Configuration: This specifies that Jenkins should use a Kubernetes agent for running the pipeline. The kubernetes block defines:
    - label 'dind-agent': This is a selector for the Jenkins agent pods in Kubernetes, helping to assign jobs to the correct agent type.
    - yamlFile 'jenkins-agent.yaml': Points to a YAML file within the repository or Jenkins configuration that defines the pod template for the agent.

2. Environment Variables: Sets up various environment variables used throughout the pipeline:
    - DOCKER_IMAGE: Defines the Docker image name.
    - DOCKER_CREDENTIALS: ID for Docker credentials stored in Jenkins for Docker Hub authentication.
    - VERSION: Uses the Jenkins environment variable BUILD_NUMBER to tag Docker images, ensuring each build is unique.
    - GIT_CREDENTIALS: Specifies the ID for GitLab credentials stored in Jenkins, used for repository operations.
    - HELM_REGISTRY = 'oci://registry-1.docker.io/nadav0176' - Helm registry URL for pushing Helm charts.


3. Checkout Code: This stage checks out the source code from the SCM (Source Code Management) configured in the Jenkins job, which is typically a Git repository.

4. Build Docker Image: Constructs the Docker image using the specified repository and tag. The --no-cache option ensures that the build does not use any cached layers from previous builds, leading to a fresh build each time.

5. Push to DockerHub: After building the image, this stage logs into DockerHub using the credentials provided and pushes the newly built Docker image.

6. Update Helm Values: Update Helm Values: Updates the Docker image tag in the Helm chart's values.yaml file.

7. Push Changes to GitLab: Configures Git, checks out the main branch, commits the changes, and pushes them to the GitLab repository.

8. Helm Package & Push Helm Chart to DockerHub:
Packages the Helm chart into a tarball.
Pushes the Helm chart to the specified Helm registry.

dont forget to add the docker and gitlab credentials to jenkins !! 

## To summarize: 
The Jenkins job described successfully automates the entire workflow for deploying a FastAPI application onto a Kubernetes cluster using Docker, Helm, and Argo CD. The process starts with the Jenkins pipeline pulling the latest application code, building a new Docker image tagged with the build number, and pushing this image to Docker Hub.

After the build & push are successful, the pipeline updates the Helm chart's values.yaml file to reflect the new image version, ensuring that the Helm chart is always in sync with the latest Docker image. The Helm chart is then packaged and pushed to Docker Hub, making it available for deployment.

These changes, including the updated image tag and Helm chart, are committed and pushed back to the Git repository. Argo CD, which continuously monitors this repository, automatically detects and deploys the latest changes to the Kubernetes cluster.

The process ensures that the application is consistently and correctly deployed with the latest updates, reducing manual intervention and potential errors.



