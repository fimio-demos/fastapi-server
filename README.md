# Fimio Platform: FastAPI Hello World Demo

This repo shows how to use app.fimio.xyz to build and deploy a lightweight, high-performance FastAPI application.

Hello
Helosss
Hell iiiis

## Features

- Interactive Swagger UI documentation
- Simple "Hello World" endpoint
- Health check endpoint

## Production Deployment
- Go to [app.fimio.xyz](https://app.fimio.xyz/)
- Login with your GitHub identity
- Click the create project button
- Using the drop down button, switch to the `fimio-demos` organization, search for this repository `fastapi-server`
- Create the project,
    - Enter a project name
    - Optionally provide a description for the application you intend to build
    - Click on the `Advanced` button
    - Enter `fastapi run` in the Run Command slot
    - Use the dropdown to expose port 8000, which is needed to successfully build this application
    - Click `Make Build`
    - Provide a name for this version of the application you are building
    - Click `Start Build`
- Find the deployed version of the application on the Build report page, and at `https://app.fimio.xyz/<your github identity>/<fimio-generated-root>`


## API Documentation

Once the server is running, you can access:

- Swagger UI: `https://app.fimio.xyz/<your github identity>/<fimio-generated-root>/docs`
- ReDoc: `https://app.fimio.xyz/<your github identity>/<fimio-generated-root>/redoc`

## Endpoints

- `GET /`: Returns "Hello World" message
- `GET /health`: Health check endpoint