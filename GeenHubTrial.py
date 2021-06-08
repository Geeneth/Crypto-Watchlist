import webbrowser
import tkinter as tk
import requests
import os
import subprocess

def InternetSearch(search, prefix):
	global search_string
	search_string = search
	if prefix == "YouTube":
		prefix = "https://www.youtube.com/results?search_query="
	else:
		prefix = "https://www.google.com/search?q="

	search_string = search_string.lower()
	search_string = search_string.replace(" ", "+")

	search_string = prefix+search_string
	webbrowser.open(search_string)

#CRYPTO FUNCTIONS

def BTC():
	webbrowser.open("https://www.tradingview.com/chart/?symbol=COINBASE%3ABTCUSD")

def ETH():
	webbrowser.open("https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT")

def ADA():
	webbrowser.open("https://www.tradingview.com/chart/?symbol=KRAKEN%3AADAUSD")

def DOGE():
        webbrowser.open("https://www.tradingview.com/chart/?symbol=BITFINEX%3ADOGEUSD")

def VET():
        webbrowser.open("https://www.tradingview.com/chart/?symbol=BITFINEX%3AVETUSD")

def GET():
        webbrowser.open("https://www.tradingview.com/chart/?symbol=BITTREX%3AGETUSDT")

#APPS FUNCTIONS

def Reddit():
        webbrowser.open("https://www.reddit.com/r/CryptoCurrency/")
        webbrowser.open("https://www.reddit.com/r/SatoshiStreetBets/")
        webbrowser.open("https://www.reddit.com/r/CryptoMarkets/")

def Files():
        webbrowser.open(r"C://Users//Geeneth//Desktop//Docs and Txts//Crypto Research//") 

def Andrei():
	webbrowser.open("https://www.youtube.com/channel/UCGy7SkBjcIAgTiwkXEtPnYg")

def Watchlist():
	webbrowser.open("https://coin360.com/watchlist")


HEGIHT = 600
WIDTH = 600

root = tk.Tk()
root.title('Crypto')

canvas = tk.Canvas(root, height=HEGIHT, width=WIDTH, bg='red')
canvas.pack()

frame = tk.Frame(root, bd=10, bg='#1B1B1E')
frame.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')

#CHOICE
label = tk.Label(frame, text="GEENHUB",bg='#1B1B1E', fg='white',font='Helvetica 15 bold')
label.place(relx=0.16, rely=0, relwidth=0.65, relheight=0.15)

#BUTTONS
btcbutton = tk.Button(frame, text="Bitcoin", bg='#F7931A', command=BTC, fg='white', font='Helvetica 11 bold')
btcbutton.place(relx=0, rely=0.35, relwidth=0.2, relheight=0.1)

ethbutton = tk.Button(frame, text="Ethereum", bg='#3c3c3d', command=ETH, fg='white', font='Helvetica 11 bold')
ethbutton.place(relx=0.25, rely=0.35, relwidth=0.2, relheight=0.1)

adabutton = tk.Button(frame, text="Cardano", bg='#2a71d0', command=ADA, fg='white', font='Helvetica 11 bold')
adabutton.place(relx=0.5, rely=0.35, relwidth=0.2, relheight=0.1)

dogebutton = tk.Button(frame, text="Doge", bg='#e1b303', command=DOGE, fg='white', font='Helvetica 11 bold')
dogebutton.place(relx=0.75, rely=0.35, relwidth=0.2, relheight=0.1)

vetbutton = tk.Button(frame, text="VeChain", bg='#34a3f0', command=VET, fg='white', font='Helvetica 11 bold')
vetbutton.place(relx=0.25, rely=0.475, relwidth=0.2, relheight=0.1)

getbutton = tk.Button(frame, text="GET", bg='#04cc7c', command=GET, fg='white', font='Helvetica 11 bold')
getbutton.place(relx=0.5, rely=0.475, relwidth=0.2, relheight=0.1)

#INTERNET SEARCH

entry1 = tk.Entry(frame, bg='#ffffff', font=40, justify='left')
entry1.place(relx=0.125, rely=0.15, relwidth=0.75, relheight=0.05)

button = tk.Button(frame, text="YouTube Search", bg='#c4302b', command=lambda: InternetSearch(entry1.get(), "YouTube"), fg='white', font='Helvetica 11 bold')
button.place(relx=0.225, rely=0.225, relwidth=0.25, relheight=0.05)

#entry2 = tk.Entry(frame, bg='#FFC1C2', font=40, justify='center')
#entry2.place(relx=0, rely=0.2, relwidth=0.5, relheight=0.05)

button1 = tk.Button(frame, text="Google Search", bg='#4285F4', command=lambda: InternetSearch(entry1.get(), "Google"), fg='white', font='Helvetica 11 bold')
button1.place(relx=0.525, rely=0.225, relwidth=0.25, relheight=0.05)

#APPS

redditbutton = tk.Button(frame, text="Reddit", bg='#FF4500', command=Reddit, fg='white', font='Helvetica 11 bold')
redditbutton.place(relx=0, rely=0.65, relwidth=0.2, relheight=0.1)

filesbutton = tk.Button(frame, text="Crypto Files", bg='#2A2280', command=Files, fg='white', font='Helvetica 11 bold')
filesbutton.place(relx=0.25, rely=0.65, relwidth=0.2, relheight=0.1)

andreibutton = tk.Button(frame, text="Andrei Jikh", bg='#c4302b', command=Andrei, fg='white', font='Helvetica 11 bold')
andreibutton.place(relx=0.5, rely=0.65, relwidth=0.2, relheight=0.1)

snippingbutton = tk.Button(frame, text="Watchlist", bg='#5db550', command=Watchlist, fg='white', font='Helvetica 11 bold')
snippingbutton.place(relx=0.75, rely=0.65, relwidth=0.2, relheight=0.1)

root.mainloop()
