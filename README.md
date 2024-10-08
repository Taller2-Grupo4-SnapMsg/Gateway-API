# Gateway-API
API que esta en el medio del resto de las apis, y hace checkeos de verificacion y se encarga de no exponer endpoints que no se desean que sean publicos.

La arquitectura de microservicios es la siguiente:
![Arquitectura](Arquitectura_Microservicios.png)

El gateway se encarga de comunicar todos los procesos de la aplicacion, por lo cual es bastante importante, y por eso esta deployado en un cluster de kubernetes con tres replicas.

# Instrucciones Tecnicas:

# Pre-commit
```bash
export PYTHONPATH=.$PYTHONPATH
```
```bash
pre-commit install
```
## Para correrlo sin commitear:
```bash
pre-commit run --all-files
```
## Si no, en cualquier commit de la CLI (Command Line Interface) te va a correr los hooks.
```bash
git commit
```
Acordate que sin el pythonpath te van a aparecer errores de importacion.

# Para correr el proyecto
(Con las variables de entorno exportadas)
```bash
bash run.sh
```
-> Esto va a correr el proyecto en el puerto `8080`

# Para hacer un redeploy (Desde la compu de alejo al menos(?)):
Si no tenes el kubectl configurado, okteto te lo configura con:
```bash
okteto kubeconfig
```
Pusheas la nueva imagen a dockerhub:
```bash
docker build -t merok23/gateway-api:latest .
```
```bash
docker push merok23/gateway-api:latest
```
Le pones al k8s-deployment el nuevo nombre de tu imagen:
```yaml
      containers:
        - name: gateway-api
          image: merok23/gateway-api:lastest <- Esto
```
para el deploy:
```bash
kubectl apply -f k8s-deployment.yaml
```
para el service:
```bash
kubectl apply -f k8s-service.yaml
```