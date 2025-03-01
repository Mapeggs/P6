from models.model import Model
from tensorflow.keras import Sequential, layers
from tensorflow.keras.layers import Rescaling
from tensorflow.keras.optimizers import Adam

class BasicModel(Model):
    def _define_model(self, input_shape, categories_count):
        self.model = Sequential([
            Rescaling(1./255, input_shape=input_shape),
            layers.Conv2D(32, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(128, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dense(categories_count, activation='softmax')
        ])
    
    def _compile_model(self):
        self.model.compile(
            optimizer=Adam(),
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )