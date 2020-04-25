from flask import Flask #impport the Flask class from the Flask module to be used to create an app instance
from .config import DevConfig

#application initialization
app = Flask(__name__)  #create an app instance and pass in the __name__ variable

#setting up the configurations below
app.config.from_object(DevConfig)


from app import views #this allows us to create views