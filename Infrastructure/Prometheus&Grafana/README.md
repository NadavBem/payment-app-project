# Prometheus & Grafana solutions establishment
## Prometheus:
### Add the Prometheus Helm Repository
If you haven't already added the Prometheus Helm repository, you can do so with the following commands:
```sh
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
```
```sh
helm repo update
```
### Installing Prometheus:
To install Prometheus in a custom namespace using Helm, you need to create the namespace first and then specify it during the Helm installation. Below are the adjusted commands to achieve this.

First, we need to install Prometheus in a custom namespace using the following command:
```sh
helm upgrade --install prometheus prometheus-community/prometheus --namespace monitoring --create-namespace
```
It will install all the required components of the Prometheus system with a single command. Without Helm Charts we would have to write the manifest file ourselves

### Access Prometheus 
Access Prometheus using a web browser like Chrome, you need to expose the Prometheus service. Here are the steps to do that:

First, check the Prometheus service to understand how it's configured. Run the following command and look for the Prometheus service in the output:
```sh
kubectl get svc -n monitoring
```
Now we can expose the prometheus-server service to the internet using nodeport by using the following command: 
```sh
kubectl expose service -n monitoring prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-ext
```
check the Prometheus service , you should see the 'prometheus-server-ext' added
```sh
kubectl get svc -n monitoring 
```
image: ""

Once the nodeport is set up, open your web browser (Chrome) and navigate to:
```sh
http://localhost:32187
```
## Grfana:
### Installing Grafana
To install Grafana in the monitoring namespace on Kubernetes, you can use Helm, which simplifies the deployment process and manages dependencies.

Run the following command:
```sh
helm repo add grafana https://grafana.github.io/helm-charts

helm repo update

helm upgrade --install grafana grafana/grafana --namespace monitoring
```
### Access Grafana

By default, Grafana is exposed as a ClusterIP service within the monitoring namespace.

To access Grafana’s web interface, you can set up port forwarding or expose it externally using a NodePort or LoadBalancer service.
```sh
kubectl expose service -n monitoring grafana --type=NodePort --target-port=3000 --name=grafana-ext
```
image: ""

Once the nodeport is set up, open your web browser (Chrome) and navigate to:
```
http://localhost:32134
```
### Log in to Grafana:
To get the Grafana username and password we have to access the secrets of that namespace by using the following command:  
```sh
kubectl get secret --namespace monitoring grafana -o yaml
```
```sh
echo “admin-password-value” | openssl base64 -d ; echo

echo “admin-user-value” | openssl base64 -d ; echo
```
