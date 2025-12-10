import tkinter as tk
from tkinter import ttk, messagebox
def convert_temperature():
    try:
        temp = float(temp_entry.get())
        from_unit = from_combo.get()
        to_unit = to_combo.get()

        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (temp * 9/5) + 32
            elif to_unit == "Kelvin":
                result = temp + 273.15
            else:
                result = temp

        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (temp - 32) * 5/9
            elif to_unit == "Kelvin":
                result = (temp - 32) * 5/9 + 273.15
            else:
                result = temp

        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = temp - 273.15
            elif to_unit == "Fahrenheit":
                result = (temp - 273.15) * 9/5 + 32
            else:
                result = temp

        result_label.config(text=f"Result: {result:.2f} {to_unit}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x350")
root.resizable(False, False)
title = tk.Label(root, text="Temperature Converter", font=("Arial", 18, "bold"))
title.pack(pady=15)
temp_entry = tk.Entry(root, font=("Arial", 14), justify="center")
temp_entry.pack(pady=10)
frame = tk.Frame(root)
frame.pack(pady=10)
from_combo = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kelvin"], width=12)
from_combo.set("Celsius")
from_combo.grid(row=0, column=0, padx=10)
to_combo = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kelvin"], width=12)
to_combo.set("Fahrenheit")
to_combo.grid(row=0, column=1, padx=10)
convert_btn = tk.Button(root, text="Convert", font=("Arial", 12, "bold"), bg="green", fg="white", command=convert_temperature)
convert_btn.pack(pady=20)
result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

root.mainloop()
