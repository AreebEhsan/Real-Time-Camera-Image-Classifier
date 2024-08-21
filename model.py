from sklearn.svm import LinearSVC
import numpy as np
import cv2 as cv
import PIL

class Model:

    def __init__(self):
        self.model = LinearSVC()

    def train_model(self, counters):
        img_list = []
        class_list = []

        target_width, target_height = 120, 140  # Example target dimensions

        for i in range(1, counters[0]):
            img = cv.imread(f'1/frame{i}.jpg')
            img = cv.resize(img, (target_width, target_height))  # Resize to target dimensions
            img = img.flatten()  # Flatten image to 1D array
            img_list.append(img)
            class_list.append(1)

        for i in range(1, counters[1]):
            img = cv.imread(f'2/frame{i}.jpg')
            img = cv.resize(img, (target_width, target_height))  # Resize to target dimensions
            img = img.flatten()  # Flatten image to 1D array
            img_list.append(img)
            class_list.append(2)

        img_list = np.array(img_list)
        class_list = np.array(class_list)

        self.model.fit(img_list, class_list)
        print("Model Successfully Trained!")

    def predict(self, frame):
        frame = frame[1]
        cv.imwrite("frame.jpg", cv.cvtColor(frame, cv.COLOR_RGB2GRAY))
        img = PIL.Image.open("frame.jpg")
        img = img.resize((120, 140), PIL.Image.Resampling.BOX)  # Resize to target dimensions
        img.save("frame.jpg")

        img = cv.imread('frame.jpg')
        img = cv.resize(img, (120, 140))  # Ensure consistent dimensions
        img = img.flatten()  # Flatten image to 1D array
        prediction = self.model.predict([img])

        return prediction[0]
