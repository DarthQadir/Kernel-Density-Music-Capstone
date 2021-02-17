import tkinter as tk
import tkinter.font as tkFont
import density_estimation
import tab_preprocessing
import music_theory

from tkinter import ttk


#Create the Tkinter window and subwindows that will be used
window = tk.Tk()
window.title("Input Tablature")

popup_moretab = tk.Toplevel()
popup_mode = tk.Toplevel()
popup_print = tk.Toplevel()


popup_moretab.withdraw()
popup_mode.withdraw()
popup_print.withdraw()

popup_print.title('Outputted Guitar Tabs')





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


#Code that clears the input guitar tab text
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
    
    #Write tabs to text file
    with open('tabs.txt', 'a') as tab_text:
        tab_text.write(input_box.get('1.0',tk.END))
        
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
    
    global textvar_key, textvar_mode
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
    popup_mode.withdraw()
    window.withdraw()
    with open('tabs.txt','r') as read_tabs:
        tabs = read_tabs.readlines()
        tabs = [''.join(tabs[i:i+6]).replace('\n',' ') for i in range(0,len(tabs),6)]
    
    tab_lengths = tab_preprocessing.length_check(tabs)
    tab_list = tab_preprocessing.tab_to_list(tabs,tab_lengths)
    final_notes = tab_preprocessing.vertical_slice(tab_list[0],tab_list[1],tab_list[2],tab_list[3],tab_list[4],tab_list[5],tab_list[6])
    final_notes = tab_preprocessing.remove_wrong_notes(final_notes)
    
    model = density_estimation.density_estimate(final_notes)
    samples = density_estimation.generate_samples(model)
    new_notes = music_theory.mode_notes(textvar_mode.get(),textvar_key.get())
    processed_samples = music_theory.filter_notes(music_theory.e_notes,music_theory.B_notes,
                                            music_theory.G_notes,music_theory.D_notes,
                                            music_theory.A_notes,music_theory.E_notes,samples,new_notes)
    
    print_notes = music_theory.print_notes(processed_samples)
    popup_print.deiconify()
    print_box = tk.Text(master=popup_print,height=8,width=150)
    print_box.pack()
    print_box.insert(tk.END,print_notes[0]+'\n'+print_notes[1]+'\n'+print_notes[2]+'\n'+
                        print_notes[3]+'\n'+print_notes[4]+'\n'+print_notes[5])
 
 

    
    



window.mainloop()