# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API with FastAPI, define endpoints, validate request data, and return JSON responses from an in-memory application.

## 📝 Tasks

### 🛠️ Create the FastAPI application

#### Descrição
Set up a basic FastAPI project and define the API endpoints needed to manage a small collection of resources.

#### Requisitos
O programa concluído deve:

- Create a `FastAPI` application instance
- Define a `GET /items` endpoint that returns a list of items in JSON format
- Define a `GET /items/{item_id}` endpoint that returns a single item by ID
- Use an in-memory list or dictionary as temporary storage for the data
- Return a `404` response when an item is not found

### 🛠️ Add POST requests and validation

#### Descrição
Extend the API to allow creating new items and validate incoming data using Pydantic models.

#### Requisitos
O programa concluído deve:

- Define a `Item` model with fields such as `id`, `name`, `description`, `price`, and `available`
- Use the model to validate request payloads before creating a new item
- Add a `POST /items` endpoint that accepts JSON data and returns the created item
- Return a `201 Created` status for successful inserts
- Include clear validation for required fields and values
