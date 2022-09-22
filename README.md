# dealScraper  

Python-based web-scraper for auto-reporting Amazon daily deals

## Installation & Run  

- Prior to running the application on your PC, you need to go to your browser and login to your WhatsApp account via https://web.whatsapp.com/.  

This is made easy, and can be done by pulling up a QR code scanner on your phone's WhatsApp account, and scanning the available QR code in your browser. This registers the PC as a device associated with your WhatsApp account for future use with dealScraper.  

- Clone the git repository to a local directory on your computer with the command line:    

```bash
git clone *the link to this repository*
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
