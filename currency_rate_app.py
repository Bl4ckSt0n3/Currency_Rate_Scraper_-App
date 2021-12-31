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
    
    dollar_text = tk.Label(window, text=f"Dollar $   :  ", font=("Verdana", 10), bg="#4d0c34", fg="white")
    dollar_text.grid(row=1, column=0, sticky="W", pady=3)
    
    dollar_panel = tk.Label(window, text=f" ", font=("Verdana", 10), bg="#4d0c34", fg="white")
    dollar_panel.grid(row=1, column=1, sticky="W", pady=3)

    
    euro_text = tk.Label(window, text=f"Euro €    :  ", font=("Verdana", 10), bg="#4d0c34", fg="white")
    euro_text.grid(row=2, column=0, sticky="W", pady=3)
    
    euro_panel = tk.Label(window, text=f" ", font=("Verdana", 10), bg="#4d0c34", fg="white")
    euro_panel.grid(row=2, column=1, sticky="W", pady=3)
    
    date_panel = tk.Label(window, text=f" ", font=("Verdana", 10), bg="#4d0c34", fg="white")
    date_panel.grid(row=3, column=0, pady=3)
    window.resizable(True, True)
    window["background"]="#4d0c34"
    window.attributes("-alpha", 0.8)
    #window.wm_attributes('-transparentcolor', 'grey')
    window.title("Currency App")
    window.iconphoto(False, tk.PhotoImage(file='icon.png'))
    window.geometry('-2+2')
    window.overrideredirect(True)
    
    def quitter(e):
        window.quit()
        window.destroy()
        
    
    title_bar = tk.Frame(window,  bg="#4d0c34", relief="raised", bd=1)
    title_bar.grid(row=0, column=0, pady=3)
    close_button = tk.Button(window, text="Exit", command=window.destroy)
    close_label = tk.Label(window, text="x", font="Verdana, 9", bg="#4d0c34",  fg="white")
    close_label.grid(row=0, column=1, padx=(50, 0))
    close_label.bind("<Button-1>",quitter)
    

    
    

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
