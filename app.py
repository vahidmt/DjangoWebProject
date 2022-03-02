import requests
from tkinter import *

url = "http://127.0.0.1:8000/api/posts"
res = requests.get(url)
data = res.json()


window = Tk()
window.geometry('800x600')
window.title("وبلاگ")
La = Label(window, text="My weblog")
La.grid(row=0, column=1)
bt = 1
la = 2
for i in range(100000000):
    try:
        def show():
            app=Tk()
            app.mainloop()
        da = data[i]
        if da:
            bt += 2
            la += 2
            title = (da['title'])
            url = (da['text_blog'])
            Bt = Label(window, text=title)
            La = Label(window, text=url)
            Bt.grid(row=bt, column=0)
            La.grid(row=la, column=0)
    except IndexError:
        break

window.mainloop()
