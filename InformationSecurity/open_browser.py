import webbrowser
from tkinter import *

root = Tk( )

root.title('Open browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

mygoogle = Button(root, text='Open Google', command=google).pack(pady=20)

root.mainloop()


stop = 1