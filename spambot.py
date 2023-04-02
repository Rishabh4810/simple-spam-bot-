
import customtkinter 
import pyautogui as pt
from  time import sleep

customtkinter.set_appearance_mode("System")

main = customtkinter.CTk()
main.title("spam")

def button_1():
    mssage_to_print = mssg.get()
    times_to_click = number.get()
    sleep(5)
    spam(mssage_to_print,times_to_click)
 
def spam(mssg,times):
    if int(times) == 0:
       while True:
        pt.typewrite(mssg)
        pt.press("enter")
    else:
        global i
        i=0
        for i in range (int(times)):
            pt.typewrite(mssg)
            pt.press("enter")

number = customtkinter.CTkEntry(main,width=250,placeholder_text="number of times you want to spam")
mssg = customtkinter.CTkEntry(main,width=250,placeholder_text="message you want to spam")
Button_1 = customtkinter.CTkButton(main,text="enter",command=button_1,width=100)

number.pack(pady=10)
mssg.pack(pady=10)
Button_1.pack(pady=10)

main.geometry("500x300+5+3")
main.mainloop()