from tkinter import *   #type: ignore

windows = Tk()
windows.title("Miles To KM Converter")
windows.config(padx=30, pady=30)

def calculate_km():
    miles = float(miles_input.get())
    km = round(miles*1.609)
    kilometer_result.config(text=km)

miles_input = Entry(width= 7)
miles_input.grid(row= 0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row= 0, column= 2)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row= 1, column= 0)

kilometer_result = Label(text="0")
kilometer_result.grid(row= 1, column= 1)

kilometer_label = Label(text="Km")
kilometer_label.grid(row= 1, column= 2)

calculate_button = Button(text="calculate", command=calculate_km)
calculate_button.grid(row= 2, column= 1)

windows.mainloop()