from tkinter import *
from tkinter import messagebox
import smtplib
import random

root = Tk()
root.title("Send OTP Via Email")
root.geometry("565x250")
email_label = Label(root, text="Enter receiver's Email: ", font=("ariel 15 bold"), relief=FLAT)
email_label.grid(row=0, column=0, padx=15, pady=60)
email_entry = Entry(root, font=("ariel 15 bold"), width=25, relief=GROOVE, bd=2)
email_entry.grid(row=0, column=1, padx=12, pady=60)
email_entry.focus()


def send():
    try:
        s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
        s.starttls()
        s.login("sender_email", "sender_email_password")
        otp = random.randint(1000, 9999)
        otp = str(otp)
        s.sendmail("sender_email", email_entry.get(), otp)
        messagebox.showinfo("Send OTP via Email", f"OTP sent to {email_entry.get()}")
        s.quit()

    except:
        messagebox.showinfo("Send OTP via Email",
                            "Please enter the valid email address OR check an internet connection")


send_button = Button(root, text="Send Email", font=("ariel 15 bold"), bg="black", fg="green2", bd=3, command=send)
send_button.place(x=210, y=150)
root.mainloop()