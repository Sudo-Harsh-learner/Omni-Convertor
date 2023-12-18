from resources import *

def clear_win():
    for widgets in app.winfo_children():
        widgets.destroy()
    menu()

def GridRes():
    for i in range(0,5):
        Grid.rowconfigure(app,i,weight=1)
        Grid.columnconfigure(app,i,weight=1)
    refresh()
# currency methods

def convert():
    global result_label
    refresh()
    try:
        data= requests.get(url).json()
        currencies = data['rates']
        fc = from_country.get()
        tc = to_country.get()
        value = float(amount.get())
        amt =   value * currencies[countries[tc]] / currencies[countries[fc]]
        amt = round(amt, 2)
        amount_show.delete(0,END)
        amount_show.insert(0,(amt))   
    except:
        messagebox.showerror(title="Error", message="Enter a valid number please.")

def bar():
    refresh()
    try:
        mixer.init()
        mixer.music.load('C:/Users/harsh/Desktop/Major Project/Project/Audio/Elevator Music.mp3')
        mixer.music.play()
        myBar = ttk.Progressbar(app,orient=HORIZONTAL, length=180, mode='determinate')
        myBar.grid(row=3,column=2, columnspan=2)
        for x in range(5):
            myBar['value'] += 20
            refresh()
            time.sleep(1)
        mixer.music.stop()   
        myBar.destroy()
        convert()
    except:
        convert()

def curr():
    clear_win()
    refresh()
    try:

        title = customtkinter.CTkLabel(master=app, text="The Currency Convertor", width=app._current_width,height=25, font=('Fixedsys',30),  bg_color="#806779")
        title.grid(row=0, column=1,rowspan=1, columnspan=4, sticky=N)
     
        # labels 
        from_label = customtkinter.CTkLabel(app,text="From",font=font, text_color="#709345", width=1)
        from_label.grid(row=1,column=0,columnspan=2)
        to_label = customtkinter.CTkLabel(app,text="To",font=font,  text_color="#509345", width=1)
        to_label.grid(row=1,column=4,columnspan=2)
        

        #Input drop down lists
        from_drop = customtkinter.CTkComboBox(app,variable=from_country, values=(countries.keys()), font=('Arial',12,'bold'), dropdown_font=('Arial',12,'bold'), fg_color="#4186ab", text_color=fg, button_color="#456543", button_hover_color="#987678",   dropdown_hover_color="#00FF00", dropdown_text_color=bg)
        from_drop.grid(row=2,column=0,columnspan=2)
        to_drop = customtkinter.CTkComboBox(app,variable=to_country, values=(countries.keys()), font=('Arial',12,'bold'), dropdown_font=('Arial',12,'bold'), fg_color="#4186ab", text_color=fg, button_color="#456543", button_hover_color="#987678",   dropdown_hover_color="#00FF00", dropdown_text_color=bg)
        to_drop.grid(row=2,column=4,columnspan=2)
       

        # Input 
        global amount, amount_show
        amount = customtkinter.CTkEntry(app,font=('Arial',20,'bold'), text_color="#000000", justify=CENTER, width=120,fg_color="#4186ab")
        amount.grid(row=3,column=1,columnspan=2)
        amount_show = customtkinter.CTkEntry(app,font=('Arial',20,'bold'), text_color="#000000", justify=CENTER, width=120,fg_color="#4186ab")
        amount_show.grid(row=3,column=3,columnspan=2)
       
        #Buttons
        convert_BT = customtkinter.CTkButton(app, text="Convert",font=('Arial',20,'bold'), text_color="#FFFFFF", fg_color="#709345", command=bar)
        convert_BT.grid(row=4,column=1)
        reset_BT = customtkinter.CTkButton(app, text="Reset",font=('Arial',20,'bold'), text_color="#FFFFFF", fg_color="#509345", command=reset)
        reset_BT.grid(row=4,column=4)
       
        refresh()
    except:
        messagebox.showerror(title="The Currency Convertor", message="Something went wrong!!")
# calculator methods 
def clear():
    global equation
    resultEntry.delete(0,END)
    equation = ""

def show(value):
    global i
    global equation
    equation += value
    resultEntry.insert(i,value)
    i += 1

def calculate():
    refresh()
    try:
        global equation
        result = ""
        result = eval(equation)
        clear()
        resultEntry.insert(0,result)
    except:
        messagebox.showerror(title="Error", message="Please clear the previous result before entring new equation!!!")

def reset():
    amount.delete(0,END)
    amount_show.delete(0,END)

def back():
     resultEntry.delete(resultEntry.index("end")-1)

def calc():
    clear_win()
    refresh()
    # calculator window
    global resultEntry
    resultEntry = customtkinter.CTkEntry(app, font=font,width=app._current_width, height=50,fg_color="#000000", border_color="#000000")
    resultEntry.grid(row=0,column=0, sticky=N, columnspan=app._current_width, rowspan=2)

    Button1 = customtkinter.CTkButton(app, command=clear, text="Clear", font=font,width=150,height=30, fg_color="#801a00", hover_color="#555489" )
    Button1.grid(row=4,column=3,columnspan=2)

    Button2 = customtkinter.CTkButton(app, command=lambda:show("%"),text="%", font=font, width=75, height=50, fg_color="#ff791a", hover_color="#555489" )
    Button2.grid(row=1,column=3,pady=10)

    Button3 = customtkinter.CTkButton(app, command=lambda:show("/"), text="/",font=font, width=75, height=50, fg_color="#7ab300", hover_color="#555489" )
    Button3.grid(row=1,column=4,pady=10)

    Button4 = customtkinter.CTkButton(app, command=lambda:show("*"),text="x", font=font, width=75, height=50, fg_color="#7ab300", hover_color="#555489" )
    Button4.grid(row=3,column=3)

    Button5 = customtkinter.CTkButton(app, command=lambda:show("7"), text="7", font=font, width=75, height=20, fg_color="#666885", hover_color="#000000" )
    Button5.grid(row=1,column=0)

    Button6 = customtkinter.CTkButton(app, command=lambda:show("8"),text="8", font=font, width=75, height=20, fg_color="#666885", hover_color="#000000" )
    Button6.grid(row=1,column=1)

    Button7 = customtkinter.CTkButton(app, command=lambda:show("9"),text="9",font=font, width=75, height=20, fg_color="#666885", hover_color="#000000" )
    Button7.grid(row=1,column=2)

    Button8 = customtkinter.CTkButton(app, command=lambda:show("+"),text="+", font=font, width=75, height=50, fg_color="#984555", hover_color="#555489" )
    Button8.grid(row=2,column=3)

    Button9 = customtkinter.CTkButton(app, command=lambda:show("4"),text="4", font=font, width=75, height=20, fg_color="#666885", hover_color="#000000" )
    Button9.grid(row=2,column=0)

    Button10 = customtkinter.CTkButton(app, command=lambda:show("5"),text="5", font=font, width=75, height=20, fg_color="#666885", hover_color="#000000" )
    Button10.grid(row=2,column=1)

    Button11 = customtkinter.CTkButton(app, command=lambda:show("6"),text="6", font=font, width=75, height=20, fg_color="#666885", hover_color="#000000" )
    Button11.grid(row=2,column=2)

    Button12 = customtkinter.CTkButton(app, command=lambda:show("-"),text="-", font=font, width=75, height=50, fg_color="#984555", hover_color="#555489" )
    Button12.grid(row=2,column=4)

    Button13 = customtkinter.CTkButton(app, command=lambda:show("0"),text="0", font=font, width=180, height=20, fg_color="#282a43", hover_color="#000000" )
    Button13.grid(row=4,column=0, columnspan=2)

    Button14 = customtkinter.CTkButton(app, command=lambda:show("1"),text="1", font=font, width=75, height=20, fg_color="#666885", hover_color="#000000" )
    Button14.grid(row=3,column=0)

    Button15 = customtkinter.CTkButton(app, command=lambda:show("2"),text="2", font=font, width=75, height=20, fg_color="#666885", hover_color="#000000" )
    Button15.grid(row=3,column=1)


    Button16 = customtkinter.CTkButton(app, command=lambda:show("3"),text="3", font=font, width=75, height=20, fg_color="#666885", hover_color="#000000" )
    Button16.grid(row=3,column=2)

    Button17 = customtkinter.CTkButton(app, command=lambda:show("."),text=".", font=font, width=75, height=20, fg_color="#ff5447", hover_color="#555489" )
    Button17.grid(row=4,column=2)

    Button18 = customtkinter.CTkButton(app, command=calculate,text="=", font=font, width=75, height=50, fg_color="#cc6d00", hover_color="#555489" )
    Button18.grid(row=3,column=4)

    Button19 = customtkinter.CTkButton(app, command=back,text="Backspace", font=font, width=app._current_width, height=25, fg_color="#cc6d00", hover_color="#555489" )
    Button19.grid(row=5,column=0, columnspan=5)

 # app or root methods
def menu():
    refresh()
    my_menu = Menu(app)
    app.config(menu=my_menu)
    tab_menu = Menu(app, tearoff=0)
    my_menu.add_cascade(label="Menu", menu=tab_menu)
    tab_menu.add_command(label="Home", command=home, font=("Fixedsys",14))
    tab_menu.add_command(label="Currency", command=curr, font=("Fixedsys",14))
    tab_menu.add_command(label="Calculator", command=calc, font=("Fixedsys",14))
    tab_menu.add_command(label="Language", command=lang, font=("Fixedsys",14))
    tab_menu.add_command(label="Maps", command=Maps, font=("Fixedsys",14))

    my_menu.add_cascade(label="Change Theme", command=changeTheme, font=("Fixedsys",14))
    
def changeTheme():
    refresh()
    global themeTxt
    if(themeTxt == "Light"):
        customtkinter.set_appearance_mode(themeTxt)
        themeTxt = "Dark"
        fg = "#FFFFFF"
        bg = "#000000"
    else:
        customtkinter.set_appearance_mode(themeTxt)
        themeTxt = "Light"
        fg = "#000000"
        bg = "#FFFFFF"
    
def refresh():
    app.update_idletasks()

def refreshWin(event):
    app.update_idletasks()

# home page methods
def DevInfo(num):
    clear_win()
    refresh()
    path1 = "C:/Users/harsh/Desktop/Major Project/Project/Images/stack.png"
    if(num==1):
        devName = "Harshdeep Singh"
        path = "C:/Users/harsh/Desktop/Major Project/Project/Images/code.png"
        job = "I did the coding for this project"
        s = (300,300)
    if(num==2):
         devName = "Ayush Pant"
         path = "C:/Users/harsh/Desktop/Major Project/Project/Images/artist.png"
         job = "I handeled Design, documentation"
         s = (250,300)
   
    iconImage = customtkinter.CTkImage(Image.open(path1), size=(25,25))
    nameDev1 = customtkinter.CTkLabel(master=app, text=devName, width=app._current_width,height=25, font=('Fixedsys',30),  bg_color="#806779")
    nameDev1.grid(row=0, column=1,rowspan=1, columnspan=4, sticky=N)
    imageDev1 = customtkinter.CTkImage(Image.open(path), size=s)
    img_lable1 = customtkinter.CTkLabel( app, image = imageDev1, text="")
    img_lable1.grid(row=1,column=2, columnspan=3)

    Frame = customtkinter.CTkFrame(app, fg_color="#9c8a6d")
    Frame.grid(row=1,column=1)
    Grid.rowconfigure(app,1,weight=1)
    Grid.columnconfigure(app,1,weight=1)


    Label = customtkinter.CTkLabel(Frame, text="", image=iconImage)
    Label.grid(row=0,column=0, sticky=NW,padx=5)
    Grid.rowconfigure(Frame,0,weight=1)
    Grid.columnconfigure(Frame,0,weight=1)

    Label = customtkinter.CTkLabel(Frame, text="Stack-underflow",width=Frame._current_width, bg_color="#806779", font=('Fixedsys',12,'bold'))
    Label.grid(row=0, column=1,rowspan=1, columnspan=2, sticky=N)
    Grid.columnconfigure(Frame,1,weight=1)
    Grid.columnconfigure(Frame,2,weight=1)

    textbox = customtkinter.CTkTextbox(Frame, width=40, height=30, corner_radius=5, activate_scrollbars=False)
    textbox.grid(row=2,column=0,sticky=W, pady=5,padx=5)
    textbox.insert("0.0", "Hi!")
    textbox.configure(state="disabled") 
    Grid.rowconfigure(Frame,2,weight=1)

    textbox = customtkinter.CTkTextbox(Frame, width=50, height=30, corner_radius=5, activate_scrollbars=False)
    textbox.grid(row=3,column=2,sticky=E,pady=5,padx=5)
    textbox.insert("0.0", "Yoo!")
    textbox.configure(state="disabled") 
    Grid.rowconfigure(Frame,3,weight=1)

    
    textbox = customtkinter.CTkTextbox(Frame, width=110, height=30, corner_radius=5, activate_scrollbars=False)
    textbox.grid(row=4,column=0,sticky=W,pady=5,padx=5)
    textbox.insert("0.0", "What's your role,")
    textbox.configure(state="disabled") 
    Grid.rowconfigure(Frame,4,weight=1)

    textbox = customtkinter.CTkTextbox(Frame, width=110, height=30, corner_radius=5, activate_scrollbars=False)
    textbox.grid(row=5,column=0,sticky=W,pady=5,padx=5)
    textbox.insert("0.0", "In this project?")
    textbox.configure(state="disabled") 
    Grid.rowconfigure(Frame,5,weight=1)

    textbox = customtkinter.CTkTextbox(Frame, width=120, height=50, corner_radius=5, activate_scrollbars=False)
    textbox.grid(row=6,column=2,sticky=E,pady=5,padx=5)
    textbox.insert("0.0", job)
    textbox.configure(state="disabled") 
    Grid.rowconfigure(Frame,6,weight=1)

    textbox = customtkinter.CTkTextbox(Frame, width=110, height=30, corner_radius=5, activate_scrollbars=False)
    textbox.grid(row=7,column=0,sticky=W,pady=5,padx=5)
    textbox.insert("0.0", "That's awesome")
    textbox.configure(state="disabled")
    Grid.rowconfigure(Frame,7,weight=1)



def home():
    refresh()
    clear_win()
    title = customtkinter.CTkLabel(master=app, text="The Omni Convertor", width=120,height=25, font=('Algerian',30))
    title.grid(row=0, column=2,rowspan=1, columnspan=5, sticky=N)

    bg1 = customtkinter.CTkImage(Image.open("C:/Users/harsh/Desktop/Major Project/Project/Images/img1.png"),size=(200,200))
    bg2 =  customtkinter.CTkImage(Image.open("C:/Users/harsh/Desktop/Major Project/Project/Images/img3.png"),size=(200,200))
    # dev1
    img_lable = customtkinter.CTkLabel( app, image = bg1, text="")
    img_lable.grid(row=1, column=1, padx=5,pady=2)
    
    name1 = customtkinter.CTkLabel(app,text="Harshdeep Singh", font=("terminal",14) )
    name1.grid(row=2,column=1, padx=5)
    bt1 = customtkinter.CTkButton(master=app,width=100, text="About me!", command=lambda:DevInfo(1),  hover=True)
    bt1.grid(row=3,column=1,padx=5)

    #dev 2
    img_lable = customtkinter.CTkLabel( app, image = bg2, text="")
    img_lable.grid(row=1, column=8)
    name1 = customtkinter.CTkLabel(app,text="Ayush Pant", font=("terminal",14) )
    name1.grid(row=2, column=8)
    bt2 = customtkinter.CTkButton(master=app,width=100, text="About me!", command=lambda:DevInfo(2),  hover=True)
    bt2.grid(row=3, column=8)
#language methods
def updateLabel():
    refresh()
    c1 = combo1.get()
    c2 = combo2.get()
    label1.configure(text=c1)
    label2.configure(text=c2)
    
    app.after(1000,updateLabel)

def clearText():
    refresh()
    f1.delete(1.0,END)
    f2.delete(1.0,END)

def translateText():
    refresh()
    try: 
        text = f1.get(1.0,END)
        transText = Translator(service_urls=['translate.googleapis.com'])
        transText = trans.translate(text, src=combo1.get(), dest=combo2.get())
        transText = transText.text
        f2.delete(1.0,END)
        f2.insert(END,transText)     
    except:
         messagebox.showerror(title="Language", message="Check your Internet Connection!!")


def lang():
    clear_win()
    refresh()
    global trans, lang, langList
    trans = Translator()
    lang = googletrans.LANGUAGES
    langList = list(lang.values())

    global combo1, combo2, label1, label2, text1,text2,f1,f2
    #left side
    combo1 = customtkinter.CTkComboBox(master=app,values=langList,width=170, font=('courier', 14),  text_color="#000000", fg_color="#FFFFFF")
    combo1.grid(row=1,column=0)
    combo1.set("English")
    label1 = customtkinter.CTkLabel(master=app,width=170, height=50, font=('segoe', 20, 'bold'), text=combo1.get(), bg_color="#574d4c")
    label1.grid(row=2,column=0)
    f1 = customtkinter.CTkTextbox(app,width=app._current_width-100,font=('Robote', 14),fg_color="grey",scrollbar_button_color="red", wrap=WORD, bg_color="grey", height=100)
    f1.grid(row=3,column=0, rowspan=2,columnspan=app._current_width) 


    #Right Side
    combo2 = customtkinter.CTkComboBox(master=app,values=langList,width=170, font=('courier', 14),  text_color="#000000", fg_color="#FFFFFF")
    combo2.grid(row=1,column=4)
    combo2.set("Select Language")
    label2 = customtkinter.CTkLabel(master=app,width=170, height=50, font=('segoe', 20, 'bold'), text="Spanish", bg_color="#574341")
    label2.grid(row=2,column=4)
    f2 = customtkinter.CTkTextbox(master=app, fg_color="black", scrollbar_button_color="blue",  width=app._current_width-100,font=('Robote', 14), wrap=WORD, height=100)
    f2.grid(row=5,column=0,columnspan=app._current_width)
    
    #Button
    buttonTranslate = customtkinter.CTkButton(master=app, text="Translate",font=('courier',14,'italic'), width=18, hover_color="#000000", command=translateText)
    buttonTranslate.grid(row=2,column=1, columnspan=1)
    buttonClear = customtkinter.CTkButton(master=app, text="Clear",font=('courier',14,'italic'), width=80, hover_color="#000000", command=clearText)
    buttonClear.grid(row=2,column=2,columnspan=1)

    updateLabel()

#Maps
def set_marker_event():
        current_position = map_widget.get_position()
        marker_list.append(map_widget.set_marker(current_position[0], current_position[1]))

def clear_marker_event():
        for marker in marker_list:
            marker.delete()
             

def change_map(event):
        refresh()
        if map_option_menu.get() == "OpenStreetMap":
            map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif map_option_menu.get() == "Google normal":
            map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=15)
        elif map_option_menu.get() == "Google satellite":
            map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=15)

def search_event(event=None):
        refresh()
        try:
            map_widget.set_address(entry.get())
        except:
             messagebox.showerror(title="The Omni Maps", message="Sorry!! Coudn't find your address")

def Maps():
    clear_win()
    refresh()
    try:
        global map_widget, map_option_menu, entry
        
        # ============ frame_left ============

        button_1 = customtkinter.CTkButton(master=app,text="Set Marker",command=set_marker_event)
        button_1.grid(row=1,column=0)

        button_2 = customtkinter.CTkButton(master=app,text="Clear Markers",command=clear_marker_event)
        button_2.grid(row=2,column=0)

        map_label = customtkinter.CTkLabel(app, text="Tile Server:", anchor="w")
        map_label.grid(row=3,column=0)
        map_option_menu = customtkinter.CTkOptionMenu(app,values=["OpenStreetMap", "Google normal", "Google satellite"],command=change_map)
        map_option_menu.grid(row=4,column=0)

      

    # ============ frame_right ============
        map_widget = TkinterMapView(app, corner_radius=0,width=app._current_width-100,height=app._current_height-50)
        map_widget.grid(row=1,column=3,rowspan=app._current_height, columnspan=app._current_width)

        entry = customtkinter.CTkEntry(master=app,placeholder_text="type address",width=200)
        entry.grid(row=0,column=1,pady=5,columnspan=3)
        entry.bind("<Return>", search_event)

        button_5 = customtkinter.CTkButton(app,text="Search",command=search_event)
        button_5.grid(row=0,column=4,pady=5,padx=10)

        # Set default values
        try:
            map_widget.set_address("Chandigarh University")
            map_option_menu.set("Google normal")
            map_widget.set_zoom(15)
            map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=15)
        except:
            messagebox.showerror(title="The Omni Maps", message="Check your Internet Connnection!!")
    except:
        messagebox.showerror(title="The Omni Maps", message="Something went wrong!!")


if __name__ == "__main__":
    # Basic structure of window
    app = customtkinter.CTk()
    app.geometry("750x400") 
    app.maxsize(width=1200, height=500)
    app.title("The Omni Convertor")
    app.iconbitmap('C:/Users/harsh/Desktop/Major Project/Project/Images/currency.ico')
    app.bind("<Button-1>",refreshWin)
    # Variables
    from_country = StringVar()
    result_txt = StringVar()
    to_country = StringVar()
    font = ('Arial',15,'bold')
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    i =0 
    equation = ""
    marker_list = []
    themeTxt = "Light"
    fg = "#000000"
    bg = "#FFFFFF"
    menu()
    home()
    GridRes()
    app.mainloop()