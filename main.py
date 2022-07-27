import tkinter as tk

window = tk.Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

# row = 0
miles_entry = tk.Entry(width=10)
miles_entry.focus()
miles_entry.grid(row=0, column=1)

miles_label = tk.Label(text="Miles")
miles_label.grid(row=0, column=2)

# row = 1
to_label = tk.Label(text="is equal to")
to_label.grid(row=1, column=0)

km_result_label = tk.Label(text=0)
km_result_label.grid(row=1, column=1)

km_label = tk.Label(text="Km")
km_label.grid(row=1, column=2)


# row = 2
def miles_to_km():
    miles = float(miles_entry.get())
    km = round(miles * 1.609, 2)
    km_result_label.config(text=f"{km}")


button = tk.Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

window.mainloop()
