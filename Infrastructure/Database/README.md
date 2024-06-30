# MySQL Deployment on Kubernetes

This guide will show you how to deploy a MySQL pod on a Kubernetes cluster using two files: a deployment file and a secrets file.

## What You Need

- A Kubernetes cluster running
- `kubectl` tool installed and set up to talk to your cluster

## Steps to Deploy

### 1. Create a Namespace (Optional)
You can create a special space (namespace) for your database. If you don't want to, you can skip this step.
```sh
kubectl create namespace database
```
### 2. Create the Secrets file
The secrets file (mysql-secret.yaml) has important details like the database password. We don't want to put these in the deployment file, so we keep them secret.
to create a best practise secrets can you use this command:
```sh
echo -n <'your value'> | base64
```
and then let deploy our secret file by the following command:
```sh
kubectl apply -f mysql-secret.yaml -n database
```

### 3. Deploy MySQL
Now, use the deployment file to set up MySQL with a LoadBalancer service.
```sh
kubectl apply -f deployment.yaml -n database
```

### 4. Check Everything
Make sure the deployment and service are running correctly.
```sh
kubectl get deployments -n database
kubectl get services -n database
kubectl get pods -n database
```

### Done!
You now have a MySQL pod running on your Kubernetes cluster with the sensitive info kept safe. Make sure to keep your secrets file private and not share it publicly.