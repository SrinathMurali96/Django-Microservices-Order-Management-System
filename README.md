# Django based Microservices architecture for Order Management System

This is example web application based on microservices architecture. It has 3 decoupled and scalable services:

1. Order Management
2. Products Management
3. Email Sending

Technology Stack:
01. Python 
02. Django/Django REST Framework
03. Oracle


Python used as the backend development language. 
Django used as the backend framework. 
Django REST Framework or DRF used as the REST API development framework.
Oracle used as the database backend.

Each services have their seperate database completely decoupled. 

Each service deployed in each server.

For testing purpose,

1. Order Management - Started the server in the local system with Port 8001
2. Products Management - Started the server in the local system with Port 8002
3. Email Sending - Started the server  in the local system with Port 8003