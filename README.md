# Full-Stack Developer Test

I have uploaded my solutions to the 6 questions on GitHub. Each question has its own folder, so please open the respective folder to check the solution.

## Table of Contents

- Question_01
  - Dependencies
  - Installation
- Question_02
  - Dependencies
  - Installation
- Question_03
  - task 03- Solution.pdf
- Question_04
  - task 04- Solution.pdf
- Question_05
  - task 05- Solution.pdf
- Question_06
  - task 06- Solution.pdf

## Question_01

This Flask application allows users to input an email address and retrieves the referral relationship associated with that email from a SQLite database. Here's a brief overview of how it works:

Setting up the Flask App and Database: The code initializes a Flask application and configures a SQLite database to store client data.

Defining the Client Model: A Client model is defined using SQLAlchemy, representing the client's email and their referral email.

Inserting Data from CSV: The function insert_clients_from_csv() reads client data from a CSV file and inserts it into the database. It checks for existing clients before adding new ones to avoid duplicates.

Retrieving Referral Relationship: The function get_referral_relationship() retrieves the referral relationship for a given email by recursively traversing the database.

Rendering the HTML Template: The Flask route / serves the HTML template index.html, which contains a form for users to input an email address. Upon form submission, it retrieves the referral relationship for the provided email and displays it on the page.

this application demonstrates a simple Flask web app integrated with a database to retrieve and display referral relationships based on user input.

## Dependencies

Dependencies for this project are managed using a requirements.txt file, which is commonly used with pip to install the required Python packages.

## Installation

#### 01. Changes the directory to "Question_01"

```bash
  cd Question_01
```

#### 02. Installs the virtualenv package, which is used to create isolated Python environments.

```bash
  pip install virtualenv
```

#### 03. Creates a new virtual environment named "env" in the current directory

```bash
  virtualenv env
```

#### 04. Activates the virtual environment

```bash
  Mac OS / Linux: source mypython/bin/activate
  windows (cmd): env\Scripts\activate
```

#### 05. Installs the Python packages listed in the "requirements.txt" file

```bash
  pip install -r requirements.txt
```

#### 06. Runs the application

```bash
  python -m app
```

#### 07. Access the API at http://127.0.0.1:5000/

## Installation

#### 01. Changes the directory to "Question_01"

```bash
  cd Question_01
```

#### 02. Installs the virtualenv package, which is used to create isolated Python environments.

```bash
  pip install virtualenv
```

#### 03. Creates a new virtual environment named "env" in the current directory

```bash
  virtualenv env
```

#### 04. Activates the virtual environment

```bash
  Mac OS / Linux: source mypython/bin/activate
  windows (cmd): env\Scripts\activate
```

#### 05. Installs the Python packages listed in the "requirements.txt" file

```bash
  pip install -r requirements.txt
```

#### 06. Runs the application

```bash
  python -m app
```

#### 07. Access the API at http://127.0.0.1:5000/

## Question_02

This Flask application serves as a backend API for retrieving user information based on their email address. Here's a brief explanation of how it works:

Setting up the Flask App: The code initializes a Flask application and sets up a CORS policy to allow cross-origin requests.

Defining a Sample Table: A sample table is defined to store user information, including their name and points, indexed by email addresses.

Creating an API Endpoint: An endpoint /get_info is created using Flask-RESTful. This endpoint accepts POST requests containing an email address in the request body.

Handling POST Requests: When a POST request is made to the /get_info endpoint, the application parses the email address from the request body. It then checks if the email exists in the sample table. If found, it returns the corresponding user information; otherwise, it returns an error message.

Frontend Integration: The provided HTML page allows users to enter an email address. When the "Get Info" button is clicked, it triggers a JavaScript function (getUserInfo()) that sends a POST request to the Flask backend with the entered email address. The response is then displayed on the page.

API Configuration: The JavaScript code references an api_config.js file to retrieve the API URL dynamically. This file is assumed to define a variable API_URL containing the base URL of the API.

this application demonstrates a simple Flask backend serving a RESTful API endpoint, integrated with a basic HTML frontend for user interaction.

## Dependencies

Dependencies for this project are managed using a requirements.txt file, which is commonly used with pip to install the required Python packages.

## Installation

#### 01. Changes the directory to "Question_01"

```bash
  cd Question_02
```

#### 02. Installs the virtualenv package, which is used to create isolated Python environments.

```bash
  pip install virtualenv
```

#### 03. Creates a new virtual environment named "env" in the current directory

```bash
  virtualenv env
```

#### 04. Activates the virtual environment

```bash
  Mac OS / Linux: source mypython/bin/activate
  windows (cmd): env\Scripts\activate
```

#### 05. Installs the Python packages listed in the "requirements.txt" file

```bash
  pip install -r requirements.txt
```

#### 06. Runs the application

```bash
  python -m app
```

#### 07. Copy the file path of index.html and paste it into the browser's address bar.

## Question_03

#### Changes the directory to "Question_03"

```bash
  cd Question_03
```

#### task 03- Solution.pdf

## Question_04

#### Changes the directory to "Question_04"

```bash
  cd Question_04
```

#### task 04- Solution.pdf

## Question_05

#### Changes the directory to "Question_05"

```bash
  cd Question_05
```

#### task 05- Solution.pdf

## Question_06

#### Changes the directory to "Question_06"

```bash
  cd Question_06
```

#### task 06- Solution.pdf

## Authors

- [@rifatblack](https://github.com/rifatblack/)

## License

[MIT](https://choosealicense.com/licenses/mit/)
