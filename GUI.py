# Imports
import json
from tkinter import *
from tkinter import messagebox
import webbrowser

# Global Variables
number = 0


def gui():

    # GUI portion
    window = Tk()
    window.title("Amazon Deal-scraper")

    # Setup GUI variables
    prime_ship = BooleanVar()
    star_req = IntVar()
    check_auto = IntVar()
    check_books = IntVar()
    check_cell = IntVar()
    check_computer = IntVar()
    check_electronics = IntVar()
    check_headphones = IntVar()
    check_home_improvement = IntVar()
    check_kitchen = IntVar()
    check_men_watch = IntVar()
    check_woman_watch = IntVar()
    check_beauty = IntVar()
    check_camera = IntVar()
    check_videogames = IntVar()
    check_toysgames = IntVar()
    check_moviestv = IntVar()
    check_pets = IntVar()
    check_women_jewelry = IntVar()
    check_men_shoes = IntVar()
    check_women_shoes = IntVar()
    check_men_clothing = IntVar()
    check_women_clothing = IntVar()
    check_men_fashion = IntVar()
    check_women_fashion = IntVar()

    # Nested get data / save data (called by lambda when "save button" is pressed)
    def getdata():
        # Set data for params (temp)
        params = {
            "version": 1,
            "viewIndex": 0,
            "presetId": "03EC2F2785A5C47E9F2C3BC593AF14AC",
            "departments": [],
            "prime": True,
            "sorting": "BY_CUSTOM_CRITERION",
            "starRating": 2,
        }

        # Data values for all the departments
        automotive_motorcycle = "15684181"
        books = "283155"
        cellphone_accessories = "2335752011"
        computer_accessories = "541966"
        electronics = "172282"
        headphones = "172541"
        home_improvement = "228013"
        kitchen = "284507"
        men_watches = "6358539011"
        women_watches = "6358543011"
        beauty = "3760911"
        camera = "502394"
        videogames = "468642"
        toysgames = "165793011"
        moviestv = "2625373011"
        pets = "2619533011"
        women_jewelry = "7192394011"
        men_shoes = "679255011"
        women_shoes = "679337011"
        men_clothing = "1040658"
        women_clothing = "1040660"
        men_fashion = "7147441011"
        women_fashion = "7147440011"











        global number
        number_bool = 0
        dept_bool = 0
        number = entry_field_1.get()

        def get_number():
            nonlocal number_bool
            try:
                if (len(number) < 11) or (len(number) > 16):
                    raise ValueError
                int(number)
                number_bool = 1
            except ValueError:
                messagebox.showerror("Invalid WhatsappID",
                                     "Whatsapp ID can only be Integers! 11-16 digits (no dashes!)")

        get_number()

        params["prime"] = prime_ship.get()
        params["starRating"] = star_req.get()


        def get_departments():

            nonlocal dept_bool
            if number_bool == 1:
                # Pull departments, user must have at least one selected
                if check_auto.get() == 1:
                    params["departments"].append(automotive_motorcycle)
                if check_books.get() == 1:
                    params["departments"].append(books)
                if check_cell.get() == 1:
                    params["departments"].append(cellphone_accessories)
                if check_computer.get() == 1:
                    params["departments"].append(computer_accessories)
                if check_electronics.get() == 1:
                    params["departments"].append(electronics)
                if check_headphones.get() == 1:
                    params["departments"].append(headphones)
                if check_home_improvement.get() == 1:
                    params["departments"].append(home_improvement)
                if check_kitchen.get() == 1:
                    params["departments"].append(kitchen)
                if check_men_watch.get() == 1:
                    params["departments"].append(men_watches)
                if check_woman_watch.get() == 1:
                    params["departments"].append(women_watches)
                if check_beauty.get() == 1:
                    params["departments"].append(beauty)
                if check_camera.get() == 1:
                    params["departments"].append(camera)
                if check_videogames.get() == 1:
                    params["departments"].append(videogames)
                if check_toysgames.get() == 1:
                    params["departments"].append(toysgames)
                if check_moviestv.get() == 1:
                    params["departments"].append(moviestv)
                if check_pets.get() == 1:
                    params["departments"].append(pets)
                if check_women_jewelry.get() == 1:
                    params["departments"].append(women_jewelry)
                if check_men_shoes.get() == 1:
                    params["departments"].append(men_shoes)
                if check_women_shoes.get() == 1:
                    params["departments"].append(women_shoes)
                if check_men_clothing.get() == 1:
                    params["departments"].append(men_clothing)
                if check_women_clothing.get() == 1:
                    params["departments"].append(women_clothing)
                if check_men_fashion.get() == 1:
                    params["departments"].append(men_fashion)
                if check_women_fashion.get() == 1:
                    params["departments"].append(women_fashion)
                try:
                    if len(params["departments"]) > 5:
                        raise ValueError
                    else:
                        dept_bool = 1
                except ValueError:
                    messagebox.showerror("Invalid Dept number", "Must select less than 5 departments")


        get_departments()

        if (number_bool == 1) and (dept_bool == 1):
            # Convert dictionary to json
            params_json = json.dumps(params, indent=4)

            # Write json to params.json
            with open("params.json", "w") as outfile:
                outfile.write(params_json)
            with open("number.txt", "w") as number_file:
                number_file.write(number)
            window.destroy()

    # Create labels/buttons
    var = StringVar()
    label = Label(window, textvariable=var, relief=RAISED, bg="grey", fg="white", font=("Arial", 10))
    label.pack(expand=True, fill="both")
    var.set("This is the Amazon scraper tool, DealScraper!\n"
            "\n"
            "This app will send a message with the best 5 deals,"
            "including their price and a link to the item on Amazon Daily Deals"
            "\n"
            "\n"
            "\n"
            "\n"
            "Remember to log-in to whatsapp through your default browser before using:\n")

    labelb = Label(window, text="https://web.whatsapp.com/", relief=RAISED, bg="grey", fg="lightblue", font=("Arial", 10),
                   cursor="hand2")
    labelb.pack(expand=True, fill="both")
    labelb.bind("<Button-1>", lambda e: webbrowser.open_new_tab('https://web.whatsapp.com/') )


    var2 = StringVar()
    labelc = Label(window, textvariable=var2, relief=RAISED, bg="grey", fg="white", font=("Arial", 10))
    labelc.pack(expand=True, fill="both")
    var2.set(
            "\n"
             "\n"
            "This GUI will only appear until the first time you save preference settings.\n"
            "\n"
            "To reset your settings, delete the [params.json] and [number.txt] inside of the app local file directory"
            "\n"
            "\n"

            )

    # Enter WhatsAppID
    label2 = Label(window, text="Enter Whatsapp ID     (no dashes)    (include country code)   \
      (example-   19281231234)",
                   relief=RAISED, bg="grey", fg="white")
    label2.pack()
    entry_field_1 = Entry(window, width=60)
    entry_field_1.pack()

    # Prime? (radio group)
    label4 = Label(window, text="Prime Shipping?", relief=RAISED, bg="grey", fg="white")
    label4.pack()
    prime_ship.set(True)
    r1 = Radiobutton(window, text="No Prime shipping", variable=prime_ship, value=False)
    r2 = Radiobutton(window, text="Prime shipping", variable=prime_ship, value=True)
    r1.pack()
    r2.pack()

    # Stars (no requirement, 1+, 2+, 3+, 4+) (radio group)
    label5 = Label(window, text="Item Star Requirement", relief=RAISED, bg="grey", fg="white")
    label5.pack()
    star_req.set(4)
    Radiobutton(window, text="No Star Requirement", variable=star_req, value=0).pack()
    Radiobutton(window, text="1+ Stars", variable=star_req, value=1).pack()
    Radiobutton(window, text="2+ Stars", variable=star_req, value=2).pack()
    Radiobutton(window, text="3+ Stars", variable=star_req, value=3).pack()
    Radiobutton(window, text="4+ Stars", variable=star_req, value=4).pack()

    # Departments (check boxes)
    label6 = Label(window, text="Choose 5 or less Departments", relief=RAISED, bg="grey", fg="white")
    label6.pack()

    frame1 = Frame(window)
    frame1.pack()

    frame2 = Frame(window)
    frame2.pack()

    frame3 = Frame(window)
    frame3.pack()

    frame4 = Frame(window)
    frame4.pack()

    frame5 = Frame(window)
    frame5.pack()

    c1 = Checkbutton(frame1, text="Automotive", variable=check_auto)
    c2 = Checkbutton(frame1, text="Books", variable=check_books)
    c3 = Checkbutton(frame1, text="Cell Phones", variable=check_cell)
    c4 = Checkbutton(frame1, text="Computers", variable=check_computer)
    c5 = Checkbutton(frame1, text="Electronics", variable=check_electronics)
    c6 = Checkbutton(frame2, text="Headphones", variable=check_headphones)
    c7 = Checkbutton(frame2, text="Home Improvement", variable=check_home_improvement)
    c8 = Checkbutton(frame2, text="Kitchen", variable=check_kitchen)
    c9 = Checkbutton(frame2, text="Men's Watches", variable=check_men_watch)
    c10 = Checkbutton(frame2, text="Women's Watches", variable=check_woman_watch)
    c11 = Checkbutton(frame3, text="Beauty", variable=check_beauty)
    c12 = Checkbutton(frame3, text="Camera", variable=check_camera)
    c13 = Checkbutton(frame3, text="Video Games", variable=check_videogames)
    c14 = Checkbutton(frame3, text="Toys & Games", variable=check_toysgames)
    c15 = Checkbutton(frame3, text="Movies / TV", variable=check_moviestv)
    c16 = Checkbutton(frame4, text="Pet Supplies", variable=check_pets)
    c17 = Checkbutton(frame4, text="Women's Watches", variable=check_women_jewelry)
    c18 = Checkbutton(frame4, text="Women's Watches", variable=check_men_shoes)
    c19 = Checkbutton(frame4, text="Women's Watches", variable=check_women_shoes)
    c20 = Checkbutton(frame4, text="Men's Clothing", variable=check_men_clothing)
    c21 = Checkbutton(frame5, text="Women's Clothing", variable=check_women_clothing)
    c22 = Checkbutton(frame5, text="Men's Fashion", variable=check_men_fashion)
    c23 = Checkbutton(frame5, text="Women's Fashion", variable=check_women_fashion)
    c1.pack(side=LEFT)
    c2.pack(side=LEFT)
    c3.pack(side=LEFT)
    c4.pack(side=LEFT)
    c5.pack(side=LEFT)
    c6.pack(side=LEFT)
    c7.pack(side=LEFT)
    c8.pack(side=LEFT)
    c9.pack(side=LEFT)
    c10.pack(side=LEFT)
    c11.pack(side=LEFT)
    c12.pack(side=LEFT)
    c13.pack(side=LEFT)
    c14.pack(side=LEFT)
    c15.pack(side=LEFT)
    c16.pack(side=LEFT)
    c17.pack(side=LEFT)
    c18.pack(side=LEFT)
    c19.pack(side=LEFT)
    c20.pack(side=LEFT)
    c21.pack(side=LEFT)
    c22.pack(side=LEFT)
    c23.pack(side=LEFT)


    # Save button
    save_button = Button(window, text="Save Settings!", bg="grey", fg="white", command=lambda: getdata())
    save_button.pack()
    window.mainloop()