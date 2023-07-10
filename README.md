# DoctorCalc

## 1. Info

**Video Demo:**  https://youtu.be/_UqPBXRH7_U

**Author:** Oskar Kąklewski from Gdańsk, Poland

## 2. Description

DoctorCalc is a web app with medical calculators and criteria tests/scores that I created primarily for doctors. The main inspiration for me was my wife Michelle, who is a Family Practice Doctor, and who is in need of such tool pretty much on a daily basis. My goal was to create a tool that she and other doctors could use in order to diagnose patients faster and more efficiently.

In its current form, DoctorCalc is more of a demo or a proof of concept than a finished product, but my plan is to develop it further in the nearest future. Currently, it contains three calculators, namely:

- Ibuprofen dosage,

- Paracetamol dosage,

- Package calculation,

and three medical scores:

- CHA2DS2-VASc score,

- Centor score (McIsaac modified), 

- Wells score for DVT.

All of these items have been chosen randomly as I didn't have any specific preference. 

## 3. Technical side

DoctorCalc is a web app, therefore it was created with HTML in CSS mostly. Instead of using vanilla CSS I decided to use SCSS, because I consider it easier to write and read than standard CSS. This mostly due to easier variable management and nesting of selectors. All SCSS is contained in *static/sass/main.scss* file, which has been compiled to *static/css/main.css* by Live Sass Compiler plugin for VS Code.

Back-end side of the project contains of Flask and SQLite database. All Flask code is contained in the *app.py* file. Its main purpose is to connect all the subpages, but it also manages such functions as registering an account, logging a user in and adding to/removing from favorites. SQL database, which is stored in *doctor-calc.sb*, contains four tables:

- users - with usernames and hashed passwords,

- sqlite_sequence - auto-generated,

- favorites - with usernames and items that a particular user added to the Favorites list,

- favorites_data - contains items data, such as a tag, a link and the full name.

While coding the back-end I had a dilemma whether the app should require logging in. On one hand it was necessary to be able to provide the *Add to favorites* option. On the other I wasn't very sure, whether blocking usage of the items (calculators and scores) with an account is a good idea. Finally, I decided to take a hybrid approach, which means that all items are available for all users withount having an account, but adding items to Favorites is only available for logged in users.

Another dilemma I had was whether all calculations should be performed in the back-end (by Flask) or in the front-end (by JavaScript). I decided to do it on the front-end, because I didn't want to put all items' code in the Flask app. Instead, each item's page contains its own JavaScript section, where the code is stored. It means, that whenever a user is using DoctorCalc, they only download the code dedicated to the app items they are using instead of all the code for the entire app.

Part of the code that is shared between all 3 scores is stored in *static/js/main.js*. This function is called *countScore()* and it is responsible for the summing up the value of all inputs. Each of the scores contains different interpretation of the score, therefore the functions responsible for providing the interpretation are stored in each respective HTML file. 

All HTML files are stored in the *templates/* folder. The website is put together via Flask and its templating system, therefore the most important file is *layout.html*, which contains a navbar and a footer and is extended by other HTML files.
