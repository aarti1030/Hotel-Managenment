import tkinter as tk
from tkinter import Toplevel


def display_menu():
    # Create a new window
    menu_window = Toplevel()
    menu_window.title("Hotel Menu")
    menu_window.geometry("300x200")

    # Menu items with updated prices
    menu_items = {
        "Special Pizza": "₹400",
        "Burger": "₹150",
        "Fries": "₹60",
        "Soda": "₹20",
        "Pasta": "₹200",
        "Salad": "₹200",
        "Ice Cream": "₹150",
        "Pizza": "₹200"
    }

    # Display menu items in the new window
    for item, price in menu_items.items():
        tk.Label(menu_window, text=f"{item}: {price}").pack()

root = tk.Tk()
root.title("Hotel Del Luna")
root.geometry("1000x600")

# Define a large font
large_font = ('Alex', 24, 'bold')

# Create a Label widget to display the hotel name
hotel_label = tk.Label(root, text="Hotel Del Luna", font=large_font)
hotel_label.grid(row=0, column=0, columnspan=4, pady=20)

# Menu items for bill calculation with updated prices
menu_items1 = {
    "Special Pizza": 400,
    "Burger": 150,
    "Fries": 60,
    "Soda": 20,
    "Pasta": 200,
    "Salad": 200,
    "Ice Cream": 150,
    "Pizza": 200
}

quantities = {}

# Initialize order number
order_number = 1

def calculate_bill():
    global order_number
    subtotal = sum(menu_items1[item] * int(quantities[item].get() or 0) for item in menu_items1)
    service_charge = subtotal * 0.1  # Assuming 10% service charge
    total = subtotal + service_charge

    # Displaying the bill details in rupees
    bill_details = f"Order Number: {order_number}\nSubtotal: ₹{subtotal:.2f}\nService Charge: ₹{service_charge:.2f}\nTotal: ₹{total:.2f}"
    bill_text.set(bill_details)

    # Increment the order number for the next order
    order_number += 1

for i, item in enumerate(menu_items1):
    tk.Label(root, text=item).grid(row=i + 1, column=0, padx=10, pady=5)
    qty_var = tk.StringVar()
    tk.Entry(root, textvariable=qty_var, width=5).grid(row=i + 1, column=1, padx=10, pady=5)
    quantities[item] = qty_var

# Bill Details
bill_text = tk.StringVar()
bill_frame = tk.LabelFrame(root, text="Bill Details", padx=10, pady=10, bg="light pink", fg="black",
                           font=("Arial", 10, "bold"))
bill_frame.grid(row=1, column=2, rowspan=8, sticky="nsew", padx=5, pady=5, columnspan=2)

bill_label = tk.Label(bill_frame, textvariable=bill_text, justify='left', fg="black", font=("Arial", 10, "bold"))
bill_label.pack()

def reset_order():
    for qty in quantities.values():
        qty.set('')
    bill_text.set('')

def quit_app():
    root.destroy()

# Define button sizes
button_width = 20
button_height = 3

# Create four large buttons in a row
button1 = tk.Button(root, text="item_Price", fg="black", bg="yellow", borderwidth=3, width=button_width,
                    height=button_height, command=display_menu, font=("Arial", 10, "bold"))
button1.grid(row=10, column=0, padx=10, pady=10)

button2 = tk.Button(root, text="Total", fg="black", bg="green", borderwidth=3, width=button_width, height=button_height,
                    command=calculate_bill, font=("Arial", 10, "bold"))
button2.grid(row=10, column=1, padx=10, pady=10)

button3 = tk.Button(root, text="Reset", fg="black", bg="lightblue", borderwidth=3, width=button_width,
                    height=button_height, command=reset_order, font=("Arial", 10, "bold"))
button3.grid(row=10, column=2, padx=10, pady=10)

button4 = tk.Button(root, text="Quit", fg="black", bg="red", borderwidth=3, width=button_width, height=button_height,
                    command=quit_app, font=("Arial", 10, "bold"))
button4.grid(row=10, column=3, padx=10, pady=10)

# Run the application
root.mainloop()
