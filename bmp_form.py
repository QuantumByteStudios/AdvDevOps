from customtkinter import *
from pathlib import Path
from tkinter import *
from tkinter import messagebox, Toplevel, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Lenovo\Desktop\Mini Project f\assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
    
def clear():
    date_entry.delete(0, END)
    ca_entry.delete(0, END)
    co2_entry.delete(0, END)
    na_entry.delete(0, END)
    k_entry.delete(0, END)
    bun_entry.delete(0, END)
    crt_entry.delete(0, END)
    glc_entry.delete(0, END)

def submit():
    bmp_form.destroy()

bmp_form = CTk()
bmp_form.title("PulseAnalytics")
x = (bmp_form.winfo_screenwidth() - 650) // 2
y = (bmp_form.winfo_screenheight() - 700) // 2
bmp_form.geometry(f"650x700+{x}+{y}")
bmp_form.configure(bg="#000000")

frame1 = CTkFrame(master=bmp_form, fg_color="#96EFFF", corner_radius=0, width=650,height=700)
frame1.place(x=0, y=0)

title_label = CTkLabel(master=frame1, text="BMP Form", font=CTkFont('Microsoft YaHei UI Light',28,"bold",underline="true"))
title_label.place(relx=0.5, rely=0.06,anchor="center")

date_label = CTkLabel(master=frame1, text="Date:", font=CTkFont('Kanit Regular',20))
date_label.place(relx=0.1,rely=0.15)
date_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="DD/MM/YYYY")
date_entry.place(relheight=0.05,relwidth=0.5,relx=0.42,rely=0.15)

ca_label = CTkLabel(master=frame1, text="Calcium :", font=CTkFont('Kanit Regular',20))
ca_label.place(relx=0.1,rely=0.24)
ca_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="mg/L")
ca_entry.place(relheight=0.05,relwidth=0.5,relx=0.42,rely=0.24)

co2_label = CTkLabel(master=frame1, text="Bicarbonate(CO2) :", font=CTkFont('Kanit Regular',20))
co2_label.place(relx=0.1,rely=0.33)
co2_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="mEq/L")
co2_entry.place(relheight=0.05,relwidth=0.5,relx=0.42,rely=0.33)

na_label = CTkLabel(master=frame1, text="Sodium :", font=CTkFont('Kanit Regular',20))
na_label.place(relx=0.1,rely=0.42)
na_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="mEq/L")
na_entry.place(relheight=0.05,relwidth=0.5,relx=0.42,rely=0.42)

k_label = CTkLabel(master=frame1, text="Potassium :", font=CTkFont('Kanit Regular',20))
k_label.place(relx=0.1,rely=0.51)
k_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="mEq/L")
k_entry.place(relheight=0.05,relwidth=0.5,relx=0.42,rely=0.51)

bun_label = CTkLabel(master=frame1, text="Blood Urea Nitrogen :", font=CTkFont('Kanit Regular',20))
bun_label.place(relx=0.1,rely=0.6)
bun_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="mg/dL")
bun_entry.place(relheight=0.05,relwidth=0.5,relx=0.42,rely=0.6)

crt_label = CTkLabel(master=frame1, text="Creatinine :", font=CTkFont('Kanit Regular',20))
crt_label.place(relx=0.1,rely=0.69)
crt_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="mg/dL")
crt_entry.place(relheight=0.05,relwidth=0.5,relx=0.42,rely=0.69)

glc_label = CTkLabel(master=frame1, text="Glucose :", font=CTkFont('Kanit Regular',20))
glc_label.place(relx=0.1,rely=0.78)
glc_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="mg/dL")
glc_entry.place(relheight=0.05,relwidth=0.5,relx=0.42,rely=0.78)


submit_btn = CTkButton(master=frame1,text="Submit",corner_radius=30,fg_color="#5FBDFF",hover_color="#7B66FF",width=150,height=60,font=CTkFont('Kanit Regular',20),text_color="#000000",command=submit)
submit_btn.place(relheight=0.06,relwidth=0.19,relx=0.65,rely=0.92,anchor="center")

clear_btn = CTkButton(master=frame1,text="Clear",corner_radius=30,fg_color="transparent",hover_color="#FF2D3F",border_width=2,border_color="black",width=150,height=60,font=CTkFont('Kanit Regular',20),text_color="#000000",command=clear)
clear_btn.place(relheight=0.06,relwidth=0.18,relx=0.35,rely=0.92,anchor="center")




bmp_form.resizable(False, False)
bmp_form.mainloop()