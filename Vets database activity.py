# importing libraries
from guizero import *
import sqlite3
    
# Create an app and makes a window
app = App(title='myVET Database', width=500, height=500)


#function which is called when the submit button on the front app is pressed 
def open_customer_window():

   #customer window code and widgets
    customer_window = Window(app, title="Add new customer")
    Text(customer_window, text="Add a customer")
    
    form_box = Box(customer_window, layout = "grid", align = "left")  #created a box with grid layout for making the form easier
    firstName_lbl = Text(form_box, text="First name: ", grid = [0,0])
    firstName = TextBox(form_box, text="Type here", grid = [1,0], width=15)

    secondName_lbl = Text(form_box, text = "Second name: ", grid = [0,1])
    secondName = TextBox(form_box, text = "Type here", grid = [1,1], width=15)

    address1_lbl = Text(form_box, text = "Address 1: ", grid = [0,2])
    address_1 = TextBox(form_box, text = "Type here", grid = [1,2], width=15)

    address2_lbl = Text(form_box, text = "Address 2: ", grid = [0,3])
    address_2 = TextBox(form_box, text = "Type here", grid = [1,3], width=15)

    phone_lbl = Text(form_box, text = "Phone: ", grid = [0,4])
    customer_phone = TextBox(form_box, text = "Type here", grid = [1,4], width=15)
    
    PushButton(customer_window, text='Add Customer', align="bottom",command=add_new_customer, args=[customer_window,form_box,firstName,secondName,address_1,address_2,customer_phone])
    PushButton(customer_window, text='Cancel', align="bottom", command=cancel_customer_window, args=[customer_window])

#end of open_customer_window function

# Hides the customer window if the cancel button pressed
def cancel_customer_window(customer_window):
    customer_window.hide()
# End of cancel customer window function


# Function run when Add Customer button pressed
def add_new_customer(customer_window,form_box,firstName,secondName,address_1,address_2,customer_phone):
    first_name = firstName.value
    second_name = secondName.value
    address1 = address_1.value
    address2 = address_2.value
    phone = customer_phone.value
    
    with sqlite3.connect("vets") as db:
        cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS owner (firstName text NOT NULL, secondName text NOT NULL, address1 text NOT NULL, address2 text NOT NULL, phone text NOT NULL );""")

    first_name.isalpha()  # .isalpha() will check if all the content of the string is part of the alphabet (it will not accept spaces)
    second_name.isalpha()
    phone.isdigit()       # .isdigit() will check if the contents of the string are all integers

    if first_name.isalpha() == True and second_name.isalpha() == True and phone.isdigit() == True:   # data will only be added to the database if the information is entered correctly

        cursor.execute(("""INSERT INTO owner VALUES(?,?,?,?,?)"""),(first_name, second_name, address1, address2, phone))

        db.commit()

        print("\nOwner added successfully")
        
        cursor.execute("SELECT * from owner")
        print(cursor.fetchall())

    else:
        print("\nSome information entered isn't valid. Please check and try again")
    
    open_customer_window() # this will refresh the entry form to be ready to enter another person
    
  #THIS WAS FOR TESTING   
  #print(first_name)
  #print(second_name)
  #print(address1)
  #print(address2)
  #print(phone)
    customer_window.hide()
# End of cancel customer window function




# Creates the main app page with some widgets
text = Text(app, text="myVET Database")
submit = PushButton(app, text='Add new customer', command=open_customer_window)



#displays the app
app.display()
