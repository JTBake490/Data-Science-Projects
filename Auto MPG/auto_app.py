import numpy as np
import joblib
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, root=None, model_path=None, scaler_path=None, font=None):
        super().__init__(root)
        self.root = root
        self.model_path = model_path
        self.scaler_path = scaler_path
        self.font = font
        self.model = None
        self.scaler = None
        
        # Labels that will be shown when a prediction is made
        # and deleted when the user wants to make another prediction
        self.entries = {}
        self.prediction_label_title = None
        self.prediction_label = None
        

    def get_model(self):
        with open(self.model_path, 'rb') as joblib_file:
            self.model = joblib.load(joblib_file)
            
    def get_scaler(self):
        with open(self.scaler_path, 'rb') as scaler_file:
            self.scaler = joblib.load(scaler_file)

    def create_widgets(self):
        tk.Label(self, text='Predict Auto MPG', font=(self.font, 24)).pack()
        
        self.entries['Displacement'] = tk.Entry(self, font=(self.font, 12))
        self.entries['Horsepower'] = tk.Entry(self, font=(self.font, 12))
        self.entries['Weight'] = tk.Entry(self, font=(self.font, 12))
        self.entries['Model Year'] = tk.Entry(self, font=(self.font, 12))
            
        for key, entry in self.entries.items():
            entry.insert(0, f'{key}')
            entry.pack()
            
        self.predict_button = tk.Button(self, text='Predict MPG', command=self.predict_mpg, font=(self.font, 16))
        self.predict_button.pack()
        
        self.delete_button = tk.Button(self, text='Delete', command=self.delete_text, font=(self.font, 16))
        self.delete_button.pack()

        self.quit = tk.Button(self, text='QUIT', fg='red', command=self.root.destroy, font=(self.font, 14))
        self.quit.pack(side='bottom')
        
        
    def predict_mpg(self):        
        features = [np.float64(entry.get()) for entry in self.entries.values()]
        features_array = self.scaler.transform(np.array(features).reshape(1, -1))
        prediction = np.round(self.model.predict(features_array), 4)
        
        self.prediction_label_title = tk.Label(self, text=f'\nMiles Per Gallon Prediction:\n', font=(self.font, 18))
        self.prediction_label = tk.Label(self, text=f'{prediction[0]} Miles Per Gallon\n', font=(self.font, 18))

        self.prediction_label_title.pack()
        self.prediction_label.pack()
            
        self.predict_button['state'] = tk.DISABLED
        
        
    def delete_text(self):
        self.prediction_label_title.destroy()
        self.prediction_label.destroy()
        
        self.predict_button['state'] = tk.NORMAL
        

root = tk.Tk()
root.title('MPG Prediction Appliction')
app = Application(root=root, model_path='auto_mpg_model.joblib',
                  scaler_path='auto_mpg_scaler.joblib',
                  font='Jetbrains mono')
app.pack()
app.get_model()
app.get_scaler()
app.create_widgets()
app.mainloop()