import tkinter as tk
import joblib
import numpy as np

class BreastCancerApplication(tk.Frame):
    def __init__(self, root=None, model_path=None):
        super().__init__(root)
        self.root = root
        self.model_path = model_path
        self.model = None

        self.entry_names = ['mean radius', 'mean perimeter', 'mean area', 'mean concave points', 'worst radius', 'worst perimeter', 'worst area', 'worst concave points']
        self.entries = {}

    def get_model(self):
        with open(self.model_path, 'rb') as model_file:
            self.model = joblib.load(model_file)

    def create_widgets(self):
        tk.Label(self, text='Predict Breast Cancer\n', font=('Arial', 24)).pack()

        for name in self.entry_names:
            self.entries[f'{name}'] = tk.Entry(self)

        for name, entry in self.entries.items():
            tk.Label(self, text=name.upper()).pack()
            entry.pack()

        self.predict_button = tk.Button(self, text='PREDICT', command=self.predict_class)
        self.predict_button.pack()

        self.delete_button = tk.Button(self, text='Delete', command=self.delete_text)
        self.delete_button.pack()

        self.quit = tk.Button(self, text='QUIT', fg='red', command=self.root.destroy)
        self.quit.pack(side='bottom')

    def predict_class(self):
        features = [np.float64(entry.get()) for entry in self.entries.values()]
        features_array = np.array(features).reshape(1, -1)
        prediction_num = self.model.predict(features_array)
        prediction_label = 'Malignant' if prediction_num[0] == 0 else 'Benign'

        self.prediction_label_title = tk.Label(self, text='\nBreast Cancer Prediction:\n')
        self.prediction_label = tk.Label(self, text=f'{prediction_label}')

        self.prediction_label_title.pack()
        self.prediction_label.pack()

        self.predict_button['state'] = tk.DISABLED

    def delete_text(self):
        self.prediction_label_title.destroy()
        self.prediction_label.destroy()

        self.predict_button['state'] = tk.NORMAL

root = tk.Tk()
root.title('Breast Cancer Classification')
root.geometry('350x750')
app = BreastCancerApplication(root=root, model_path='breast_cancer_model.joblib')
app.pack()
app.get_model()
app.create_widgets()
app.mainloop()