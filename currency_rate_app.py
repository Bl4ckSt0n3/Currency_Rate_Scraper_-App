import requests
from bs4 import BeautifulSoup
import tkinter as tk
from datetime import datetime


def get_current_data():

    _url = "https://www.sabah.com.tr/finans/doviz/doviz-kurlari"
    current_time = datetime.now()
    timeObj = current_time.strftime("%d-%b-%Y (%H:%M:%S)")
    try:
        request = requests.get(_url)
        soup = BeautifulSoup(request.content, "html.parser")
        table_dollar = soup.find('div', attrs={'id': 'divUSD'})
        table_euro = soup.find('div', attrs={'id': 'divEUR'})
        currency_data = dict()
        currency_data["date"] = timeObj
        
        for row in table_dollar.findAll('div', attrs={'id': 'USD_KAPANIS_DATA'}):
            currency_data["dollar_title"] = row.text
            
        for row_e in table_euro.findAll('div', attrs={'id': 'EUR_KAPANIS_DATA'}):
            currency_data["euro_title"] = row_e.text
            return currency_data

    except Exception as e:
        print(e)


def main():

    window = tk.Tk()
    # window.overrideredirect(True)
    
    dollar_text = tk.Label(window, text=f"Dollar $   :  ", font=("Verdana", 20), bg="grey", fg="white")
    dollar_text.grid(row=0, column=0, sticky="W", pady=3)
    
    dollar_panel = tk.Label(window, text=f" ", font=("Verdana", 20), bg="grey", fg="white")
    dollar_panel.grid(row=0, column=1, sticky="W", pady=3)

    
    euro_text = tk.Label(window, text=f"Euro €    :  ", font=("Verdana", 20), bg="grey", fg="white")
    euro_text.grid(row=1, column=0, sticky="W", pady=3)
    
    euro_panel = tk.Label(window, text=f" ", font=("Verdana", 20), bg="grey", fg="white")
    euro_panel.grid(row=1, column=1, sticky="W", pady=3)
    
    date_panel = tk.Label(window, text=f" ", font=("Verdana", 20), bg="grey", fg="white")
    date_panel.grid(row=2, column=0, pady=3)

    window.resizable(False, False)
    window["background"]="grey"
    window.attributes("-alpha", 0.8)
    window.wm_attributes('-transparentcolor', 'grey')
    # window.wm_attributes('-fullscreen', 'True')
    window.title("Currency App")
    window.iconphoto(False, tk.PhotoImage(file='icon.png'))

    def update():
        panel_text = get_current_data()
        dollar_panel["text"] = panel_text["dollar_title"] + " ₺"
        euro_panel["text"] = panel_text["euro_title"] + " ₺"
        date_panel["text"] = panel_text["date"]
        window.after(25000, update)
    update()
    window.mainloop()
        
if __name__ == "__main__":
    # update()
    # window.mainloop()
    main()
