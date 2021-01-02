import webbrowser 
import os
import platform
from tkinter import *

LIGHT_THEME = False

def toggle_light_theme(*args):
  

    global root, lbl, theme_toggle, LIGHT_THEME
    if not LIGHT_THEME:
        root['bg'] = 'white'
        lbl['bg'] = 'white'
        theme_toggle['bg'] = 'white'
        theme_toggle['fg'] = 'black'
        LIGHT_THEME = True
    else:
        root['bg'] = 'gray10'
        lbl['bg'] = 'gray10'
        theme_toggle['bg'] = 'gray10'
        theme_toggle['fg'] = 'white'
        LIGHT_THEME = False
    root.update()


def get_browser():
    if platform.system() == "Linux":
        return 'firefox', '/usr/bin/firefox'
    elif platform.system() == "Windows":
        return 'chrome', "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    else:
        raise OSError("Unfortunately, your OS is not supported.")


def searchYoutube():
    query = q.get()
    url = "https://www.youtube.com/results?search_query="+query+""
    browser = get_browser()
    if platform.system() == "Windows":
        webbrowser.register(browser[0],  
                        None,         
                        webbrowser.BackgroundBrowser(browser[1])),
    
    webbrowser.get(browser[0]).open_new(url)



root = Tk()
root.title("Productive Search")
root.geometry('500x300')
root.configure(bg="gray10")


lbl = Label(root, text="Search Youtube:", font=('impact' if platform.system() == "Windows" else "Arial Black", 30,),
            fg="red2", bg="gray10")
lbl.place(relx=0.5, rely=0.4, anchor='center')



q_var = StringVar()

q = Entry(root, textvariable=q_var, justify=CENTER)
q.focus_force()
q.place(relx=0.5,  rely=0.6, anchor='center')


bt = Button(root, text="Search", command=searchYoutube)
img = PhotoImage(file=os.path.abspath('res/do1.png'))
bt.config(image=img)
bt.place(relx=0.5,  rely=0.7, anchor='center')

theme_toggle = Button(root, text="Toggle Theme", bg="gray10", fg="white", activebackground="gray10",
                      activeforeground="white",
                      command=toggle_light_theme)
theme_toggle.place(relx=0.99, rely=0.99, anchor='se')
 

root.mainloop()




 

 