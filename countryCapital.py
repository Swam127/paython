from tkinter import *
import random

root=Tk()
root.title("Country and Capital")
root.geometry("500x500")

enter_country = Entry(root)
enter_country.place(relx=0.5,rely=0.2,anchor=CENTER)

enter_capital = Entry(root)
enter_capital.place(relx=0.6,rely=0.3,anchor=CENTER)


country_list = Label(root)
capital_list = Label(root)
country = Label(root)
capital = Label(root)

list1 = []
list2= []

def generate_country():
    country_name = enter_country.get()
    list1.append(country_name)
    country_list["text"] = "Country List: "+str(list1)
    
    capital_name = enter_capital.get()
    list2.append(capital_name)
    capital_list["text"] = "Capital List: "+str(list2)

def randomfunction():
    length = len(list1)
    random_no = random.randint(0, length)
    country1 = list1[random_no-1]
    country["text"] = "Random Country: "+str(country1)
    
    capital1 = list2[random_no-1]
    capital["text"] = "Random Capital: "+str(capital1)
    
add_country = Button(root, text="Add Country and Capital", command=generate_country)
full_result = Button(root, text="Get Random Country and Capital", command=randomfunction)

add_country.place(relx=0.5,rely=0.4,anchor=CENTER)
full_result.place(relx=0.6, rely=0.7,anchor=CENTER)
country_list.place(relx=0.5,rely=0.5,anchor=CENTER)
capital_list.place(relx=0.6,rely=0.6,anchor=CENTER)
country.place(relx=0.5,rely=0.8,anchor=CENTER)
capital.place(relx=0.6,rely=0.9,anchor=CENTER)

root.mainloop()