# myDevOps-Minikube

Minikube Installation:
a.	Use a virtualization platform (e.g., VirtualBox) if not already installed. You can use your host OS if you have Docker Desktop Installed.

Intalled on local PC

b.	Install Minikube by following the official installation instructions for your operating system.

DONE.

c.	Verify the installation by running basic Minikube commands and checking the version.

![Alt text](image.png)

Deploying Applications:
a.	Create a custom Docker image for the application, which displays the pod name. (Use any repo from GitHub having a Docker File)
 
b.	Create three deployments using the custom Docker image.
c.	Verify the successful deployment of the pods.

Setting Up Services:
a.	Create a NodePort service to expose one of the deployments.
b.	Create a ClusterIP service to expose the second deployment.
c.	Create a LoadBalancer service to expose the third deployment.
d.	Verify the successful creation of the services.

Accessibility Demonstration:
a. Explain why pods are inaccessible outside the cluster when using the ClusterIP service. b. Demonstrate how pods are accessible within the cluster using the NodePort service. c. Demonstrate how pods are accessible from outside the cluster using the LoadBalancer service.

Documentation and Submission:
a.	Create a GitHub repository to host the YAML manifest files.
b.	Include a comprehensive README file with step-by-step instructions for setting up the Minikube cluster, deploying the applications, and demonstrating their accessibility.
c.	Commit and push the YAML manifest files and the README to the GitHub repository.
d.	Submit the link to the GitHub repository by the assignment deadline.

