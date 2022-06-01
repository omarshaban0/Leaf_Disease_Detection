import os
import numpy as np

import tensorflow as tf
#from my_utils import create_generators, process_plantvillage_dataset, fix_gpu, test_model
from tensorflow.python.keras.callbacks import EarlyStopping
from leaves_model import diseasedleaves_model


if __name__=="__main__":

   #set path to path of plantvillage dataset folder
   path_to_dataset= "C:\\Users\\omaro\\Documents\\GitHub\\Leaf_Disease_Detection\\plantvillage dataset"
   process_plantvillage_dataset(path_to_dataset=path_to_dataset)

   #set path to previous path, but add \\train, \\val, and \\test to each corresponding \\test
   path_to_train= "C:\\WeedDetection\\plantvillage dataset\\train"
   path_to_val= "C:\\WeedDetection\\plantvillage dataset\\val"
   path_to_test= "C:\\WeedDetection\\plantvillage dataset\\test"
   batch_size = 8
   epochs = 30

   train_generator, val_generator, test_generator = create_generators(batch_size=batch_size, train_data_path=path_to_train, val_data_path=path_to_val, test_data_path=path_to_test)
   nbr_classes = train_generator.num_classes

   path_to_save_model = './Models'

   checkpoint_saver = tf.keras.callbacks.ModelCheckpoint(
      path_to_save_model,
      monitor="val_accuracy",
      mode='max',
      save_best_only=True,
      save_freq='epoch',
      verbose=1
   )

   early_stop = EarlyStopping(monitor="val_accuracy", patience=10)

   model = diseasedleaves_model(nbr_classes=nbr_classes)

   model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

   model.fit(
     train_generator,
     epochs= epochs,
     batch_size=batch_size,
     validation_data=val_generator,
     steps_per_epoch=train_generator.samples//train_generator.batch_size,
     validation_steps=val_generator.samples//val_generator.batch_size,
     callbacks=[checkpoint_saver],
     )
   test_model(test_generator, val_generator)

   converter = tf.lite.TFLiteConverter.from_saved_model('./Models')
   tflite_model=converter.convert()

   with open('leafdetection_model.tflite', 'wb') as f:
      f.write(tflite_model)

