import tkinter as tk
import joblib
import numpy as np

class ZooApplication(tk.Frame):
    def __init__(self, root=None, model_path=None):
        super().__init__(root)
        self.root = root
        self.model_path = model_path
        self.model = None

        self.class_labels = []
        self.entries = {}
        self.entry_names = [
        'hair', 'feathers', 'eggs', 'milk', 'airborne',
        'aquatic', 'predator', 'toothed', 'backbone', 'breathes', 'venomous',
        'fins', 'legs', 'tail', 'domestic', 'catsize']

    def get_model(self):
        with open(self.model_path, 'rb') as model_file:
            self.model = joblib.load(model_file)

    def create_widgets(self):
        tk.Label(self, text='Predict Zoo Type\n', font=('Arial', 24)).pack()

        for name in self.entry_names:
            self.entries[f'{name}'] = tk.Entry(self)

        for name, entry in self.entries.items():
            tk.Label(self, text=name.upper()).pack()
            entry.pack()

        self.predict_button = tk.Button(self, text='PREDICT', fg='green', command=self.predict_pop)
        self.predict_button.pack()

        self.quit = tk.Button(self, text='QUIT', fg='red', command=self.root.destroy)
        self.quit.pack(side='bottom')

    def predict_class(self):
        features = [np.float64(entry.get()) for entry in self.entries.values()]
        features_array = np.array(features).reshape(1, -1)
        prediction_num = self.model.predict(features_array)
        prediction_label = prediction_num[0]
        probabilities = [f'{idx+1}: ' + str(perc*100) + '%' for idx, perc in enumerate(self.model.predict_proba(features_array)[0])]

        self.prediction_label_title = tk.Label(self, text=f'\nZoo Type Prediction: {prediction_label}\n')
        self.prediction_label_title.pack()

        for probability in probabilities:
            self.class_labels.append(tk.Label(self, text=f'Type {probability}'))

        for class_label in self.class_labels:
            class_label.pack()

        self.predict_button['state'] = tk.DISABLED

    def predict_pop(self):
        self.class_labels.clear()

        toplevel = tk.Toplevel()
        toplevel.title('Zoo Prediction')
        toplevel.geometry('500x500')

        features = [np.float64(entry.get()) for entry in self.entries.values()]
        features_array = np.array(features).reshape(1, -1)
        prediction_num = self.model.predict(features_array)
        prediction_label = prediction_num[0]
        probabilities = [f'{idx+1}: ' + str(perc*100) + '%' for idx, perc in enumerate(self.model.predict_proba(features_array)[0])]

        self.prediction_label_title = tk.Label(toplevel, text=f'\nZoo Type Prediction: {prediction_label}\n')
        self.prediction_label_title.pack()

        for probability in probabilities:
            self.class_labels.append(tk.Label(toplevel, text=f'Type {probability}'))

        for class_label in self.class_labels:
            class_label.pack()

root = tk.Tk()
root.title('Zoo Type Classification')
root.geometry('450x1000')

app = ZooApplication(root=root, model_path='zoo_model.joblib')
app.pack()
app.get_model()
app.create_widgets()
app.mainloop()