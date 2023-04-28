# Microservice communication with RabbitMQ

Project by: Kanumuri Sri Charan, Keerthana Shivakumar, Keerthi R and Mahika Gupta

## Problem Statement

Building and deploying a microservices architecture where multiple components communicate with each other using RabbitMQ. A message broker is an architectural pattern for message validation, transformation and routing. For the scope of this project, we will build 4 microservices: A HTTP server that handles incoming requests to perform CRUD operations on a Student Management Database + Check the health of the RabbitMQ connection, a microservice that acts as the health check endpoint, a microservice that inserts a single student record, a microservice that retrieves student records, a microservice that deletes a student record given the SRN.

## File Structure 

```bash
├── <microservices-project-directory>
    ├── docker-compose.yml
    ├── producer
    │   ├── producer.py
    │   ├── Dockerfile
        └──requirements.txt
    ├── consumer_one
    │   ├── healthcheck.py
    │   ├── Dockerfile
    │   └──requirements.txt
    ├── consumer_two
    │   ├── insertion.py
    │   ├── Dockerfile
    │   └──requirements.txt
    ├── consumer_three
    │   ├── deletion.py
    │   ├── Dockerfile
    │   └──requirements.txt
    └── consumer_four
        ├── read.py
        ├── Dockerfile
        └──requirements.txt

```
### Instructions to run the project
1. Clone the repository or download the zip file.
2. Navigate to the project directory and open a terminal.
3. Run the follwing command to build the containers.<br>
    ```docker-compose build```
4. Run the following command to run the containers.<br>
    ```docker-compose up```
5. Open a new terminal and run the following command to check the health of the RabbitMQ connection.<br>
    ```curl http://localhost:5000/healthcheck```
6. Open a new terminal and run the following command to insert a student record.<br>
    ```curl -X POST http://localhost:5000/insert_record/SRN/NAME/SEC```
7. Open a new terminal and run the following command to read all the records.<br>
    ```curl http://localhost:5000/read_database```
8. Open a new terminal and run the following command to delete a student record.<br>
    ```curl -X DELETE http://localhost:5000/delete_record/SRN```
9. To stop the containers, run the following command.<br>
    ```docker-compose down```

