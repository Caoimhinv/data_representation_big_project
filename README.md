# Data Representaton Project

## GMIT Autumn/Winter 2021

___

![wine](/images/wine2.jpg)

## Daddy's Wine Wishlist!
---
#### Introduction
The brief for this project was to write a program that demonstrates an understanding of creating and consuming RESTful APIs. I decided to create an application that allows me to store details of wines in a database and interact with them from a web interface.  

---

#### Contents of repositry  

- **images** - folder of images used in the project
- **static_pages**
    - **daddyswine.html** - main page containing the table
- **templates**
    - **welcome.html** - landing/home page with link to main page
- **.gitignore** - list of files/directories to ignore
- **WineDao.py** - DAO (data access object) links the web interface to the database
- **configTemplate.py** - template for creating config file for user
- **requirements.txt** - contains details of all packages used
- **server1.py** - Flask server

---

#### Quickview

![wine](/images/pythonAnywhere.jpeg)  

The application can be viewed here with pythonanywhere:  
https://caoimhinv.pythonanywhere.com  
Just follow the prompts.  

You can skip the next few steps if you want an easier life!

---

#### Install and run
You need to create the environment to run the application on your own machine – the packages needed are listed in the requirements.txt file.  
Steps to installation:
1. Download the code from https://github.com/Caoimhinv/data_representation_project
2. install the necessary packages by running the following code from **Terminal** (or the command line):  
`pip install -r requirements.txt`
3. You then need to run **MySQL**. From Terminal:  
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
INSERT INTO users (name, email, password) VALUES ('Caoimhin', 'caoimhinvallely@gmail.com', 'Francie4');
```

5. Create a configuration file entitled `dbConfig.py` and copy in the code from the template `configTemplate.py`, replacing the username and password with your own.

6. Start the server from the terminal by running `python server.py`

7. Open your broswer and follow the prompts or view each page with the following URLs:  
http://localhost:5000/  
http://localhost:5000/login  
http://localhost:5000/welcome.html  
http://localhost:5000/daddyswine.html  

---

#### Explore

The first page you arrive at will ask you to login - just click the link. You will be welcomed at the next page and you can click to continue or logout. You then arrive at a landing page where you can click another link to bring you to the main page. The main page table will be pre-populated with the default wines added to the database (if you did that!). You can delete or update these, and then add your own wines. Endless hours of fun! 😆 When you're done you can logout.

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



