# api-demo-frontend

[![Build](https://github.com/Arcanexus/api-demo-frontend/actions/workflows/azure-container-webapp.yml/badge.svg)](https://github.com/Arcanexus/api-demo-frontend/actions/workflows/azure-container-webapp.yml)

## Summary
A simple set of Python scripts simulating a fake CRUD based API.

## Frontend webapp
The frontend is a Flask webapp.

### Manual
To run the webapp :
1. (Optional) Create a Venv
2. Install prerequisites from **requirements.txt**
3. Run ```python app.py```
4. Browse [localhost:5000](http://localhost:5000) (change the URL depending on where you deployed the webapp)

### Docker
To run the webapp, launch the following command:
```
 docker run -d -p80:80 -name api-demo-frontend ghcr.io/arcanexus/api-demo-frontend:latest
 ```

