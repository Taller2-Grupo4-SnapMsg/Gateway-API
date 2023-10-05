# Gateway-API
API que esta en el medio del resto de las apis, y hace checkeos de verificacion y se encarga de no exponer endpoints que no se desean que sean publicos.

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
## Si no en cualquier commit de la CLI (Command Line Interface) te va a correr los hooks.
```bash
git commit
```
Acordate que sin el pythonpath te van a aparecer errores de importacion.

# Para poder conectar el gateway con los otros servicios, vas a tener que exportar las variables de entorno.
Por ejemplo, si quiero conectarme con users:
```bash
export USERS_URL=https://loginback-lg51.onrender.com$USERS_URL
```
Si te olvidaste, te va a tirar un error de este estilo:
```bash
requests.exceptions.MissingSchema: Invalid URL '/login_admin': No scheme supplied. Perhaps you meant https:///login_admin?
```

# Para correr el proyecto
(Con las variables de entorno exportadas)
```bash
bash run.sh
```
-> Esto va a correr el proyecto en el puerto `8080`