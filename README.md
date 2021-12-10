# Data Representaton Project

## GMIT Autumn/Winter 2021

___

![wine](/images/wine2.jpg)

## Daddy's Wine Wishlist!
---
#### Introduction
The brief for this project was to write a program that demonstrates an understanding of creating and consuming RESTful APIs. I decided to create an application that allows me to store details of wines in a database and interact with them from a web interface. There is a second database containing contact details which are used to verify the user at login.

---

#### Contents of repositry  

- **images** - folder of images used in the project
- **static_pages**
    - **daddyswine.html** - main page containing the table and options for CRUD operations
- **templates**
    -**login.html** - html page for loggin in
    - **welcome.html** - landing/welcome page with link to continue to main page or logout
- **.gitignore** - list of files/directories to ignore
- **WineDao.py** - DAO (data access object) links the web interface to the database
- **configTemplate.py** - template for creating config file for user
- **requirements.txt** - contains details of all packages used
- **server1.py** - Flask server

---

#### Quickview

![wine](/images/pythonAnywhere.jpeg)  

The application can be viewed here with **pythonanywhere**:  
https://caoimhinv.pythonanywhere.com/ 
Just follow the prompts.  
Pythonanywhere seems to be a bit troublesome in that the database doesn't always load! In which case you might want to try the following!

---

#### Install and run
You need to create the environment to run the application on your own machine – the packages needed are listed in the requirements.txt file.  

Steps to installation:
1. Download the code from https://github.com/Caoimhinv/data_representation_project
2. install the necessary packages by running the following code from **Terminal** (or the command line):  
`pip install -r requirements.txt`
3. You then need to run **MySQL** (from Terminal):  
`mysql -u root -p`
4. Create a database and 2 tables to run in tandem with the application. The following SQL code will do that:

``` SQL
CREATE DATABASE wineCellar;
USE wineCellar;
CREATE TABLE wines3 (ID int AUTO_INCREMENT, nameProducer varchar(50), vintage int, regionCountry varchar(50), PRIMARY KEY (ID));
```  

Populate the table with default data:

``` SQL
INSERT INTO wines3 (nameProducer, vintage, regionCountry) VALUES ('Chateau Margaux', 1953, 'Bordeaux, France'),('Grange, Penfolds', 1986, 'South Australia');
```

Create a second table and populate:

``` SQL
CREATE TABLE users (ID int AUTO_INCREMENT, name varchar(50), email varchar(50), password varchar(50), PRIMARY KEY (ID));
```

``` SQL
INSERT INTO users (name, email, password) VALUES ('admin', 'cadmin@admin.com', 'admin');
```

5. Create a configuration file entitled `dbConfig.py` and copy in the code from the template `configTemplate.py`, replacing the username and password with your own.

6. Start the server from the terminal by running `python server.py`

7. Open your broswer and follow the prompts or view each page with the following URLs:  
http://localhost:5000/  
http://localhost:5000/login  
http://localhost:5000/welcome  
http://localhost:5000/daddyswine.html  

---

#### Explore

The first page you arrive at says 'hello' and prompts you to 'continue'. This leads you to the loginpage. The pythonanwhere site login details are:  

```
username: admin@admin.com
password: admin
```

If you're running the application locally, and you populated the `users` table in the `wineCellar` database with the suggested code above, it'll be the same.

If your details are accepted, you will be welcomed at the next page where you can click to continue or logout. You then arrive at the main page. The main page table will be pre-populated with default wines (pythonanywhere) or with the wines you added to the database manually. On either platform you can update or delete these, then add your own wines, and have a glass while you're doing it. Endless hours of fun! 😆 When you're done you can logout.


![wineLogo](/images/wineLogo.jpg)

---
## Credits/References

https://developer.mozilla.org/en-US/docs/Web/CSS/background-color

https://www.w3schools.com/jsref/prop_style_display.asp

https://www.w3schools.com/html/html5_syntax.asp

https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/

https://stackoverflow.com/questions/20137688/login-with-flask-framework


---
<br>

# END

#### Contact
caoimhinvallely@gmail.com



