import tkinter as tk

#Functions
def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height*height)
    answer_label.config(text="BMI: \n {}".format(bmi))

# Make the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("600x600") #Size
root.configure(background="#262626")

# Height Label
my_title = tk.Label(root,
                    text="Height (Metres):", 
                    font=("Ariel",20),
                    bg='#262626',
                    fg='#ffffff')
my_title.place(x=10, y=10)

# Weight Label
my_title = tk.Label(root,
                    text="Weight (kg):", 
                    font=("Ariel",20),
                    bg='#262626',
                    fg='#ffffff')
my_title.place(x=10, y=100)

# Answer Label
answer_label = tk.Label(root,
                        text="BMI: ",
                        font=("Ariel",20),
                        bg='#262626',
                        fg='#ffffff')
answer_label.place(x=10, y=250)

# Height entry box
height_entry = tk.Entry(root,
                font=("Ariel",16))
height_entry.place(x= 10, y = 60)

# Weight entry box
weight_entry = tk.Entry(root,
                font=("Ariel",16))
weight_entry.place(x= 10, y = 150)

# Calculate Button
button = tk.Button(root,
                   text="Calculate",
                   font=("Ariel",10),
                   command=calculate_bmi)
button.place(x=10, y = 200)

# Start the event loop
root.mainloop()
