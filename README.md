# WhatsApp-Bot

This is a simple Web WhatsApp Bot developed in python3 using Selenium along with the interactive GUI using Kivy. 
Selenium is used mainly for automating web applications for testing purposes, but is certainly not limited to just that. Boring web-based administration tasks can (and should!) be automated as well.

Selenium has the support of some of the largest browser vendors who have taken (or are taking) steps to make Selenium a native part of their browser. It is also the core technology in countless other browser automation tools, APIs and frameworks.

# Features!

  - Creates a WhatsApp group automatically by providing group name and participants in GUI
  
### Requirements

* [Python 3+](https://www.python.org/download/releases/3.0/?) - Pyhton 3.6+ verion
* [Selenium](https://github.com/SeleniumHQ/selenium) - Selenium for web automation
* [Kivy](https://kivy.org/doc/stable/) - for GUI

### Installation

Step 1: Install the required modules
```sh
$ pip3 install selenium
$ pip3 install kivy
```
OR

Install all the module in one go
```sh
$ sh overall.sh
```

Step 2: Selenium requires a driver to interface with the chosen browser.
> For [Click for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
> For [Click for FireFox](https://github.com/mozilla/geckodriver/releases)
> For [Click for safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10)

Step 3: Extract the downloaded driver onto a project folder and enter the path to driver in logic.py file.

Step 4: Set path variable to the environment. Paste this command to the terminal
```sh
$ export PATH=$PATH:/home/path/to/the/driver/folder/ # optional if error occurs
```
Step 5: run groupdb.py using Python3
```sh
$ python3 groupdb.py
```
Step 6: Enter the name of the group and the participants you want to add in that group, then press Submit

Step 7: When the WhatsApp Web is opened on browser, it will ask you to scan a QR code when you do it for first time

Step 8: After Scanning the QR code, you will be asked to press Enter Key in the terminal.

### Note

The contact name should match exactly with the name saved in your contacts.
