# Mailing Lists

This program semi-automates the process of getting a list of students from a bCourses class and typing their names into gmail to find their Berkeley email addresses. Note that if there is any easier way to do this, I highly encourage you to use that. Please feel free to message me if you can automate this further.

Credits given to Shrey Mohanty for enormous prepwork.

General Instructions:

MAKE SURE TO HAVE THESE INSTALLED: Python, Pandas, Pyautogui, tkinter, regex. You can do this by pip install. 

1. RAW HTML GATHERING 
- Go to the people's page of your course and filter for students only. Then scroll to the bottom of the webpage until all students are loaded in. Right click and save as the page as Webpage, Complete. (This may be different for other browsers, I am in chrome).

2. HTML Parse.
- Open the html file in your text editor, and select all the text and paste it into this website: https://wordhtml.com/
- Delete all the unecessary text above the first name manually and click the arrow next to the following to execute the action:
    - Delete Classes and IDs
    - Delete Empty Tags
    - Delete Tags with One Space
    - Deletes Successive Spaces
    - Deletes All Comments
    - Deletes Tag Attributes.
  
  - Select all and save this newly cleaned HTML code to new txt file.
  - From here, utilize the name extract jupyter notebook to fully extract the raw names. Make sure if you have successive classes, change the name of the excel in the last line in order to not have an error. Make sure to also change the filepath in loading the html code so that it matches your semi cleaned one. 

2. SETTING UP THE SCRIPTS
Open up your Berkeley email account, click compose email, and splitscreen the tab with your Python environment. In the command line, type 'import pyautogui' (note: this is assuming you already have the package installed) and press enter. Type 'pyautogui.position()' and move your mouse to hover over the recipients part of your compose box. Press enter to run the command. Copy coordinates of what the comments in the python file direct you to do.

3. RUNNING THE SCRIPTS
Run the updatedrmscripts.py in command prompt. Make sure to not move your mouse while the program is running, but if anything does go wrong, move your mouse to the upper left corner of the screen to stop the program.

Notes:
- Gmail is smart and will know if you're running scripts. Make sure to close all your tabs when this runs to reduce autofill failure.
- If you notice that the autofill is erroring out, increase the pause times until performance improves.
- There will usually be some names whose emails were not found after the program has finished running. You can either manually fill it in, or run the scripts again with an excel of just the missed one.

The scripts does all of the refining for you. 
