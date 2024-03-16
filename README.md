# Todo project using Django Rest Framework

This is a simple todo app made with RESTful APIs using django framework

## Getting Started

To get started with TweeterSphere, follow the instructions below:


### Installation

1. Clone the repository:

```
git clone https://github.com/Rhythm1821/Django-todo-project/
```


2. Navigate to the project directory:

```
cd Django-todo-project
```


3. Create a virtual environment:

```
python3 -m venv venv
```


4. Activate the virtual environment:

```
source venv/bin/activate
```


5. Install dependencies:

```
pip install -r requirements.txt
```


### Database Setup

6. Run database migrations:

```
python3 manage.py migrate
```


### Running the Server

7. Start the development server:

```
python3 manage.py runserver
```

You can now access TweeterSphere at http://127.0.0.1:8000/ in your web browser.


### Installation (with docker)

Add your credentials to .env file

1. Clone the repository:

```
git clone https://github.com/Rhythm1821/Django-todo-project/
```


2. Navigate to the project directory:

```
cd Django-todo-project/
```

3. Ensure no container is running:

```
docker ps #(if running do "docker kill {container_id}")
```

### Build the container

4. Start building the container:

```
docker compose up --build
```

You can now access TweeterSphere at http://127.0.0.1:8000/ in your web browser.
