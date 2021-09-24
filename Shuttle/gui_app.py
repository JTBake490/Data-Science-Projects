import numpy as np
import pickle
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, root=None, model_path=None, font=None):
        super().__init__(root)
        self.root = root
        self.model_path = model_path
        self.font = font
        self.model = None
        
        # Labels that will be shown when a prediction is made
        # and deleted when the user wants to make another prediction
        self.entries = {}
        self.prediction_label = None
        self.prob_label = None
        self.class_labels = []
        

    def get_model(self):
        with open(self.model_path, 'rb') as pkl_file:
            self.model = pickle.load(pkl_file)


    def create_widgets(self):
        tk.Label(self, text='Predict Shuttle Class', font=(self.font, 24)).pack()
        
        for entry in range(9):
            self.entries[f'e{entry}'] = tk.Entry(self, font=(self.font, 12))
            
        for feature, entry in enumerate(self.entries.values()):
            entry.insert(0, f'Feature {feature}')
            entry.pack()
            
        self.predict_button = tk.Button(self, text='Predict Class', command=self.predict_class, font=(self.font, 16))
        self.predict_button.pack()
        
        self.delete_button = tk.Button(self, text='Delete', command=self.delete_text, font=(self.font, 16))
        self.delete_button.pack()

        self.quit = tk.Button(self, text='QUIT', fg='red', command=self.root.destroy, font=(self.font, 14))
        self.quit.pack(side='bottom')
        
        
    def predict_class(self):        
        features = [np.round(np.int64(entry.get()), 4) for entry in self.entries.values()]
        features_array = np.array(features).reshape(1, -1)
        prediction = self.model.predict(features_array)
        probabilities = [f'Class{idx}: ' + str(perc*100) + '%' for idx, perc in enumerate(self.model.predict_proba(features_array)[0], start=1)]
        
        self.prediction_label = tk.Label(self, text=f'\nShuttle Prediction: {prediction[0]}\n', font=(self.font, 18))
        self.prob_label = tk.Label(self, text=f'\nClass Probabilities:\n', font=(self.font, 16))
        self.prediction_label.pack()
        self.prob_label.pack()
        
        for probability in probabilities:
            self.class_labels.append(tk.Label(self, text=probability, font=(self.font, 14)))
            
        for class_label in self.class_labels:
            class_label.pack()
            
        self.predict_button['state'] = tk.DISABLED
        
        
    def delete_text(self):
        self.prediction_label.destroy()
        self.prob_label.destroy()
        
        for class_label in self.class_labels:
            class_label.destroy()
            
        self.class_labels.clear()
        self.predict_button['state'] = tk.NORMAL
        

root = tk.Tk()
root.title('Shuttle Classfication Prediction Appliction')
app = Application(root=root, model_path='shuttle_model.pkl', font='Jetbrains mono')
app.pack()
app.get_model()
app.create_widgets()
app.mainloop()