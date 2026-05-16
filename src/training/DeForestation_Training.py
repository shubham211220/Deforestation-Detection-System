from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
from keras.models import Sequential
import matplotlib.pyplot as plt
model=Sequential()
model.add(Conv2D(32,(3,3),activation='relu',input_shape=(150,150,3)))#l1
model.add(MaxPooling2D() )

model.add(Conv2D(32,(3,3),activation='relu'))#L2
model.add(MaxPooling2D() )

model.add(Conv2D(32,(3,3),activation='relu'))#L3
model.add(MaxPooling2D() )

model.add(Flatten())
model.add(Dense(100,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

history=model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])



from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        '../../dataset/train',
        target_size=(150,150),
        batch_size=64 ,
        class_mode='binary')

test_set = test_datagen.flow_from_directory(
        '../../dataset/test',
        target_size=(150,150),
        batch_size=64,
        class_mode='binary')

history=model.fit_generator(
        training_set,
        epochs=150,
        validation_data=test_set,

        )

model.save('../../models/deforestation_trained_data.h5',history)

print("==============================saved the model===============================================")

# summarize history for accuracy
fig = plt.figure(1)
plt.title('Model Accuracy Graph')
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
fig = plt.figure(2)
plt.title('Model Loss Graph')
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()