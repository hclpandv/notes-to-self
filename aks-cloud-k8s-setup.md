# How to setup aks cluster

```
# Command to get the cluster cred and cache into local kubeconfig
az aks get-credentials --resource-group rg-eas-d-auto-poc01 --name aks-eas-d-poc01-oolklkl
OUTPUT: `Merged "aks-eas-d-poc01-oolklkl" as current context in /home/clouduser/.kube/config`

# Use kubectl to list pods
kubectl get po -A
OUTPUT: `To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code HVMYVFZTX to authenticate.`
 
```
