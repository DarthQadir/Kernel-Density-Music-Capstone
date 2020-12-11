import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk


#Create the Tkinter window and subwindows that will be used
window = tk.Tk()
window.title("Input Tablature")
popup_moretab = tk.Toplevel()
popup_mode = tk.Toplevel()

popup_moretab.withdraw()
popup_mode.withdraw()



#Make explanation
label_explanation = tk.Label(master=window, height=12, width=90,text=
"\n\n\n 1- Copy paste your tablature in the box below and press enter \n \n 2- If you need to input more tablatures, click yes in the next prompt, or if you're done, click no' \n \n 3- Input which key and mode you want your output to be in. \n \n 4- Get new tablature!")
label_explanation.grid(row=0,column=0)

#Make title
run_font = tkFont.Font(family="Lucida Grande", size=17)
run_label = tk.Label(master=window,text='How to run the program',font=run_font)
run_label.place(x=283,y=16)

#Make input box for guitar tabs
input_box = tk.Text(master=window,height=8, width=100,borderwidth=3)
input_box.grid(row=1,column=0,pady=10)
input_box.insert(tk.END,'Enter guitar tab here......') 


#Code that clears the input guitar tab part
def clear_textbox(event):
    if input_box.get('1.0',tk.END) == 'Enter guitar tab here......\n':
        input_box.delete('1.0', tk.END)
input_box.bind("<Button-1>", clear_textbox)


#Add buttons
clear_button = tk.Button(master=window, text='Clear input')
clear_button.grid(row=2,column=0,pady=5)


#Code that clears all input
def clear_tab(event):
    input_box.delete('1.0',tk.END)
    
clear_button.bind("<Button-1>",clear_tab)

    
def clear_next_tab(event):
    window.deiconify()
    input_box.delete('1.0',tk.END)
    input_box.insert(tk.END,'Enter guitar tab here......')
    popup_moretab.withdraw()    

    


def ask_tab(event):
    popup_moretab.deiconify()
    window.withdraw()
    popup_moretab.title('Input more tabs?')
    input_text = tk.Label(master=popup_moretab,text='Do you want to input more tabs?',width=30)
    input_text.grid(row=0,column=0,columnspan=2)
    
    yes_button = tk.Button(master=popup_moretab,text='Yes')
    yes_button.grid(row=1,column=0,pady=3)
    yes_button.bind("<Button-1>",clear_next_tab)
    
    no_button = tk.Button(master=popup_moretab,text='No')
    no_button.grid(row=1,column=1,pady=3)
    no_button.bind("<Button-1>",mode_choose)

input_box.bind("<Return>",ask_tab)


def mode_choose(event):
    popup_mode.deiconify()
    popup_moretab.withdraw()
    window.withdraw()
    popup_mode.title('Choose key and mode of song')
    
    keys_label=tk.Label(master=popup_mode,text='Choose Key')
    keys_label.grid(row=0,column=0)
    
    mode_label=tk.Label(master=popup_mode,text='Choose Mode')
    mode_label.grid(row=0,column=1)
    
    textvar_key = tk.StringVar()
    textvar_mode = tk.StringVar()
    keys = ttk.Combobox(master=popup_mode, textvariable = textvar_key)
    modes = ttk.Combobox(master=popup_mode, textvariable=textvar_mode)
    
    keys['values'] = ('C','C#','D','D#','E','F','F#','G','G#','A','A#','B')
    modes['values'] = ('Ionian (Major Scale)','Dorian','Phrygian','Lydian','Mixolydian','Aeolian (Minor Scale)','Locrian')
    
    keys.grid(row=1,column=0,padx=10)
    modes.grid(row=1,column=1)
    
    keys.current(0)
    modes.current(0)
    
    tabs_button = tk.Button(master=popup_mode,text='Get tabs!')
    tabs_button.grid(row=2,column=0,columnspan=2,pady=10)
    tabs_button.bind("<Button-1>",machine_learning)
    
    
def machine_learning(event):
    window.quit()
    
    



window.mainloop()