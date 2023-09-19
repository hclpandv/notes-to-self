
```bash
# Download okteto
curl https://get.okteto.com -sSfL | sh

# valiate installation success
okteto version && kubectl version

# Download and set env variable for okteto cred. Download from settings tab in the ui.
export KUBECONFIG=$HOME/Downloads/okteto-kube.config:${KUBECONFIG:-$HOME/.kube/config}

# Create deployment
kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1

# Proxy :(
echo -e "Starting Proxy. After starting it will not output a response. Please return to your original terminal window\n"; kubectl proxy

# Running pod name
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME

# Nodeport :(
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080

# Get all services
kubectl get services

# Describe
kubectl describe services/kubernetes-bootcamp

# Scale
kubectl scale deployments/kubernetes-bootcamp --replicas=1

# Interact with running pod
kubectl exec -it $POD_NAME -- bash
kubectl exec -ti $POD_NAME -- curl localhost:8080



```
