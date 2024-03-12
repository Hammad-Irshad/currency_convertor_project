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

    curr1 = combo1.get()
    curr2 = combo2.get()
    amount = value.get()

    querystring = {"from":curr1,"to":curr2,"amount":amount}

# for symbol and curr2
    
    if curr2 == 'USD':
        symbol ='$'
        detail_curr2 ='United States Dollar'

    elif curr2 == 'EUR':
        symbol = '€'
        detail_curr2 = 'Euro'

    elif curr2 == 'PKR':
        symbol = 'Rs'
        detail_curr2 = 'Pakistan Rupee'

    elif curr2 == 'INR':
        symbol = '₹'
        detail_curr2 = 'Indian Rupee'
    
    elif curr2 == 'GBP':
        symbol = '£'
        detail_curr2 = 'British Pound Sterling'
    
    elif curr2 == 'JPY':
        symbol = '¥'
        detail_curr2 = 'Japanese Yen'
    
    elif curr2 == 'CNY':
        symbol = '¥'
        detail_curr2 = 'Chinese Yuan Renminbi'
    
    elif curr2 == 'CAD':
        symbol = 'C$'
        detail_curr2 = 'Canadian Dollar'
    
    elif curr2 == 'AUD':
        symbol = 'A$'
        detail_curr2 = 'Australian Dollar'
    
    elif curr2 == 'AED':
        symbol = 'د.إ'
        detail_curr2 = 'United Arab Emirates Dirham'
    
    elif curr2 == 'SAR':
        symbol = '﷼'
        detail_curr2 = 'Saudi Riyal'
    
    elif curr2 == 'QAR':
        symbol = '﷼'
        detail_curr2 = 'Qatari Riyal'
    
    elif curr2 == 'KWD':
        symbol = 'د.ك'
        detail_curr2 = 'Kuwaiti Dinar'
    
    elif curr2 == 'BHD':
        symbol = 'ب.د'
        detail_curr2 = 'Bahraini Dinar'

    elif curr2 == 'SGD':
        symbol = 'S$'
        detail_curr2 = 'Singapore Dollar'


# for curr1

    if curr1 == 'USD':
        detail_curr1 ='United States Dollar'

    elif curr1 == 'EUR':
        detail_curr1 = 'Euro'

    elif curr1 == 'PKR':
        detail_curr1 = 'Pakistan Rupee'

    elif curr1 == 'INR':
        detail_curr1 = 'Indian Rupee'
    
    elif curr1 == 'GBP':
        detail_curr1 = 'British Pound Sterling'
    
    elif curr1 == 'JPY':
        detail_curr1 = 'Japanese Yen'
    
    elif curr1 == 'CNY':
        detail_curr1 = 'Chinese Yuan Renminbi'
    
    elif curr1 == 'CAD':
        detail_curr1 = 'Canadian Dollar'
    
    elif curr1 == 'AUD':
        detail_curr1 = 'Australian Dollar'
    
    elif curr1 == 'AED':
        detail_curr1 = 'United Arab Emirates Dirham'
    
    elif curr1 == 'SAR':
        detail_curr1 = 'Saudi Riyal'
    
    elif curr1 == 'QAR':
        detail_curr1 = 'Qatari Riyal'
    
    elif curr1 == 'KWD':
        detail_curr1 = 'Kuwaiti Dinar'
    
    elif curr1 == 'BHD':
        detail_curr1 = 'Bahraini Dinar'

    elif curr1 == 'SGD':
        detail_curr1 = 'Singapore Dollar'





    headers = {
        "X-RapidAPI-Key": "b2f1c65b6dmsha9ba2116bb0f29ap180815jsnd7d9417231cf",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.request("GET",url, headers=headers, params=querystring)



    # print(response.text)

    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    formatted = symbol + " {:,.2f}".format(converted_amount)

    result['text'] = formatted
    

   
    

    detail_lable = Label(main, compound=CENTER, text=f"{detail_curr1} ==> {detail_curr2}", relief="flat",  anchor= CENTER, font=('Ivy 12 bold'), bg=cor0, fg=cor1)
    detail_lable.place(x=12, y=110)
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