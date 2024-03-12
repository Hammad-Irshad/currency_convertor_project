from tkinter import Tk,ttk
from tkinter import *

from PIL import Image,ImageTk
import requests
import json

#colors
cor0 = "#FFFFFF"    # white
cor1 = "#333333"    # black
cor2 = "#EB5D51"    # red

window = Tk()

window.geometry('400x400')
window.title('convertor')
window.configure(bg=cor0)
window.resizable(height= False , width= False)



# frames


top = Frame(window, width= 400, height=60, bg=cor2)
top.grid(row=0, column=0)

main = Frame(window, width= 400, height=285, bg=cor0)
main.grid(row=1, column=0)


# convert function

def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    curr1 = combo1.get().upper()
    curr2 = combo2.get().upper()
    amount = value.get()

    # Check if the input is a valid number
    try:
        amount = float(amount)
    except ValueError:
        result['text'] = "Invalid input"
        return

    querystring = {"from":curr1,"to":curr2,"amount":amount}



    # Currency details
    currency_details = {
        'USD': {'symbol': '$', 'detail': 'United States Dollar'},
        'EUR': {'symbol': '€', 'detail': 'Euro'},
        'PKR': {'symbol': 'Rs', 'detail': 'Pakistan Rupee'},
        'INR': {'symbol': '₹', 'detail': 'Indian Rupee'},
        'GBP': {'symbol': '£', 'detail': 'British Pound Sterling'},
        'JPY': {'symbol': '¥', 'detail': 'Japanese Yen'},
        'CNY': {'symbol': '¥', 'detail': 'Chinese Yuan Renminbi'},
        'CAD': {'symbol': 'C$', 'detail': 'Canadian Dollar'},
        'AUD': {'symbol': 'A$', 'detail': 'Australian Dollar'},
        'AED': {'symbol': 'د.إ', 'detail': 'United Arab Emirates Dirham'},
        'SAR': {'symbol': '﷼', 'detail': 'Saudi Riyal'},
        'QAR': {'symbol': '﷼', 'detail': 'Qatari Riyal'},
        'KWD': {'symbol': 'د.ك', 'detail': 'Kuwaiti Dinar'},
        'BHD': {'symbol': 'ب.د', 'detail': 'Bahraini Dinar'},
        'SGD': {'symbol': 'S$', 'detail': 'Singapore Dollar'}
    }


    headers = {
        "X-RapidAPI-Key": "b2f1c65b6dmsha9ba2116bb0f29ap180815jsnd7d9417231cf",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.request("GET",url, headers=headers, params=querystring)



    # print(response.text)

    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    formatted = currency_details[curr2]['symbol'] + " {:,.2f}".format(converted_amount)

    result['text'] = formatted
    

   
    

    detail_lable = Label(main, compound=CENTER, text=" ", width=40,  anchor= CENTER, font=('Ivy 12 bold'), bg=cor0, fg=cor1)
    detail_lable['text'] = f"{currency_details[curr1]['detail']} ==> {currency_details[curr2]['detail']}"
    detail_lable.place(x=0, y=105)
    # print(converted_amount, formatted)



#top frame

icon = Image.open('image/currency_logo.png')
icon = icon.resize((40,40))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image=icon, compound=LEFT, text="Currency Convertor", height=5, padx=30, pady=30, anchor= CENTER, font=('Arial 16 bold'), bg=cor2, fg=cor1)
app_name.place(x=0,y=0)



#main frame
result = Label(main, compound=LEFT, text=" ", relief="solid", width=18, height=3, pady=7, anchor= CENTER, font=('Ivy 16 bold'), bg=cor0, fg=cor1)
result.place(x=70,y=10)

currency =['PKR', 'USD', 'INR', 'EUR', 'GBP', 'JPY', 'CNY', 'CAD', 'AUD', 'AED', 'SAR', 'QAR', 'KWD', 'BHD', 'SGD']


from_lable = Label(main, compound=LEFT, text="From", relief="flat", width=8, height=3, pady=0, anchor= NW, font=('Ivy 12 bold'), bg=cor0, fg=cor1)
from_lable.place(x=70,y=130)
combo1 = ttk.Combobox(main, width=7, justify=CENTER, font=("Ivy 12 bold"))
combo1['values'] = (currency)
combo1.place(x=70,y=155)

to_lable = Label(main, compound=LEFT, text="To", relief="flat", width=8, height=3, pady=0, anchor= NW, font=('Ivy 12 bold'), bg=cor0, fg=cor1)
to_lable.place(x=220,y=130)
combo2 = ttk.Combobox(main, width=7, justify=CENTER, font=("Ivy 12 bold"))
combo2['values'] = (currency)
combo2.place(x=220,y=155)

value = Entry(main, width=30, relief="solid", justify= CENTER, font= ("IVy 12 bold"))
value.place(x=50,y=190)

button = Button(main, text="Convert", width=20, height=2, padx=5, bg=cor2, fg=cor1, font=("IVy 12 bold"), command=convert)
button.place(x=70, y=220)




window.mainloop()