# Angel Viankah Mercado
# BSCpE 1-5

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def show_data():
    last_name = last_name_entry.get()
    first_name = first_name_entry.get()
    age = age_entry.get()
    house_number = house_number_entry.get()
    street = street_entry.get()
    barangay = barangay_entry.get()
    municipality = municipality_entry.get()

    # Result window to display the inputted data
    result_window = tk.Toplevel(root)
    result_window.title("Result")

    result_frame = ttk.Frame(result_window, padding=(20, 10))
    result_frame.pack()

    ttk.Label(result_frame, text="They call you:", font=('Helvetica', 12)).grid(row=0, column=0, sticky=tk.W, pady=5)
    ttk.Label(result_frame, text=first_name, font=('Helvetica', 12)).grid(row=0, column=1, sticky=tk.W, pady=5)

    ttk.Label(result_frame, text="Your family name is:", font=('Helvetica', 12)).grid(row=1, column=0, sticky=tk.W, pady=5)
    ttk.Label(result_frame, text=last_name, font=('Helvetica', 12)).grid(row=1, column=1, sticky=tk.W, pady=5)

    ttk.Label(result_frame, text="Existing for:", font=('Helvetica', 12)).grid(row=2, column=0, sticky=tk.W, pady=5)
    ttk.Label(result_frame, text=age, font=('Helvetica', 12)).grid(row=2, column=1, sticky=tk.W, pady=5)

    ttk.Label(result_frame, text="House Number:", font=('Helvetica', 12)).grid(row=3, column=0, sticky=tk.W, pady=5)
    ttk.Label(result_frame, text=house_number, font=('Helvetica', 12)).grid(row=3, column=1, sticky=tk.W, pady=5)

    ttk.Label(result_frame, text="Street:", font=('Helvetica', 12)).grid(row=4, column=0, sticky=tk.W, pady=5)
    ttk.Label(result_frame, text=street, font=('Helvetica', 12)).grid(row=4, column=1, sticky=tk.W, pady=5)

    ttk.Label(result_frame, text="Barangay:", font=('Helvetica', 12)).grid(row=5, column=0, sticky=tk.W, pady=5)
    ttk.Label(result_frame, text=barangay, font=('Helvetica', 12)).grid(row=5, column=1, sticky=tk.W, pady=5)

    ttk.Label(result_frame, text="Municipality of:", font=('Helvetica', 12)).grid(row=6, column=0, sticky=tk.W, pady=5)
    ttk.Label(result_frame, text=municipality, font=('Helvetica', 12)).grid(row=6, column=1, sticky=tk.W, pady=5)

# Main window
root = tk.Tk()
root.title("Data Entry Form")
root.geometry("480x420")

# Create and place widgets using the grid layout
style = ttk.Style()
style.configure("TLabel", font=('Helvetica', 12))
style.configure("TEntry", font=('Helvetica', 12))
style.configure("TButton", font=('Helvetica', 12, 'bold'))

label_frame = ttk.Frame(root, padding=(20, 10))
label_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(label_frame, text="Name:", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

ttk.Label(label_frame, text="Last Name:").grid(row=1, column=0, sticky=tk.W, pady=5)
last_name_entry = ttk.Entry(label_frame)
last_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

ttk.Label(label_frame, text="First Name:").grid(row=2, column=0, sticky=tk.W, pady=5)
first_name_entry = ttk.Entry(label_frame)
first_name_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

ttk.Label(label_frame, text="Age:", font=('Helvetica', 12, 'bold')).grid(row=3, column=0, columnspan=2, pady=10)

ttk.Label(label_frame, text="Age:").grid(row=4, column=0, sticky=tk.W, pady=5)
age_entry = ttk.Entry(label_frame)
age_entry.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

ttk.Label(label_frame, text="Address:", font=('Helvetica', 12, 'bold')).grid(row=5, column=0, columnspan=2, pady=10)

ttk.Label(label_frame, text="House Number:").grid(row=6, column=0, sticky=tk.W, pady=5)
house_number_entry = ttk.Entry(label_frame)
house_number_entry.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)

ttk.Label(label_frame, text="Street:").grid(row=7, column=0, sticky=tk.W, pady=5)
street_entry = ttk.Entry(label_frame)
street_entry.grid(row=7, column=1, padx=10, pady=5, sticky=tk.W)

ttk.Label(label_frame, text="Barangay:").grid(row=8, column=0, sticky=tk.W, pady=5)
barangay_entry = ttk.Entry(label_frame)
barangay_entry.grid(row=8, column=1, padx=10, pady=5, sticky=tk.W)

ttk.Label(label_frame, text="Municipality:").grid(row=9, column=0, sticky=tk.W, pady=5)
municipality_entry = ttk.Entry(label_frame)
municipality_entry.grid(row=9, column=1, padx=10, pady=5, sticky=tk.W)

# To submit the data
submit_button = ttk.Button(root, text="Submit", command=show_data)
submit_button.grid(row=1, column=0, pady=10)

# Button Color
style = ttk.Style()
style.theme_use('alt')
style.configure('TButton', background = 'red', foreground = 'white', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
style.map('TButton', background=[('active','red')])

# Start the event loop
root.mainloop()