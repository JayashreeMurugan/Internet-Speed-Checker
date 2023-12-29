import pyspeedtest
from tkinter import*
#create the window
#create an object from the tk class
app=Tk()
app.configure(background="lightblue")
app.geometry("750x350")
app.resizable(0,0)
app.title("Internet speed checker App")

ping_speed=StringVar() 
down_speed=StringVar() 

#create a text and link entry label widgets
heading_text=Label(app,text="welcome to internet speed checker Application",font='Arial 14 bold',fg="grey",bg="lightblue")
web_url=Label(app,text="Enter web url",font='Arial 14 bold',fg='white',bg='lightblue')
ping_result=Label(app,text="Ping result",font='Arial 14 bold',fg='white',bg='lightblue')
download_result=Label(app,text="Download Result:",font='Arial 14 bold',fg='white',bg='lightblue')

#set a postion for this label widgets
heading_text.grid(row=0,column=1,pady=20)
web_url.grid(row=1,column=0,padx=10)
ping_result.grid(row=3,column=0,padx=10)
download_result.grid(row=4,column=0,padx=10,pady=10)

result1=Label(app,text=" ",textvariable=ping_speed,font='Arial 14 ',fg='white',bg='black')
result1.grid(row=3,column=1)

result2=Label(app,text=" ",textvariable=down_speed,font='Arial 14 ',fg='white',bg='black')
result2.grid(row=4,column=1)

#link entry box
url_entry=Entry(app,width=25,font="Arial 14 bold")
url_entry.grid(row=1,column=1)
#create a function
def speed_test():
    internet=pyspeedtest.SpeedTest(url_entry.get())
    ping_speed.set(internet.ping())
    down_speed.set(internet.download())
#create a entry
btn=Button(app,text="Check the internet speed here",font='Arial 14',fg='black',bg='grey',command=speed_test)
btn.grid(row=2,column=1,pady=10)

app.mainloop()