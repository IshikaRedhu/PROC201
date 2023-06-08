from tkinter import *
window=Tk()


def calculate_interest():
    amount = int(Amount.get())
    rate = int(Rate.get())
    time = int(Time.get())
    interest = (amount*rate*time)/100
    interest = round(interest,1)
    result_label.destroy()
    net_amount = amount+interest

    output_message =Label(result_frame,text="The interest generated is "+str(interest),bg="#c0d6e4",font=('Calibri',12),width=42)
    output_message1 =Label(result_frame,text="The payable amount is "+str(net_amount),bg="#c0d6e4",font=('Calibri',12),width=42)
    output_message1.place(x=20,y=40)
    output_message1.pack()
    output_message.place(x=20,y=45)
    output_message.pack()

window.title('Simple Interest Calculator')
window.geometry("380x400")
window.configure(bg='#c0d6e4')


app_label=Label(window, text="SIMPLE INTEREST CALCULATOR", fg = "black", bg = "#c0d6e4", font=("Calibri", 20),bd=5)
app_label.place(x=20, y=20)

amount_label=Label(window, text="Principal Amount", fg = "black", bg = "#c0d6e4", font=("Calibri", 12),bd=1)
amount_label.place(x=20, y=90)

Amount=Entry(window, text="", bd=2, width=22)
Amount.place(x=150, y=92)

rate_label=Label(window, text="Rate (%)", fg = "black", bg = "#c0d6e4", font=("Calibri", 12),bd=1)
rate_label.place(x=20, y=140)

Rate=Entry(window, text="", bd=2, width=22)
Rate.place(x=150, y=142)

time_label=Label(window, text="Time (years)", fg = "black", bg = "#c0d6e4", font=("Calibri", 12),bd=1)
time_label.place(x=20, y=185)

Time=Entry(window, text="", bd=2, width=22)
Time.place(x=150, y=187)

calculate_button= Button(window,text="Calculate",fg="black",bg="#c0d6e4",bd=4,command = calculate_interest)
calculate_button.place(x=20,y=250)

result_frame = LabelFrame(window,text="Result", bg = "#c0d6e4", font=("Calibri", 12))
result_frame.pack(padx=20, pady=30)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "#c0d6e4", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()
window.mainloop()
