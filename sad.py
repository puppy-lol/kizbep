from tkinter import *
import random

root = Tk()
root.title("country capitals")
root.geometry("400x400")

enter_name = Entry(root)
enter_name2 = Entry(root)
enter_name.place(relx = 0.5, rely = 0.1, anchor = CENTER)
enter_name2.place(relx = 0.5, rely = 0.2, anchor = CENTER)

country_name_list = Label(root)
city_name_list = Label(root)
random_country = Label(root)
random_city = Label(root)

list1 = []
list2 = []
def addcountry():
    country_name = enter_name.get()
    list1.append(country_name)
    city_name = enter_name2.get()
    list2.append(city_name)
    country_name_list["text"] = "countries: " + str(list1)
    city_name_list["text"] = "capitals: " + str(list2)

def random_number():
    length = len(list1)
    length2 = len(list2)
    random_no =  random.randint(0, length-1)
    generated_random_number = list1[random_no]
    random_country["text"] = "Random country: " + str(generated_random_number)
    random_no2 = random.randint(0, length2-1)
    generated_random_number2 = list2[random_no]
    random_city["text"] = "Random capital: " + str(generated_random_number2)

btn = Button(root, text="Display the locations", command = addcountry)
btn.place(relx = 0.5, rely = 0.3, anchor = CENTER)

country_name_list.place(relx = 0.5, rely = 0.4, anchor = CENTER)
city_name_list.place(relx = 0.5, rely = 0.5, anchor = CENTER)

btn1 = Button(root, text="display locations randomly ", command = random_number)
btn1.place(relx = 0.5, rely = 0.6, anchor = CENTER)

random_country.place(relx = 0.5, rely = 0.7, anchor = CENTER)
random_city.place(relx = 0.5, rely = 0.8, anchor = CENTER)

root.mainloop()