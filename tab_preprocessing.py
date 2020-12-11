

def length_check(tabs):
    """   
    Function that returns the length of each tablature that is input into the program.
    
    Checks the length by measuring distance between the '|' symbol in tabs
    """

    tab_lengths = []
    for tab in tabs:
      start_check = False
      for i in range(len(tab)):

        if start_check == False:
          if tab[i] == '|':
            start = i
            start_check = True

        else:
          if tab[i] == '|':
            end = i
            break
      tab_lengths.append(end - start - 1)
      
    return tab_lengths
    
  


def add_dash(string,longest_len):
    """
    Helper function for tab_to_list that adds dashes to strings to make each string the same length
    """
    while len(string) < longest_len:
      string += '-'  

def get_notes(tab,i,string_type):
    """
    Helper function for tab_to_list that appends the right notes from the string list to another list
    """
  if eval('check_'+string_type) == False:
    if tab[i] == string_type:
      eval('string_'+string_type).append(tab[i+2:i+2+tab_lengths[count]])
      temp = eval('check_'+string_type)
      temp = True



def tab_to_list(tabs,tab_lengths):
    """
    Function that adds each string's notes from each tab to a list.
    
    Returns each string's notes in a list
    """
    #Arrays to hold each string's notes
    
    global string_e,string_B,string_G,string_D,string_A,string_E
    string_e = []
    string_B = []
    string_G = []
    string_D = []
    string_A = []
    string_E = []


    count = 0



    #Put the notes for each string in the aforementioned lists
    for tab in tabs:

      #Checks for optimization purposes
      check_e = False
      check_B = False
      check_G = False
      check_D = False
      check_A = False
      check_E = False
      
      for i in range(len(tab)):   
        get_notes(tab,i,'e')
        get_notes(tab,i,'B')
        get_notes(tab,i,'G')
        get_notes(tab,i,'D')
        get_notes(tab,i,'A')
        get_notes(tab,i,'E')

      count+=1


    #Now we have the tabs in a prettier format
    string_e = ''.join(string_e)
    string_B = ''.join(string_B)
    string_G = ''.join(string_G)
    string_D = ''.join(string_D)
    string_A = ''.join(string_A)
    string_E = ''.join(string_E)


    #Make each string of a consistent length
    global longest_len
    longest_len = max(len(string_e),len(string_B),len(string_G),len(string_D),len(string_A),len(string_E))



    add_dash(string_e,longest_len)
    add_dash(string_B,longest_len)
    add_dash(string_G,longest_len)
    add_dash(string_D,longest_len)
    add_dash(string_A,longest_len)
    add_dash(string_E,longest_len)
      
    return (string_e,string_B,string_G,string_D,string_A,string_E,longest_len)
    
 
 
 
 
 
 def twelve_note(i):
  """
  Helper function for vertical_slice. It appends two vertical slices of our tab
  """
  notes.append(string_e[i])
  notes.append(string_B[i])
  notes.append(string_G[i])
  notes.append(string_D[i])
  notes.append(string_A[i])
  notes.append(string_E[i])
  notes.append(string_e[i+1])
  notes.append(string_B[i+1])
  notes.append(string_G[i+1])
  notes.append(string_D[i+1])
  notes.append(string_A[i+1])
  notes.append(string_E[i+1])
  final_notes.append(notes)

def six_note(i):
  """
  Helper function for vertical_slice. It appends one vertical slice of our tab
  """
  notes.append(string_e[i])
  notes.append(string_B[i])
  notes.append(string_G[i])
  notes.append(string_D[i])
  notes.append(string_A[i])
  notes.append(string_E[i])
  final_notes.append(notes)


def note_check(string,i):
  """
  Helper function for vertical_slice. It checks whether we have a 2 digit or 1 digit note
  """
  if string[i].isdigit() == True:
        if i != longest_len-1:
          if string[i+1].isdigit() == True:
            return 2
          else:
            return 1

 
 

def vertical_slice():
    """
    This cell basically takes a vertical slice of the tablature to get a single note/chord and it appends that note/chord into a list
    Only reason I have more 'repetitive' code is because I need the flag to check for double digit notes,
    and that uses the continue function
    """

    final_notes = []
    flag=True
    for i in range(longest_len):
        if flag == False:
            flag = True
            continue
        notes = []
        if note_check(string_e,i) == 2:
            twelve_note(i)
            flag = False
            continue
        elif note_check(string_e,i) == 1:
            six_note(i)

        if note_check(string_B,i) == 2:
            twelve_note(i)
            flag = False
            continue
        elif note_check(string_B,i) == 1:
            six_note(i)

        if note_check(string_G,i) == 2:
            twelve_note(i)
            flag = False
            continue
        elif note_check(string_G,i) == 1:
            six_note(i)

        if note_check(string_D,i) == 2:
            twelve_note(i)
            flag = False
            continue
        elif note_check(string_D,i) == 1:
            six_note(i)

        if note_check(string_A,i) == 2:
            twelve_note(i)
            flag = False
            continue
        elif note_check(string_A,i) == 1:
            six_note(i)

        if note_check(string_E,i) == 2:
            twelve_note(i)
            flag = False
            continue
        elif note_check(string_E,i) == 1:
            six_note(i)
 
    return final_notes
 
 
 def remove_wrong_notes(final_notes):
    """
    Function that processes final notes to get rid of wrongly processed notes. For example,
    consecutive 5's can be read as 55, but the guitar only has 24 frets.
    """
    
    #Array to store indices of notes which are to be removed
    removal_index = []

    for note in range(len(final_notes)):
      if len(final_notes[note]) > 8:
        for i in range(6):
          if final_notes[note][i].isdigit() == True and final_notes[note][i+6].isdigit() == True:
            if (int(final_notes[note][i] + final_notes[note][i+6])) > 24:
              final_notes.append(final_notes[note][0:6])
              final_notes.append(final_notes[note][6:12])
              removal_index.append(note)
              break


    #Get rid of the wrong notes
    final_notes = [i for j, i in enumerate(final_notes) if j not in removal_index]

    #Join different string notes or dashes
    for i in range(len(final_notes)):
      final_notes[i] = ''.join(final_notes[i])
      
    return final_notes
    
    
