from tkinter import *

from PIL import ImageTk,Image
from tkinter import ttk
root=Tk()
root.title("Planet Encyclopedia")
root.geometry("500x500")
root.configure(background="lightblue")

mercury=ImageTk.PhotoImage(Image.open("mercury.jpg"))
venus=ImageTk.PhotoImage(Image.open("venus.jpg"))
earth=ImageTk.PhotoImage(Image.open("earth.jpg"))

label_planet=Label(root,text="Planet :" ,bg="lightblue")
label_planet_name=Label(root,font=("courier",18,"bold"),bg="lightblue")
label_planet_image=Label(root,bg="gold2",highlightthickness=5,borderwidth=2,relief=SOLID)
label_planet_gravity_radius=Label(root,font=("castellar"), bg="lightblue")
label_planet_info=Label(root,font=("courier",18,"bold"),bg="lightblue",wraplength=500)

planets=["Mercury","Venus","Earth"]
selected_val=StringVar()
dropdown=ttk.Combobox(root,values=planets,textvariable=selected_val)
dropdown.place(relx=0.5,rely=0.1,anchor=CENTER)

def PlanetInfo():
    planet=selected_val.get()
    if planet=="Mercury":
        label_planet_name["text"]="Mercury"
        label_planet_image["image"]=mercury
        label_planet_gravity_radius["text"]="gravity:3.7 m/s \n radius:2439.7 km"
        label_planet_info["text"]="Mercury is the smallest planet in our solar system. "
    elif planet=="Venus":
        label_planet_name["text"]="Venus"
        label_planet_image["image"]=venus
        label_planet_gravity_radius["text"]="gravity=8.87 m/s \n radius=6051.8 km"
        label_planet_info["text"]="Venus is the brightest object in the sky after the sun."
    elif planet=="Earth":
        label_planet_name["text"]="Earth"
        label_planet_image["image"]=earth
        label_planet_gravity_radius["text"]="gravity=9.807 m/s \n radius=6371 km"
        label_planet_info["text"]="Earth is the only planet known to have life and have liquid water"
        
    
    
btn=Button(root,text="Show PLanet Info",command=PlanetInfo)
btn.place(relx=0.5,rely=0.18,anchor=CENTER)

label_planet.place(relx=0.2, rely=0.1, anchor=CENTER)
label_planet_name.place(relx=0.5, rely=0.25, anchor=CENTER)
label_planet_image.place(relx=0.5, rely=0.5, anchor=CENTER)
label_planet_gravity_radius.place(relx=0.5, rely=0.8, anchor=CENTER)
label_planet_info.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()


