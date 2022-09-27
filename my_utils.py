from ctypes.wintypes import RGB
import matplotlib.pyplot as plt
import numpy as np

import os
import glob
from sklearn.model_selection import train_test_split
import shutil
import csv
import tensorflow as tf


from keras.preprocessing.image import ImageDataGenerator



# def display_some_examples(examples, labels):

#    plt.figure(figsize=(10,10))

#    for i in range(25):

#       idx = np.random.randint(0, examples.shape[0] - 1)
#       img = examples[idx]
#       label = labels[idx]

#       plt.subplot(5,5, i+1)
#       plt.title(str(label))
#       plt.imshow(img)

#    plt.show()

#processes the dataset into easily usable directories
def process_plantvillage_dataset(path_to_dataset, val_split_size=0.1, test_split_size=0.1):
   #deletes grayscale and segmented datasets
   path_to_grayscale_set = os.path.join(path_to_dataset, 'grayscale')
   shutil.rmtree(path_to_grayscale_set)
   path_to_segmented_set = os.path.join(path_to_dataset, 'segmented')
   shutil.rmtree(path_to_segmented_set)

   #gets path of color folder
   path_to_color_set = os.path.join(path_to_dataset, 'color')

   #creates val and test directories
   path_to_val = os.path.join(path_to_dataset, 'val')
   os.makedirs(path_to_val)

   path_to_test = os.path.join(path_to_dataset, 'test')
   os.makedirs(path_to_test)

   #creates path to train folder
   path_to_train = os.path.join(path_to_dataset, 'train')
   
   #rename color set to train set
   os.rename(path_to_color_set, path_to_train)

   folders = os.listdir(path_to_train)

   #copy dirs into path_to_val and path_to_test, and filled based on split sizes
   for folder in folders:

      full_path = os.path.join(path_to_train, folder)
      #image_paths = glob.glob(os.path.join(full_path, '*.JPG'))

      #split data into training and validation data
      #x_train, x_del = train_test_split(image_paths, test_size=.8)

      #for x in x_del:
      #   os.remove(x)

      image_paths2 = glob.glob(os.path.join(full_path, '*.JPG'))

      #split data into training and validation data
      x_train, x_val = train_test_split(image_paths2, test_size=val_split_size)

      for x in x_val:

         path_to_folder = os.path.join(path_to_val, folder)

         if not os.path.isdir(path_to_folder):
            os.makedirs(path_to_folder)
         
         #if os.path.isfile(x):
         shutil.move(x, path_to_folder)
      
      image_paths3 = glob.glob(os.path.join(full_path, '*.JPG'))

      #split data into training and test data
      x_train, x_test = train_test_split(image_paths3, test_size=test_split_size)

      for x in x_test:

         path_to_folder = os.path.join(path_to_test, folder)

         if not os.path.isdir(path_to_folder):
            os.makedirs(path_to_folder)
         
         shutil.move(x, path_to_folder)

#data generators
def create_generators(batch_size, train_data_path, val_data_path, test_data_path):

   preprocessor = ImageDataGenerator(rescale= 1. /255)

   train_generator = preprocessor.flow_from_directory(
      train_data_path, 
      class_mode="categorical", 
      target_size=(256, 256),
      color_mode='rgb',
      shuffle=True,
      batch_size=batch_size
   )
   
   val_generator = preprocessor.flow_from_directory(
      val_data_path, 
      class_mode="categorical", 
      target_size=(256, 256),
      color_mode='rgb',
      shuffle=False,
      batch_size=batch_size
   )

   test_generator = preprocessor.flow_from_directory(
      test_data_path, 
      class_mode="categorical", 
      target_size=(256, 256),
      color_mode='rgb',
      shuffle=False,
      batch_size=batch_size
   )

   return train_generator, val_generator, test_generator

def test_model(test_generator, val_generator):
   model = tf.keras.models.load_model('./Models')
   model.summary

   print("validation:")
   model.evaluate(val_generator)

   print("test")
   model.evaluate(test_generator)

if __name__=="__main__":

   model = tf.keras.models.load_model('./Models')
   model.summary()

   apple_scab_path = "C:\\Users\\omaro\\Documents\\GitHub\\Leaf_Disease_Detection\\Testing Photos\\Apple__Apple_Scab.png"

   apple_scab_sideways_path = "C:\\Users\\omaro\\Documents\\GitHub\\Leaf_Disease_Detection\\Testing Photos\\Apple__Apple_Scab_Sideways.png"

   apple_healthy_path = "C:\\Users\\omaro\\Documents\\GitHub\\Leaf_Disease_Detection\\Testing Photos\\Apple__Healthy.png"

   apple_scab = tf.io.read_file(apple_scab_path)
   apple_scab = tf.image.decode_png(apple_scab_path)
   apple_scab = tf.io.read_file(apple_scab_path)

   apple_scab_sideways

   apple_healthy