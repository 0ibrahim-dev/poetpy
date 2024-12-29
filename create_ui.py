import tkinter as tk
import func

def ui():
    root = tk.Tk()
    root.title("Grid Layout")
    root.geometry("600x400")

    # Input alanı
    input_frame = tk.LabelFrame(root, text="Input", bg="white", fg="blue", relief="flat", padx=10, pady=10)
    input_frame.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=5, pady=5)
    
    # Input text area
    input_text = tk.Text(input_frame, height=10, width=30)
    input_text.pack(fill="both", expand=True)

    # Model frame
    model_frame = tk.LabelFrame(root, text="Model Selection", bg="white", fg="blue", relief="flat", padx=10, pady=10)
    model_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
    
    # Model seçenekleri
    model_var = tk.StringVar(value="model1")
    models = [("Model 1", "model1"), ("Model 2", "model2"), ("Model 3", "model3")]
    
    for i, (text, value) in enumerate(models):
        rb = tk.Radiobutton(model_frame, text=text, value=value, variable=model_var, bg="white")
        rb.pack(anchor="w", pady=2)

    # Button
    button = tk.Button(root, text="Process", bg="lightgreen", command=lambda: func.buttonClicked())
    button.grid(row=1, column=1, sticky="n", padx=5, pady=5)

    # Output alanı
    output_frame = tk.LabelFrame(root, text="Output", bg="white", fg="blue", relief="flat", padx=10, pady=10)
    output_frame.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
    
    # Output text area
    output_text = tk.Text(output_frame, height=6, width=30)
    output_text.pack(fill="both", expand=True)

    # Grid yapı oranları
    root.grid_rowconfigure(0, weight=5)
    root.grid_rowconfigure(1, weight=2)
    root.grid_rowconfigure(2, weight=3)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    root.mainloop()
