import keras
from keras.models import load_model

model = load_model('minst.h5')

model.predict()
