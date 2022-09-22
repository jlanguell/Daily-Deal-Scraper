# Daily-Deal-Scraper  

Python-based web-scraper for auto-reporting Amazon daily deals

## Installation & Run  

- Prior to running the application on your PC, you need to go to your browser and login to your WhatsApp account via https://web.whatsapp.com/.  

This is made easy, and can be done by pulling up a QR code scanner on your phone's WhatsApp account, and scanning the available QR code in your browser. This registers the PC as a device associated with your WhatsApp account for future use with dealScraper.  

If you have git installed on your computer: 

- Clone the git repository to a local directory on your computer with the command line:    

```bash
git clone https://github.com/jlanguell/dealScraper.git
```  

- Use command line to navigate to the folder that contains 'requirements.txt'  

- Pip install the requirements.txt file with  

```bash
pip install -r requirements.txt
```  

- Prior to running the program, make sure that if you have a multiple-monitor setup, your CMD terminal and any open browsers exist on the same display. There is some issue with the pywhatkit module that does not allow the application to work when these two entities are on different monitors.  

- Run the program by typing:  
```bash
python dealScraper.py
```  

- If necessary, use your python specific version, i.e.:
```bash
python3 dealScraper.py
```  

## Usage  

When the application runs the first time, it should open a simple GUI for you to enter the WhatsApp number you wish to text (11-16 integers with country code & area code, e.g. 17037737373). Then, you can select to filter deals by prime/no prime, an item star rating minimum, and by department. 

When you hit "Save Changes", a json file is created locally that stores your preferences and a text file that stores your phone number. Additionally, after the programs runs, a WhatsApp log is then created locally or appended to (if one already exists), that tracks information about every message that has been sent using the app.  

*NOTE:* After saving your preferences, the application will run without the preference GUI. If you wish to re-set your preferences, you should delete params.json and number.txt from the local directory. Deleting these two files is *safe*.  

