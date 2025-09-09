from tkinter import *
from tkinter import messagebox
import pandas
import os
from datetime import datetime
import csv
import statistics
import matplotlib.pyplot  as plt

RED= "#DC143C"

#-----------------------heart rate csv file------------------------------------
if not os.path.exists("heart_rate.csv"):
    data = pandas.DataFrame(columns=["Timestamp","Heart rate"])
    data.to_csv("heart_rate.csv", index=False)

def get_data():

    with open("heart_rate.csv","r") as data_file:   #load heart rate data from csv and return it as a list
        reader = csv.DictReader(data_file)
        data_list_of_dicts = list(reader)   #each row becomes a dict with resp header

    heart_rates = [int(row["Heart rate"]) for row in data_list_of_dicts]
    return heart_rates,data_list_of_dicts

#-----------------------heart tracker functions ------------------------------------

def add():
    try:
        heart_rate = int(heart_rate_entry.get())

    except ValueError:
        messagebox.showerror(title="Error",message="Enter valid number")
        heart_rate_entry.delete(0, END)
        return

    if heart_rate > 100:
        messagebox.showwarning(title="High Heart Rate",message= f"Heart rate {heart_rate} bpm is high!"
                                                  f" Consider consulting a doctor if feeling unwell.")

    if heart_rate < 60:
        messagebox.showwarning(title="Low Heart Rate",message= f"Heart rate {heart_rate} bpm is low!"
                                                  f" Consider consulting a doctor if feeling unwell.")

    heart_rate_entry.delete(0,END)
    now = datetime.now()
    timestamp = now.strftime("%a %b %d %Y at %I:%M %p")

    with open("heart_rate.csv","a") as data_file:
        data_file.write(f"{timestamp},{heart_rate}\n")

    result_label.config(text=f"Added: {heart_rate} bpm {timestamp}",wraplength=250)

def average():
    heart_rates, _ = get_data()
    if len(heart_rates) ==0 :
        messagebox.showinfo(title= "Error",message="No heart rate data found")
        return #exit

    avg = round(statistics.mean(heart_rates),2)
    if 60<=avg<=100:
        result_label.config(text=f"The average heart rate is {avg} bpm (normal)",wraplength=250)

    else:
        result_label.config(text=f"The average heart rate is {avg} bpm (Out of range!)",wraplength=250)
        messagebox.showwarning(title="Warning",message=f"The average heart rate is {avg} bpm (Out of range!)")

def maximum():
    heart_rates,data_list_of_dicts = get_data()
    maximum_rate = max(heart_rates)

    if len(heart_rates) ==0 :
        messagebox.showinfo(title= "Error",message="No heart rate data found")
        return #exit

    maximum_index = heart_rates.index(maximum_rate)
    timestamp = data_list_of_dicts[maximum_index]["Timestamp"]

    result_label.config(text= f"The maximum heart rate is {maximum_rate} recorded at {timestamp}",wraplength=250)

def minimum():
    heart_rates,data_list_of_dicts = get_data()
    minimum_rate = min(heart_rates)

    if len(heart_rates) ==0 :
        messagebox.showinfo(title= "Error",message="No heart rate data found")
        return #exit

    minimum_index = heart_rates.index(minimum_rate)
    timestamp = data_list_of_dicts[minimum_index]["Timestamp"]

    result_label.config(text=f"The minimum heart rate is {minimum_rate} recorded at {timestamp}", wraplength=250)

def show_graph():
    heart_rates, data_list_of_dicts = get_data()

    if len(heart_rates) == 0:
        messagebox.showinfo(title="No Data", message="No heart rate data found")
        return

    # extract timestamps
    timestamps = [row["Timestamp"] for row in data_list_of_dicts]

    # show only last 20 entries to avoid clutter
    N = 20
    if len(timestamps) > N:
        timestamps = timestamps[-N:]  #slicing to take the last 20 entries
        heart_rates_to_plot = heart_rates[-N:]
    else:
        heart_rates_to_plot = heart_rates

    # create plot
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, heart_rates_to_plot, marker='o', linestyle='-', color='red')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Timestamp")
    plt.ylabel("Heart Rate (bpm)")
    plt.title("Heart Rate Over Time")
    plt.tight_layout()
    plt.show()


#-----------------UI INTERFACE-----------------------------
window = Tk()
window.title("The Heart Rate Tracker ")
window.config(padx=100,pady=100,bg=RED)

canvas = Canvas(width=232,height=220,bg=RED,highlightthickness=0)
heart_image = PhotoImage(file="heart.png")


canvas.create_image(116,110,image=heart_image)
canvas.grid(row=1,column=1)

#label
title_label = Label(text="Heart Rate Tracker",font=("Ariel",30,"bold"),bg=RED,fg="#FDEBD0")
title_label.grid(row=0,column=1,pady=5)

heart_rate_label = Label(text="Enter heart rate: ",font=("Ariel",13,"bold"),bg=RED,fg="#FDEBD0")
heart_rate_label.grid(row=2,column=0)

result_label = Label(text="",font=("Ariel",13,"bold"),bg=RED,fg="#FDEBD0")
result_label.grid(row=4,column=1,pady=20)


#entry
heart_rate_entry = Entry(width=35)
heart_rate_entry.focus()
heart_rate_entry.grid(row=2,column=1,pady=30)

#button
add_button = Button(text="Add heart rate",highlightthickness=0,command=add)
add_button.grid(row=2,column=2)

avg_button = Button(text="Average heart rate",highlightthickness=0,command=average)
avg_button.grid(row=3,column=0)

max_button = Button(text="Maximum heart rate",highlightthickness=0,command=maximum)
max_button.grid(row=3,column=1)

min_button = Button(text="Minimum heart rate",highlightthickness=0,command=minimum)
min_button.grid(row=3,column=2)

graph_button = Button(text="Show Graph",highlightthickness=0,command=show_graph)
graph_button.grid(row=5,column=1)



window.mainloop()
