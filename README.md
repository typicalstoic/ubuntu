University Schedule Mini Project
=======

## Project Description

This web application is built to manage and display university course schedules.
It pulls data from a MySQL database hosted on AWS RDS and organizes it into a neatly
formatted HTML table. Users can interact with the app by sorting courses
based on difficulty levels, such as Undergraduate or Graduate, through a simple button 
click. The project combines the Flask Framework (Python) with
a remote database, incorporates some responsive web design elements, and offers 
sorting functionality for a more user-friendly experience.

## Steps Followed During Development

### 1. Initial Setup

* Created an AWS RDS instance for the MySQL database allowing all incoming traffic in inbound rules.
* Created an EC2 instance with the IAM of Ubuntu allowing public access
* Connected the RDS to the EC2 instance on AWS
* Installed MobaXterm to connect to the EC2 instance from the local machine
* Installed DBeaver to connect to the RDS instance from the local machine
* Connected DBeaver to the RDS, and MobaXterm to the EC2

#### Created two tables in the RDS instance via DBeaver:

~~~
CREATE TABLE IF NOT EXISTS courses(
	id INT auto_increment primary key,
    course VARCHAR(100),
    description VARCHAR(100),
    time VARCHAR(100),
    week_day VARCHAR(100),
    instructor VARCHAR(100),
    level INT
    );
~~~

~~~
  CREATE TABLE IF NOT EXISTS description(
	id INT auto_increment primary key,
    description TEXT
    );
    
~~~
#### Inserted initial data into the tables with varying difficulty levels.

~~~
  INSERT INTO courses(course, description, week_day, time, instructor, 4000) 
    VALUES('Math for CS', 'details', 'T', '17:30', 'Mr Nacio', 1000),
    ('INTL', 'details', 'W', '19:00', 'Ms Aljabari', 2000),
    ('Environmental Ethics', 'details', 'R', '13:30', 'Mr Unknown', 1000),
    ('Computer Programming 1', 'details', 'F', '18:30', 'Mr Debasis', 2000),
    ('Operating Systems', 'details', 'M', '12:00', 'Ms Saidjamolboeva', 1000);
   
~~~

~~~
    INSERT INTO description(description) 
    VALUES('Focuses on mathematical foundations critical for computer science, including logic, set theory, combinatorics, and graph theory.'),
    ('Introduces key concepts in international relations, exploring global political dynamics, diplomacy, and conflict resolution.'),
    ('Examines moral principles and their application to environmental issues, emphasizing sustainability and ethical decision-making'),
    ('Covers the fundamentals of programming, including syntax, algorithms, and problem-solving using a specific programming language.'),
    ('Explores the design and functioning of operating systems, including process management, memory management, and file systems.');
    
   
~~~
### 2. Backend Development
Installed Flask and MySQL connector:
 
pip install flask mysql-connector-python
Created a main.py file containing:
1. A connection to the MySQL database. 
2. A route to fetch and display course data. 
3. A sort_by_difficulty route to retrieve and display sorted data.
### 3. Frontend Development
* Designed an HTML template (table.html) for displaying course schedules in a table format. 
* Added a "Sort" and "Reset" buttons.
* Styled the table and page using inline CSS.
### 4. Code From Local Machine to EC2 Instance
* Pushed the local project to a new Github repository.
* Installed git to the EC2 instance using Mobaxterm:
    
    git clone <https://github.com/typicalstoic/ubuntu.git>
    cd project
     
* Opened the project, created and activated venv, and installed all dependencies.
### 5. AWS Hosting
* Deployed the Flask app. 
* Also set up necessary security group rules to allow HTTP traffic on port 5000 if did not before.
* Ran the Flask app in MobaXterm with:
        python3 main.py --host=0.0.0.0
    
* Verified that the web application was accessible via the EC2 instance's public IP address.
### 6. Testing and Debugging
* Verified database connections and ensured data was being displayed correctly.
* Ensured sorting functionality worked as expected when clicking the "Sort by Difficulty" button.

## Screenshots

##### 1. Home Page

![image](https://github.com/user-attachments/assets/c0cbc437-c971-426c-b63e-415e5f7c2483)

##### 2.  Page of Course Details

![image](https://github.com/user-attachments/assets/e17f68c1-7fff-456f-846f-e98d6ade57c9)


##### 3. Sorted by Difficulty

![image](https://github.com/user-attachments/assets/fa86fc6b-d796-4069-b6b5-f6d8f628afe1)


Displays the courses sorted by difficulty (e.g., 1000 first, followed by 2000, 3000 and 4000).



### Prerequisites

1. Python 3 installed on your machine.

2. Flask installed in your environment:

        pip install flask mysql-connector-python
3. An AWS RDS instance with the required schema and data. 

### Steps

1. Clone the project repository:

 
    git clone https://github.com/typicalstoic/ubuntu.git
    cd project

2. Update the database connection details in main.py:

* host
* user
* password
* database 

3. Run the Flask app:

    python3 main.py --host=0.0.0.0
4. Open the application in your browser using the public IP address of your EC2 instance:

    http://44.208.34.221:5000

## Future Improvements

* Add user authentication to secure access to the application.
* Implement advanced filtering and search functionality.
* Enhance the user interface using Bootstrap or another CSS framework.
