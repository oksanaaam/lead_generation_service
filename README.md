# Lead Generation Interface
This project aims to develop a web interface for a lead generation service using the Django framework.  
The interface allows users to generate leads by specifying keywords, location, and the desired number of leads.  
The project includes log-in and sign-up functionality, with user authentication and registration stored in a PostgreSQL database.

## Features
Log-in: Users can log in to access the lead generation functionality.  
Sign-up: New users can register by providing their email, username, and password.  
Lead Generator: Registered users can enter keywords, location, and the number of leads they want to generate.  
Navigation: The interface includes a navigation bar with links to all pages.  
Responsive Design: The website is designed to be responsive and accessible across different devices.  


### Installation

1. Clone the repo
`git clone https://github.com/oksanaaam/lead_generation_service.git`
2. Open the project folder in your IDE
3. Open a terminal in the project folder
4. If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:
```
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

### Installation PostgreSQL and create database.

Set the required environment variables in .env.sample file:

```
SECRET_KEY=<your SECRET_KEY>
ALLOWED_HOSTS=<your ALLOWED_HOSTS>
DEBUG = <your debug>

POSTGRES_HOST=<your db hostname>
POSTGRES_DB=<your db name>
POSTGRES_USER=<your user name>
POSTGRES_PASSWORD=<your password>
```

### Run database migrations:

```
python manage.py makemigrations
python manage.py migrate
```

## Usage

Start the server:

`python manage.py runserver`

Visit the log-in page and enter your credentials to log in.
![img.png](static%2Fimg%20for%20README.md%2Fimg.png)

If you don't have an account, click on the sign-up link to create a new account.
![img_1.png](static%2Fimg%20for%20README.md%2Fimg_1.png)

Once logged in, navigate to the Lead Generator page.
![img_2.png](static%2Fimg%20for%20README.md%2Fimg_2.png)

Enter the keywords, location, and the desired number of leads.
![img_3.png](static%2Fimg%20for%20README.md%2Fimg_3.png)

Submit the form to generate leads.(this page are in deploying by other programmers)
![img_5.png](static%2Fimg%20for%20README.md%2Fimg_5.png)

Use the navigation bar to access other pages or log out.
![img_4.png](static%2Fimg%20for%20README.md%2Fimg_4.png)
