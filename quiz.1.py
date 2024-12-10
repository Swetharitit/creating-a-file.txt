import tkinter as tk
from tkinter import messagebox
root=tk.Tk()


def answer():
    for x in q:
        print(x)
        
    ques=q.get()
    if user in ans:
        c_ans+=1
        messagebox.showinfo("succsessful",correct)
    else:
            w_ans+=1
            messagebox.showerror("invalid",wrong)
sub_button=tk.button(text="enter anser",command=answer)
    
    
