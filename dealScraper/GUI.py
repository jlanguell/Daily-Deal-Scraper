import json
from tkinter import *
from tkinter import messagebox

number = 0

def gui():
    # GUI portion
    window = Tk()
    window.title("Scraper GUI")

    #setup variables
    primeship = BooleanVar()
    starreq = IntVar()
    checkauto = IntVar()
    checkbooks = IntVar()
    checkcell = IntVar()
    checkcomputer = IntVar()
    checkelectronics = IntVar()
    checkheadphones = IntVar()
    checkhomeimprovement = IntVar()
    checkkitchen = IntVar()
    checkmenwatch = IntVar()
    checkwomanwatch = IntVar()

    # nested get data / save data (called by lambda when "save button" is pressed"
    def getdata():

        # set data for params (temp)
        params = {
            "version": 1,
            "viewIndex": 0,
            "presetId": "03EC2F2785A5C47E9F2C3BC593AF14AC",
            "departments": [],
            "prime": True,
            "sorting": "BY_CUSTOM_CRITERION",
            "starRating": 2,
        }

        # data values for all the departments
        automotivemotorcycle = "15684181"
        books = "283155"
        cellphonescccessories = "2335752011"
        computersaccessories = "541966"
        electronics = "172282"
        headphones = "172541"
        homeimprovement = "228013"
        kitchen = "284507"
        menwatches = "6358539011"
        womenwatches = "6358543011"

        global number
        numberisgood = 0
        number = entryfield1.get()

        def getNumber():
            nonlocal numberisgood
            try:
                int(number)
                numberisgood = 1
            except ValueError:
                messagebox.showerror("Invalid WhatsappID", "Whatsapp ID can only be Integers! (no dashes!)")

        getNumber()
        print(number)


        if (numberisgood == 1):

            params["prime"] = primeship.get()
            params["starRating"] = starreq.get()

            # pull departments, user must have at least one selected
            if checkauto.get() == 1:
                params["departments"].append(automotivemotorcycle)
            if checkbooks.get() == 1:
                params["departments"].append(books)
            if checkcell.get() == 1:
                params["departments"].append(cellphonescccessories)
            if checkcomputer.get() == 1:
                params["departments"].append(computersaccessories)
            if checkelectronics.get() == 1:
                params["departments"].append(electronics)
            if checkheadphones.get() == 1:
                params["departments"].append(headphones)
            if checkhomeimprovement.get() == 1:
                params["departments"].append(homeimprovement)
            if checkkitchen.get() == 1:
                params["departments"].append(kitchen)
            if checkmenwatch.get() == 1:
                params["departments"].append(menwatches)
            if checkwomanwatch.get() == 1:
                params["departments"].append(womenwatches)
            # convert dictionary to json
            params_json = json.dumps(params, indent=4)
            # Write json to params.json
            with open("params.json", "w") as outfile:
                outfile.write(params_json)
            with open("number.txt", "w") as number_file:
                number_file.write(number)
            window.destroy()


    #setup labels/buttons
    var = StringVar()
    label = Label(window, textvariable=var, relief=RAISED, bg="grey", fg="white")
    label.pack()
    var.set("This is the Amazon scraper tool!  This GUI will only appear until the first time you save settings.\n"
            "\n"
            "Save your settings using the radio buttons and check boxes\n"
            "\n"
            "Hit 'Save settings' to save your scraper settings\n"
            "\n"
            "to reset your settings, simply delete the params.json inside of the program folder"
            "\n"
            "---------------------"
            "\n"
            )
    # enter whatsappID
    label2 = Label(window, text="Enter Whatsapp ID (no dashes, including country code (ex 19281231234)", relief=RAISED, bg="grey", fg="white")
    label2.pack()
    entryfield1 = Entry(window, width=60)
    entryfield1.pack()
    # prime? (radio group)
    label4 = Label(window, text="Prime?", relief=RAISED, bg="grey", fg="white")
    label4.pack()
    primeship.set(True)
    r1 = Radiobutton(window, text="No Prime shipping", variable=primeship, value=False)
    r2 = Radiobutton(window, text="Prime shipping", variable=primeship, value=True)
    r1.pack()
    r2.pack()
    # stars (no requirement, 1+, 2+, 3+, 4+) (radio group)
    label5 = Label(window, text="Star Requirement?", relief=RAISED, bg="grey", fg="white")
    label5.pack()
    starreq.set(4)
    Radiobutton(window, text="No Star Requirement", variable=starreq, value=0).pack()
    Radiobutton(window, text="1+ Stars", variable=starreq, value=1).pack()
    Radiobutton(window, text="2+ Stars", variable=starreq, value=2).pack()
    Radiobutton(window, text="3+ Stars", variable=starreq, value=3).pack()
    Radiobutton(window, text="4+ Stars", variable=starreq, value=4).pack()
    # departments (check boxes)
    label6 = Label(window, text="Choose Departments", relief=RAISED, bg="grey", fg="white")
    label6.pack()
    c1 = Checkbutton(window, text="Automotive", variable=checkauto)
    c2 = Checkbutton(window, text="Books", variable=checkbooks)
    c3 = Checkbutton(window, text="Cell Phones", variable=checkcell)
    c4 = Checkbutton(window, text="Computers", variable=checkcomputer)
    c5 = Checkbutton(window, text="Electronics", variable=checkelectronics)
    c6 = Checkbutton(window, text="Headphones", variable=checkheadphones)
    c7 = Checkbutton(window, text="Home Improvement", variable=checkhomeimprovement)
    c8 = Checkbutton(window, text="Kitchen", variable=checkkitchen)
    c9 = Checkbutton(window, text="Men's Watches", variable=checkmenwatch)
    c10 = Checkbutton(window, text="Women's Watches", variable=checkwomanwatch)
    c1.pack()
    c2.pack()
    c3.pack()
    c4.pack()
    c5.pack()
    c6.pack()
    c7.pack()
    c8.pack()
    c9.pack()
    c10.pack()
    # save button
    savebutton = Button(window, text="Save Settings!", bg="grey", fg="white", command=lambda: getdata())
    savebutton.pack()
    window.mainloop()