
# Leaf Disease Detection - READ ME IN PROGRESS

![Apple_Scab](https://github.com/omarshaban0/Leaf_Disease_Detection/blob/main/Assets%20for%20Readme/Apple_Scab_Leaf.JPG)
![Apple_Healthy](https://github.com/omarshaban0/Leaf_Disease_Detection/blob/main/Assets%20for%20Readme/Apple_Healthy_Leaf.JPG)

Modern agriculture has come a long way, with many technologies and tools to prevent issues in farming and maximize profits. Some of these tools can be detrimental to the environment though, with chemicals such as herbicides, fungicides, etc. effecting our plants and soil. 

This is why I created this project, which uses a [dataset](https://www.tensorflow.org/datasets/catalog/plant_village) of over 54,000 images of 38 different classes of 38 classes of varying leaves, and 14 different species of plants (Apple, Blueberry, Cherry, Corn, Grape, Orange, Peach, Bell Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, and Tomato).

## Project Details

####  Model Summary

![Model Summary](https://github.com/omarshaban0/Leaf_Disease_Detection/blob/main/Assets%20for%20Readme/Model_Summary.PNG)

####  Result of testing set, shows a ~97% accuracy

![Accuracy](https://github.com/omarshaban0/Leaf_Disease_Detection/blob/main/Assets%20for%20Readme/accuracy.png)

## Technologies Used
I used 5 key technologies :

* [TensorFlow](https://www.tensorflow.org/) - open source library used for machine learning
* [Google Coral DevBoard](https://coral.ai/products/dev-board/) - single board computer mainly used for running machine learning models, most important aspect is the [TPU](https://www.assured-systems.com/us/news/article/google-edge-tpu---what-is-it-and-how-does-it-work/). I am also using the Coral Camera, a camera used specifically for the devboard.
* [miniconda](https://docs.conda.io/en/latest/miniconda.html) - minimal version of conda, an environment manager
* [pip](https://github.com/pypa/pip) - python package installer and management tool
* [PlantVillage](https://www.tensorflow.org/datasets/catalog/plant_village) - Dataset used for ML model training, validation, and testing


##### Other key technologies used include:

* [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) - single board computer used as host for setting up DevBoard
* [Visual Studio Code](https://code.visualstudio.com/) - IDE used for development


#### More technologies will be added in the future as more features are added

## Project Setup - WIP


## Future Scope - WIP
#### To be completed
1. Finish testing code. I have made the model with 97% accuracy, but I need to add the funcionality of inputting a path of an image, and returning what class of leaf it is. This should be very easy, with loading the image, the model, and then running the model onto the image.
2. Running model on DevBoard with camera. I have already converted the model into a tflite in the code, and then was able to use .... I am now trying to use the given [image recognition tools](https://github.com/google-coral/examples-camera) from google, and have currently tried gstreamer but was not able to run the model on it, only being able to access the camera.
3. Cleaning up code. I feel that my code is kind of scattered, and needs to be compiled into specific files for specific functions.
4. Test Model in person. After I finish #2 (Running Model on DevBoard), I plan on visiting some orchards and farms to test the model with actual leaves. I expect that it will not do as well, since the training images had black/grey backgrounds, and were all in the same direction, which is not realistic.
#### Things to Explore
1. Using C++ for model. While Python is great for a lot of reasons, it can be very costly in speed and power. This is why I want to explore using the C++ infrastructure for Tensorflow, and see if it can make it more efficient.
2. Using TensorFlow technology to monitor/graph model training. I have recently seen some other projects that were able to produce graphs, and data to show how the process of training the model was over time. I think implementing that tool will make it easier to monitor how tweaks in the model will effect the training.
