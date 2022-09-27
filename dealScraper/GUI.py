# Imports
import json
from tkinter import *
from tkinter import messagebox

# Global Variables
number = 0


def gui():

    # GUI portion
    window = Tk()
    window.title("Scraper GUI")

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
                try:
                    if len(params["departments"]) > 5:
                        raise ValueError
                    else:
                        dept_bool = 1
                except ValueError:
                    messagebox.showerror("Invalid Dept number", "must have less than 5 departments")

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
    label = Label(window, textvariable=var, relief=RAISED, bg="grey", fg="white")
    label.pack()
    var.set("This is the Amazon scraper tool, DealScraper!"
            "This GUI will only appear until the first time you save preference settings.\n"
            "\n"
            "Save your settings using the radio buttons and check boxes\n"
            "\n"
            "Hit 'Save Settings!' to save your deal preferences locally\n"
            "\n"
            "To reset your settings, simply delete the params.json and/or number.txt inside of the local directory"
            "\n"
            "---------------------"
            "\n"
            "This app will send a message with the best 5 deals,"
            "including their price and a link to the item on Amazon Daily Deals"
            "\n"
            "---------------------"
            "\n"
            )

    # Enter WhatsAppID
    label2 = Label(window, text="Enter Whatsapp ID (no dashes; include country code (ex 19281231234)",
                   relief=RAISED, bg="grey", fg="white")
    label2.pack()
    entry_field_1 = Entry(window, width=60)
    entry_field_1.pack()

    # Prime? (radio group)
    label4 = Label(window, text="Prime Membership", relief=RAISED, bg="grey", fg="white")
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
    c1 = Checkbutton(window, text="Automotive", variable=check_auto)
    c2 = Checkbutton(window, text="Books", variable=check_books)
    c3 = Checkbutton(window, text="Cell Phones", variable=check_cell)
    c4 = Checkbutton(window, text="Computers", variable=check_computer)
    c5 = Checkbutton(window, text="Electronics", variable=check_electronics)
    c6 = Checkbutton(window, text="Headphones", variable=check_headphones)
    c7 = Checkbutton(window, text="Home Improvement", variable=check_home_improvement)
    c8 = Checkbutton(window, text="Kitchen", variable=check_kitchen)
    c9 = Checkbutton(window, text="Men's Watches", variable=check_men_watch)
    c10 = Checkbutton(window, text="Women's Watches", variable=check_woman_watch)
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

    # Save button
    save_button = Button(window, text="Save Settings!", bg="grey", fg="white", command=lambda: getdata())
    save_button.pack()
    window.mainloop()