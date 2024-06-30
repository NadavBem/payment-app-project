# Kubernetes cluster establishment
Running Kubernetes from Docker Desktop is a straightforward process, as Docker Desktop includes a built-in Kubernetes cluster that can be enabled. Here's a step-by-step guide on how to set it up on windows:
## Install Docker Desktop
If you haven't installed Docker Desktop yet, download and install it from the Docker official website.

## Enable Kubernetes in Docker Desktop
- Open Docker Desktop: Launch the Docker Desktop application on your computer.
Access Settings - Click on the Docker icon in the system tray, then click on the gear icon (Settings).

- Enable Kubernetes:
In the Settings/Preferences window, navigate to the Kubernetes tab.
Check the box labeled "Enable Kubernetes".

- Click "Apply & Restart" to enable Kubernetes and restart Docker Desktop.

![docker-cluster](https://github.com/NadavBem/payment-app-project/blob/main/Infrastructure/Kubernetes/docker-cluster.png?raw=true)

## Verify Kubernetes Installation
Check Kubernetes Status:
After Docker Desktop restarts, open a terminal or command prompt.
Run the following command on powershell to check the status of Kubernetes:
```
kubectl cluster-info
```
You should see output indicating that Kubernetes is running.

## Clean up
Once you're done experimenting with Kubernetes on Docker Desktop, you may want to clean up resources:

- Disable Kubernetes:

    Open Docker Desktop.
Navigate to Settings → Kubernetes.
Uncheck "Enable Kubernetes" and click "Apply & Restart".

- Clean Up Kubernetes Resources (Optional):
If you want to remove Kubernetes resources (namespaces, deployments, services) that you created during testing:
Use kubectl delete commands to delete resources.
Example:
```sh
kubectl delete namespace <namespace-name>
```
Replace <namespace-name> with the name of the Kubernetes namespace you want to delete.

This clean-up process ensures that your system is tidy and free of unnecessary Kubernetes resources and Docker Desktop installations.
