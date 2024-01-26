import tkinter as tk
from tkinter import PhotoImage, font


def calculate_interest():
    principal = int(principal_entry.get())
    rate = int(rate_entry.get())
    time = int(time_entry.get())

    interest = principal * rate * time / 100
    total_amount = principal + interest

    result_label.config(text=f"Your interest with {rate}% is: {interest}", fg="blue", font=("Arial", 10, "bold"))
    total_label.config(text=f"Total amount you have to pay after {time} month/year is: {total_amount}", fg="green",
                       font=("Arial", 10, "bold"))


# Create the main window
root = tk.Tk()
root.title("Interest Calculator")

# Load the background image and resize it
bg_image = PhotoImage(file="your_image_path.png")
bg_image = bg_image.subsample(2, 2)  # Adjust the subsample values to resize the image

# Set up a canvas to place the image
canvas = tk.Canvas(root, width=bg_image.width(), height=bg_image.height())
canvas.pack()

# Place the resized background image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

# Set a custom font for bold text
custom_font = font.Font(weight="bold")

# Create and place widgets with different colors
principal_label = tk.Label(root, text="Enter Principal (Amount):", bg="gray", fg="white", font=custom_font)
principal_label.pack()

principal_entry = tk.Entry(root)
principal_entry.pack()

rate_label = tk.Label(root, text="Enter Rate (without %):", bg="gray", fg="white", font=custom_font)
rate_label.pack()

rate_entry = tk.Entry(root)
rate_entry.pack()

time_label = tk.Label(root, text="Enter Time (month/year):", bg="gray", fg="white", font=custom_font)
time_label.pack()

time_entry = tk.Entry(root)
time_entry.pack()

# Set the button a bit below and with bold text
calculate_button = tk.Button(root, text="Calculate", command=calculate_interest, bg="orange", fg="white",
                             font=custom_font)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", fg="blue", bg="gray", font=custom_font)
result_label.pack()

total_label = tk.Label(root, text="", fg="green", bg="gray", font=custom_font)
total_label.pack()

# Start the main loop
root.mainloop()
