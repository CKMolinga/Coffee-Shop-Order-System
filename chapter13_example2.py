# Name: Kombe Molinga Prince-Charles
# Student ID: C0964367
# Chapter 13 Example 2: Coffee Shop Order System

import tkinter as tk
from tkinter import messagebox

# WINDOW SETUP
root = tk.Tk()
root.title("Coffee Shop Order System")
root.geometry("600x400")
root.configure(bg="wheat")

# VARIABLES
# Set default coffee size to "Small"
coffee_size = tk.StringVar(value="Small")

# Add-on variables
extra_shot = tk.BooleanVar()
whipped_cream = tk.BooleanVar()
caramel_drizzle = tk.BooleanVar()

# FUNCTIONS

# Calculate total price based on selected coffee size and add-ons


def calculate_total():
    total = 0.0

    # Coffee size prices
    if coffee_size.get() == "Small":
        total += 2.99
    elif coffee_size.get() == "Medium":
        total += 3.99
    elif coffee_size.get() == "Large":
        total += 4.99

    # Add-ons
    if extra_shot.get():
        total += 0.50
    if whipped_cream.get():
        total += 0.30
    if caramel_drizzle.get():
        total += 0.40

    display_label.config(text=f"Total Price: ${total:.2f}")


# Place order function to display a confirmation message
def place_order():
    display_label.config(text="Order Placed!")


# Clear order function to reset all selections and clear the display
def clear_order():
    coffee_size.set("Small")
    extra_shot.set(False)
    whipped_cream.set(False)
    caramel_drizzle.set(False)
    display_label.config(text="")


# FRAME 1: COFFEE SIZE
size_frame = tk.LabelFrame(
    root,
    text="Select Coffee Size",
    bg="lightyellow",
    bd=2,
    relief=tk.RAISED
)
size_frame.pack(side=tk.TOP, fill=tk.X, pady=10, padx=10)

tk.Radiobutton(
    size_frame, text="Small ($2.99)",
    variable=coffee_size, value="Small",
    bg="lightyellow"
).pack(side=tk.LEFT, padx=5, pady=5)

tk.Radiobutton(
    size_frame, text="Medium ($3.99)",
    variable=coffee_size, value="Medium",
    bg="lightyellow"
).pack(side=tk.LEFT, padx=5, pady=5)

tk.Radiobutton(
    size_frame, text="Large ($4.99)",
    variable=coffee_size, value="Large",
    bg="lightyellow"
).pack(side=tk.LEFT, padx=5, pady=5)

# FRAME 2: ADD-ONS
addons_frame = tk.LabelFrame(
    root,
    text="Add-Ons",
    bg="lightgreen",
    bd=2,
    relief=tk.RAISED
)
addons_frame.pack(side=tk.TOP, fill=tk.X, pady=10, padx=10)

tk.Checkbutton(
    addons_frame, text="Extra Shot (+$0.50)",
    variable=extra_shot, bg="lightgreen"
).pack(side=tk.LEFT, padx=5, pady=5)

tk.Checkbutton(
    addons_frame, text="Whipped Cream (+$0.30)",
    variable=whipped_cream, bg="lightgreen"
).pack(side=tk.LEFT, padx=5, pady=5)

tk.Checkbutton(
    addons_frame, text="Caramel Drizzle (+$0.40)",
    variable=caramel_drizzle, bg="lightgreen"
).pack(side=tk.LEFT, padx=5, pady=5)

# FRAME 3: ORDER ACTIONS
order_frame = tk.LabelFrame(
    root,
    text="Order",
    bg="lightblue",
    bd=2,
    relief=tk.RAISED
)
order_frame.pack(side=tk.TOP, fill=tk.X, pady=10, padx=10)

tk.Button(
    order_frame, text="Calculate Total",
    command=calculate_total
).pack(side=tk.LEFT, padx=5, pady=5)

tk.Button(
    order_frame, text="Place Order",
    command=place_order
).pack(side=tk.LEFT, padx=5, pady=5)

tk.Button(
    order_frame, text="Clear Order",
    command=clear_order
).pack(side=tk.LEFT, padx=5, pady=5)

# DISPLAY AREA
display_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="wheat"
)
display_label.pack(side=tk.BOTTOM, pady=10)

# MAIN LOOP
root.mainloop()
