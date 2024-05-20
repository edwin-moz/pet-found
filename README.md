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

Add a models folder and package file in the api folder: ~project/api/models/\_\_init\_\_.py

I added the 2 models and imported them into the package file.

<!-- More information about the models in the Models section -->

Add a views folder and package file in the api folder: ~project/api/views/\_\_init\_\_.py

<!-- INCLUDE SECTION HERE FOR THE MODELS -->
