# Leaf_Disease_Detection

![Apple_Scab](https://github.com/omarshaban0/Leaf_Disease_Detection/blob/main/Assets%20for%20Readme/Apple_Scab_Leaf.JPG)
![Apple_Healthy](https://github.com/omarshaban0/Leaf_Disease_Detection/blob/main/Assets%20for%20Readme/Apple_Healthy_Leaf.JPG)

My friends and I love watching, analyzing and enjoying films across many genres and regions. That is why, I wanted
to create a place where me and my friends can write and critique the movies we watch. The NS Movie Review Blog
will allow authorized users to create, edit, and delete reviews for movies provided by the IMDb API. These reviews can be
viewed by anybody on the homepage, and can be queried through the search function.

## Technologies Used
I used 4 key technologies :

* [TensorFlow](https://www.tensorflow.org/) - open source library used for machine learning
* [Google Coral DevBoard](https://coral.ai/products/dev-board/) - single board computer mainly used for running machine learning models, most important aspect is the [TPU](https://www.assured-systems.com/us/news/article/google-edge-tpu---what-is-it-and-how-does-it-work/)
* [miniconda](https://docs.conda.io/en/latest/miniconda.html) - minimal version of conda, an environment manager
* [pip](https://github.com/pypa/pip) - python package installer and management tool


##### Other key technologies used include:

* [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) - single board computer used as host for setting up DevBoard
* [Visual Studio Code](https://code.visualstudio.com/) - IDE used for development


#### More technologies will be added in the future as more features are added

## Project Setup
After cloning the repository to your machine:

Install dependencies in both client and server sides of the application:

`npm install`

To test components of the application:

#### Backend:

make environment file with the following keys' values:
```
MOVIES_DB_URI= "path to mongodb url"
MOVIES_NS = "database name"
PORT = "port number"
```
Head to the backend directory of the project, and run:

`nodemon server`

#### Frontend:

Head to the frontend directory of the project, and run:

`npm start`

## Future Scope
1. 
