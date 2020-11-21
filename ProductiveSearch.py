import webbrowser 
from tkinter import *


def searchYoutube():
    query = q.get()
    url = "https://www.youtube.com/results?search_query="+query+""   
    webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open_new(url)

# def pr(): 
#     query = q.get()
#     print(query)
#     q_var.set("")
   

root =Tk()
root.title("Productive Search")
root.geometry('500x300')
root.configure(bg="gray10")

# tstframe= Frame(root)
# tstframe.grid(row=0,column=0)



lbl = Label(root, text="Search Youtube :",font=('Impact',30,),fg="red2",bg="gray10" )
lbl.place(relx = 0.5,  
                   rely = 0.4, 
                   anchor = 'center') 
#lbl.grid(row=0,column=1,)

q_var=StringVar()

q= Entry(root,textvariable=q_var,justify=CENTER )
q.focus_force()
q.place(relx = 0.5,  rely = 0.6, anchor = 'center') 



bt= Button(root, text="Search",command=searchYoutube)
img= PhotoImage(file="D:/Coding GCB/Python (Building)/ProductiveSearch/res/do1.png")
bt.config(image=img)
bt.place(relx = 0.5,  rely = 0.7, anchor = 'center')
 

# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
root.mainloop()




 

 