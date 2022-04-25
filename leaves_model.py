import tensorflow as tf
from tensorflow.python.keras.layers import Conv2D, Input, MaxPool2D, GlobalAvgPool2D, Dense, Flatten, Dropout
from tensorflow.python.keras import Model

def diseasedleaves_model(nbr_classes):

   my_input = Input(shape=(256, 256, 3))

   x = Conv2D(32, (3,3), activation='relu')(my_input)
   x = MaxPool2D()(x)
   #x = tf.keras.layers.BatchNormalization()(x)

   x = Conv2D(64, (3,3), activation='relu')(x)
   x = MaxPool2D()(x)
   #x = tf.keras.layers.BatchNormalization()(x)

   x = Conv2D(128, (3,3), activation='relu')(x)
   x = MaxPool2D()(x)
   #x = tf.keras.layers.BatchNormalization()(x)

   #x = Flatten()(x)
   x = GlobalAvgPool2D()(x)
   #x = Dropout(rate=0.6)(x)
   x = Dense(128, activation='relu')(x)
   x = Dense(nbr_classes, activation='softmax')(x)

   return Model(inputs=my_input, outputs=x)

# used for testing
if __name__=="__main__":

   model = diseasedleaves_model(10)
   model.summary()