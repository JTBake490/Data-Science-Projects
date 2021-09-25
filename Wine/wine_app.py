import tkinter as tk
import numpy as np
import joblib

class WineApplication(tk.Frame):
    def __init__(self, root, model_path):
        super().__init__(root)
        self.root = root
        self.model_path = model_path
        self.font_type = 'Jetbrains mono'
        self.targets = dict(zip(range(3),['Wine Class 0', 'Wine Class 1', 'Wine Class 2']))
        self.entry_names = ['alcohol', 'malic_acid', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols',
                            'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline']
        self.entries = {}
        self.class_labels = []

    def get_model(self):
        with open(self.model_path, 'rb') as model_path:
            self.model = joblib.load(model_path)

    def create_widgets(self):
        tk.Label(self, text='Predict Wine Classification\n', font=(self.font_type, 24)).pack()

        for name in self.entry_names:
            self.entries[name] = tk.Entry(self)

        for name, entry in self.entries.items():
            tk.Label(self, text=name.title(), font=(self.font_type, 18)).pack()
            entry.insert(0, 0)
            entry.pack()

        tk.Label(self, text='\n').pack()
        
        self.predict_button = tk.Button(self, text='PREDICT', command=self.predict_class, fg='green', font=(self.font_type, 16))
        self.predict_button.pack()

        self.delete_button = tk.Button(self, text='Delete', command=self.delete_text, fg='red', font=(self.font_type, 16))
        self.delete_button.pack()

        self.quit_button = tk.Button(self, text='QUIT', command=self.root.destroy, font=(self.font_type, 14))
        self.quit_button.pack(side='bottom')

    def predict_class(self):
        features = [np.float64(entry.get()) for entry in self.entries.values()]
        features_array = np.array(features).reshape(1, -1)
        prediction_num = self.model.predict(features_array)
        prediction = self.targets[prediction_num[0]]
        probabilities = [f'{self.targets[idx]}: ' + str(perc*100) + '%' for idx, perc in enumerate(self.model.predict_proba(features_array)[0])]

        self.prediction_label_title = tk.Label(self, text='\nWine Classification Prediction:\n', font=(self.font_type, 20))
        self.prediction_label = tk.Label(self, text=f'{prediction}', font=(self.font_type, 30))

        for probability in probabilities:
            self.class_labels.append(tk.Label(self, text=probability, font=(self.font_type, 14)))

        for class_label in self.class_labels:
            class_label.pack()

        self.prediction_label_title.pack()
        self.prediction_label.pack()

        self.predict_button['state'] = tk.DISABLED

    def delete_text(self):
        self.prediction_label_title.destroy()
        self.prediction_label.destroy()

        for class_label in self.class_labels:
            class_label.destroy()
        self.class_labels.clear()

        self.predict_button['state'] = tk.NORMAL

root = tk.Tk()
root.title('Wine Classification')
root.geometry('550x900')
app = WineApplication(root, 'wine_model.joblib')
app.pack()
app.get_model()
app.create_widgets()
app.mainloop()