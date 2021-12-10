# Data Representaton Project

## GMIT Autumn/Winter 2021

___

![wine](/images/wine2.jpg)

### Daddy's Wine Wishlist!
---
#### Introduction
The brief for this project was to write a program that demonstrates that an understanding of creating and consuming
RESTful APIs. 

#### Quickview
![wine](/images/pythonAnywhere.jpeg)  
The application can be viewed here with pythonanywhere
Login screen (not working!) - https://caoimhinv.pythonanywhere.com/login.html
Welcome page - https://caoimhinv.pythonanywhere.com/welcome.html
Main page - https://caoimhinv.pythonanywhere.com/daddyswine.html
Create function not working!

You can skip the next two steps!

#### Install and run
You need a python environment – the packages needed are listed in the requirements.txt file. Steps to installation:
1. Download the code from https://github.com/Caoimhinv/data_representation_project
2. install the necessary packages by running the follopwing code from the terminal (or command line):  
```pip install -r requirements.txt```
3. You then need to run MySQL - from Terminal:
```mysql -u root -p```
4. Create a database and 2 tables to run in tandem with the application. The following SQL code will do that:

``` SQL
CREATE DATABASE wineCellar;
USE wineCellar;
CREATE TABLE wines3 (ID int AUTO_INCREMENT, nameProducer varchar(50), vintage int, regionCountry varchar(50), PRIMARY KEY (ID));
```  

Populate the table to get going:

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

5. Create a configuration file entitled dbConfig.py and copy in the code from the template configTemplate.py, replacing the username and password with your own.

6. Start the server from the terminal by running `python server.py`

7. Open your broswer and view the pages:  
http://localhost:5000/  
http://localhost:5000/login.html  
http://localhost:5000/welcome.html  
http://localhost:5000/daddyswine.html  

---

#### Explore
The table will be pre-populated with the default wines added to the database. You can delete or update these, and then add your own wines. Endless hours of fun! 😆

---
## Credits/References
https://developer.mozilla.org/en-US/docs/Web/CSS/background-color

https://www.w3schools.com/jsref/prop_style_display.asp

https://www.w3schools.com/html/html5_syntax.asp

https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/

https://stackoverflow.com/questions/20137688/login-with-flask-framework


---
# END

#### Contact
caoimhinvallely@gmail.com



