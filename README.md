<!-- this area will be the app description -->

USING SQL LITE

<!-- this is how i setup the project -->

The steps using \* will be using the terminal on a mac

This project assumes you have installed Python / Django / Pip

In your computer's workspace (where you store your projects) create a folder with your project's name: ~/workspace/python/pet-found

<!-- In your terminal run the following commands to install the shell -> install django in your project -> add a django project in the current directory (app) -> add a python app (api) -> install restframework -> install django-cors-headers -->

- pipenv shell
- pipenv install django
- django-admin startproject app .
- python3 manage.py startapp api
- pip install djangorestframework
- pip install django-cors-headers

<!-- Delete the following files in the api folder -->

views.py
admin.py
models.py
test.py

<!-- Open the project in visual studio -->

1. Select the project interpreter in visual studio
2. In the debug tools and assets add a Django debug file for visual studio code.

<!-- In the app/settings.py file add the following -->

<!-- Note: Some authentication stuff is here incase I end up using it in the near future -->

1. Add apps to the INSTALLED_APPS variable:

# project setup

"rest_framework",
"rest_framework.authtoken",
"corsheaders",
"api",

2. Add the rest framework variable underneath the INSTALLED_APPS variable:

# project setup

REST_FRAMEWORK = {
"DEFAULT_AUTHENTICATION_CLASSES": (
"rest_framework.authentication.TokenAuthentication",
),
"DEFAULT_PERMISSION_CLASSES": [
"rest_framework.permissions.IsAuthenticated",
],
}

3. Add the cors variable underneath the REST_FRAMEWORK variable:

# project setup

CORS_ORIGIN_WHITELIST = (
"http://localhost:3000",
"http://127.0.0.1:3000",
"http://localhost:5173",
"http://127.0.0.1:5173",
)

4. Add the following to the MIDDLEWARE variable:

# project setup

'corsheaders.middleware.CorsMiddleware',

Add a models folder and package file in the api folder example: ~project/api/models/\_\_init\_\_.py

I added the 2 models and imported them into the package file.

<!-- More information about the models in the Models section -->

Once the models are finished, migrate the data with the following steps:

In the terminal run the following commands:

1. python3 manage.py makemigrations
2. python3 manage.py migrate

Once the migrations were done I started with the views to display data using postman

Add a views folder and package file in the api folder: ~project/api/views/\_\_init\_\_.py

I added the view to display GET the pet behavior and imported it to the package file.

<!-- More information about the views in the Views section -->

At this point we can update our urls.py file to include our newest view.

<!-- I added this import and I added this register right after the router variable was created -->

from api.views import PetBehaviorViewSet

# initial view setup

router.register(r"petbehaviors", PetBehaviorViewSet, "petbehavior")

I tested the first endpoint using Postman and it worked! (right now it is an empty array with a status of 200)

To make the initial data seed easier I am going to be adding initial data in the fixtures folder and a script to run the command.

Make a fixtures folder in the api directory: ~/project/api/fixtures/

I added a pet_bahaviors.json file to include my initial data for that model.

In the root directory I added a seed_database.sh file with the following:
#!/bin/bash

rm db.sqlite3
rm -rf ./api/migrations
python3 manage.py migrate
python3 manage.py makemigrations api
python3 manage.py migrate api

# python3 manage.py loaddata users

# python3 manage.py loaddata tokens

python3 manage.py loaddata pet_behaviors

I commented out users and tokens because we will not be using these at this time.

Next I ran this command to make the executable script:
chmod u+x ./seed_database.sh

And then I ran this command to test the script:
./seed_database.sh

It worked! My first model is done, my first view that gets the list is done, and the initial data is seeded for that model!

Now I am going to do the same with the next model view and test out the endpoint.

Great, now that we moved past that we can start working on the rest of the project which consists of also the same thing.

Since the models are finished we just need to add the views to be able to perform CRUD features

<!-- INCLUDE SECTION HERE FOR THE MODELS -->

PET BEHAVIOR

table pet_behavior {
id int pk
behavior varchar(100)
}

The reason that I included this table in the project was to give the users a fixed set of options to choose from.

Most posts about lost and found pets do not specify if the pet is friendly or runs away, which is why I wanted to include that here so that it can be chosen when creating a post.

POST

table post {
id int pk
contact_email varchar(300)
date_created datetime
pet_behavior_id fk
pet_age varchar(50)
pet_breed varchar(100)
pet_color varchar(100)
pet_description text(500)
pet_favorite_snack varchar(100)
pet_image_ur text(500)
pet_name varchar(100)
}

contact_email - user that lost or found the pet can write their email down.
date_created - this field will automatically be inserted when a post is created.
pet_behavior_id - this is a reference to the pet_behavior table.
pet_age - the use can specify the age (approximate) of the pet.
pet_breed - the user can specify a short description about the pet's breed.
pet_color - a short description about the color of the pet.
pet_description - this will be a text field with a max characted limit of 500. this field is to get more details about the pet.
pet_favorite_snack - this can be helpful for people who lost pets.
pet_image_url - at this time i will only include a way to add urls.
pet_name - if the pet has a colar this can be used for the pet name

<!-- INCLUDE SECTION HERE FOR THE VIEWS -->

PET BEHAVIOR VIEW

This view class will have the following features:
list all pet behaviors

POST VIEW

The post view class will have the following features:

1. Return all posts
2. Return a single post
3. Add a post
4. Delete a post

Deleting a post will be included but commented out to prevent users from deleting other posts.

PET BEHAVIOR SERIALIZER

The pet behavior serializer will take care of a lot of the work for us. It will convert our data to and from JSON format.

POST SERIALIZER

The post serializer will perform the same as the pet behavior but it will also give us a reference of our other table.
