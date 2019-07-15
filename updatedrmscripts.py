#pip install these
import pyautogui
import pandas as pd
import tkinter as tk
import regex as re

pyautogui.failsafe = True

#change the name to the excel sheet of your name data
namelist_df = pd.read_excel(r'C:\Users\I515965\Desktop\names.xlsx')
namelist = namelist_df.loc[:,1]
length = namelist.shape[0]
email_list = []
counter = 0

#alter the click coordinates given by shreya
for i in namelist:
    name = i
    #click compose email button
    pyautogui.click(76, 282)
    pyautogui.PAUSE = 0.3
    #click to the recipients
    pyautogui.click(402, 531)
    #type name
    pyautogui.typewrite(name)
    pyautogui.PAUSE = 0.35
    #press enter a couple of times
    pyautogui.press('enter')
    pyautogui.PAUSE = 0.1
    pyautogui.press('enter')
    #click anywhere in the recipients box
    pyautogui.click(367, 533)
    pyautogui.hotkey('ctrl', 'a')
    #copies to clipboard
    pyautogui.hotkey('ctrl', 'c')
    email = tk.Tk().clipboard_get()
    email_list.append(email)
    print(email)
    #click anywhere in the email body
    pyautogui.click(402, 731)
    #this deletes the draft and speeds up your server.
    pyautogui.hotkey('ctrl', 'shift', 'd')
    counter = counter + 1

    if counter == 20:
        pyautogui.PAUSE = 5
        #pyautogui.hotkey('ctrl', 'f5')
        #pyautogui.PAUSE = 3
        counter = 0

    if name == '':
        break

email_df = pd.DataFrame(data={'parsed_email': email_list})

def refine(string):
    if re.search(r'<', string) == None:
        return 'REDO'
    else:
        email = re.search(r'<(.+[^>])', string).group(1)
        return email

email_df['refined_emails'] = email_df['parsed_email'].apply(lambda x: refine(x))
#change the name of the excel list every successive iteration.
email_df.to_excel('emaillist.xlsx')
