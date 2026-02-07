import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw
import numpy as np
import tensorflow as tf

class SimpleDigitGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Digit Recognizer")
        self.root.geometry("700x550")
        self.root.configure(bg="white")
        
        # Load model
        try:
            self.model = tf.keras.models.load_model("digit_model.h5")
        except:
            messagebox.showerror("Error", "Model file not found! Train the model first.")
            self.model = None
        
        # Canvas settings
        self.canvas_size = 300
        self.brush_size = 15
        self.drawing = False
        
        # PIL image for prediction
        self.image = Image.new("L", (self.canvas_size, self.canvas_size), color=0)
        self.image_draw = ImageDraw.Draw(self.image)
        
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Draw a Digit (0-9)", 
                        font=("Arial", 18, "bold"), bg="white")
        title.pack(pady=15)
        
        # Canvas
        self.canvas = tk.Canvas(self.root, width=self.canvas_size, 
                               height=self.canvas_size, bg="black", 
                               highlightthickness=2, highlightbackground="gray")
        self.canvas.pack(pady=10)
        
        # Bind drawing events
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)
        
        # Buttons frame
        btn_frame = tk.Frame(self.root, bg="white")
        btn_frame.pack(pady=15)
        
        # Predict button
        predict_btn = tk.Button(btn_frame, text="PREDICT", 
                               command=self.predict,
                               font=("Arial", 14, "bold"),
                               bg="#4CAF50", fg="white",
                               width=12, height=2)
        predict_btn.pack(side=tk.LEFT, padx=10)
        
        # Clear button
        clear_btn = tk.Button(btn_frame, text="CLEAR", 
                             command=self.clear,
                             font=("Arial", 14, "bold"),
                             bg="#f44336", fg="white",
                             width=12, height=2)
        clear_btn.pack(side=tk.LEFT, padx=10)
        
        # Result label
        self.result_label = tk.Label(self.root, text="Result: -", 
                                     font=("Arial", 24, "bold"),
                                     bg="white", fg="#2196F3")
        self.result_label.pack(pady=10)
        
        # Confidence label
        self.confidence_label = tk.Label(self.root, text="Confidence: -", 
                                        font=("Arial", 12),
                                        bg="white", fg="gray")
        self.confidence_label.pack()
    
    def start_draw(self, event):
        self.drawing = True
        self.draw(event)
    
    def draw(self, event):
        if self.drawing:
            x, y = event.x, event.y
            r = self.brush_size
            
            # Draw on canvas
            self.canvas.create_oval(x-r, y-r, x+r, y+r, 
                                   fill="white", outline="white")
            
            # Draw on PIL image
            self.image_draw.ellipse([x-r, y-r, x+r, y+r], fill=255)
    
    def stop_draw(self, event):
        self.drawing = False
    
    def clear(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (self.canvas_size, self.canvas_size), color=0)
        self.image_draw = ImageDraw.Draw(self.image)
        self.result_label.config(text="Result: -")
        self.confidence_label.config(text="Confidence: -")
    
    def predict(self):
        if self.model is None:
            messagebox.showerror("Error", "Model not loaded!")
            return
        
        if not self.canvas.find_all():
            messagebox.showwarning("Warning", "Draw a digit first!")
            return
        
        # Preprocess image
        img = self.image.resize((28, 28))
        img_array = np.array(img) / 255.0
        img_array = img_array.reshape(1, 28, 28, 1)
        
        # Predict
        prediction = self.model.predict(img_array, verbose=0)
        digit = np.argmax(prediction[0])
        confidence = prediction[0][digit] * 100
        
        # Update results
        self.result_label.config(text=f"Result: {digit}")
        self.confidence_label.config(text=f"Confidence: {confidence:.1f}%")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleDigitGUI(root)
    root.mainloop()
