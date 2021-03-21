import tkinter as tk
import tkinter.font as tkFont
from density_estimation import density_estimator
from tab_preprocessing import tab_preprocessor
import music_theory

from tkinter import ttk





"""
Create the Tkinter window and subwindows that will be used
"""

#Main window
window = tk.Tk()
window.title("Input Tablature")


#Sub windows
popup_moretab = tk.Toplevel()
popup_mode = tk.Toplevel()
popup_print = tk.Toplevel()


#Withdraw subwindows so we show them when required
popup_moretab.withdraw()
popup_mode.withdraw()
popup_print.withdraw()


#Give the windows text titles as explanation
popup_moretab.title('Input more tabs?')
popup_mode.title('Choose key and mode of song')
popup_print.title('Outputted Guitar Tabs')

#Create variables to store key and mode of song
textvar_key = tk.StringVar()
textvar_mode = tk.StringVar()


"""
Code that makes a guide on how to use the program
"""

#Make guide on how to use program
label_explanation = tk.Label(master=window, height=12, width=90,text=
"\n\n\n 1- Copy paste your tablature in the box below and press enter \n \n 2- If you need to input more tablatures, click yes in the next prompt, or if you're done, click no' \n \n 3- Input which key and mode you want your output to be in. \n \n 4- Get new tablature!")
label_explanation.grid(row=0,column=0)


#Make title for the guide
run_font = tkFont.Font(family="Lucida Grande", size=17)
run_label = tk.Label(master=window,text='How to run the program',font=run_font)
run_label.place(x=283,y=16)




"""
Code that sets up our UI for inputting guitar tablature
"""


#Make input box for guitar tabs
input_box = tk.Text(master=window,height=8, width=100,borderwidth=3)
input_box.grid(row=1,column=0,pady=10)
input_box.insert(tk.END,'Enter guitar tab here......')


#Code that clears the input guitar tab text; mimicking softwares which clear text when you click on a box
def clear_textbox(event):
    if input_box.get('1.0',tk.END) == 'Enter guitar tab here......\n':
        input_box.delete('1.0', tk.END)
input_box.bind("<Button-1>", clear_textbox)


#Add button that clears tablature
clear_button = tk.Button(master=window, text='Clear input')
clear_button.grid(row=2,column=0,pady=5)


#Code that clears all input once the button defined above is clicked
def clear_tab(event):
    input_box.delete('1.0',tk.END)

clear_button.bind("<Button-1>",clear_tab)




def clear_next_tab(event):
    """
    Resets our UI when we need to input more tabs
    """
    window.deiconify()
    input_box.delete('1.0',tk.END)
    input_box.insert(tk.END,'Enter guitar tab here......')
    popup_moretab.withdraw()




def ask_tab(event):
    """
    Code that initializes a new UI to ask for more tablature input
    Also writes our inputted tabs to a text file
    """

    #Write tabs to text file
    with open('tabs.txt', 'a') as tab_text:
        tab_text.write(input_box.get('1.0',tk.END))

    popup_moretab.deiconify()
    window.withdraw()
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
    """
    Code that initializes a new UI to ask for the key/mode of a song
    """


    popup_mode.deiconify()
    popup_moretab.withdraw()
    window.withdraw()


    keys_label=tk.Label(master=popup_mode,text='Choose Key')
    keys_label.grid(row=0,column=0)

    mode_label=tk.Label(master=popup_mode,text='Choose Mode')
    mode_label.grid(row=0,column=1)

    #global textvar_key, textvar_mode

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
    """
    Code that carries out kernel density estimation and outputs our generated notes
    """
    popup_mode.withdraw()
    window.withdraw()
    with open('tabs.txt','r') as read_tabs:
        tabs = read_tabs.readlines()
        tabs = [''.join(tabs[i:i+6]).replace('\n',' ') for i in range(0,len(tabs),6)]

    tab_processor = tab_preprocessor(tabs)
    tab_lengths = tab_processor.length_check()
    tab_list = tab_processor.tab_to_list(tab_lengths)
    final_notes = tab_processor.vertical_slice(tab_list[6])
    final_notes = tab_processor.remove_wrong_notes(final_notes)


    model = density_estimator()
    model.density_estimate(final_notes)
    samples = model.generate_samples()
    new_notes = music_theory.mode_notes(textvar_mode.get(),textvar_key.get())
    processed_samples = music_theory.filter_notes(music_theory.e_notes,music_theory.B_notes,
                                            music_theory.G_notes,music_theory.D_notes,
                                            music_theory.A_notes,music_theory.E_notes,samples,new_notes)

    print_notes = music_theory.print_notes(processed_samples)

    #Limit number of notes printed to fit in GUI
    print_notes = [print_notes[i][0:150] for i in range(len(print_notes)) ]

    popup_print.deiconify()
    print_box = tk.Text(master=popup_print,height=8,width=150)
    print_box.pack()
    print_box.insert(tk.END,print_notes[0]+'\n'+print_notes[1]+'\n'+print_notes[2]+'\n'+
                        print_notes[3]+'\n'+print_notes[4]+'\n'+print_notes[5])

    #Delete contents of text file
    open('tabs.txt', 'w').close()



window.mainloop()
