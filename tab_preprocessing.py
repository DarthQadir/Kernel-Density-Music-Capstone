




class tab_preprocessor():

    def __init__(self,tabs):
    
        #Guitar tab
        self.tabs = tabs
        

        #Arrays to hold each string's notes
        self.string_e = []
        self.string_B = []
        self.string_G = []
        self.string_D = []
        self.string_A = []
        self.string_E = []
        
        #Checks for optimization purposes
        self.check_e = False
        self.check_B = False
        self.check_G = False
        self.check_D = False
        self.check_A = False
        self.check_E = False
        
        self.final_notes = []
        self.notes = []
        

    def length_check(self):
        """   
        Function that returns the length of each tablature that is input into the program.
        
        Checks the length by measuring distance between the '|' symbol in tabs
        """

        tab_lengths = []
        for tab in self.tabs:
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
        
      


    def add_dash(self,string,longest_len):
        """
        Helper function for tab_to_list that adds dashes to strings to make each string the same length
        """
        while len(string) < longest_len:
          string += '-'  

    def get_notes(self,tab,i,string_type,tab_lengths,count):
        """
        Helper function for tab_to_list that appends the right notes from the string list to another list
        """
        if eval('self.check_'+string_type) == False:
            if tab[i] == string_type:
              eval('self.string_'+string_type).append(tab[i+2:i+2+tab_lengths[count]])
              temp = eval('self.check_'+string_type)
              temp = True



    def tab_to_list(self,tab_lengths):
        """
        Function that adds each string's notes from each tab to a list.
        
        Returns each string's notes in a list
        """



        count = 0



        #Put the notes for each string in the aforementioned lists
        for tab in self.tabs:
          
          for i in range(len(tab)):   
            self.get_notes(tab,i,'e',tab_lengths,count)
            self.get_notes(tab,i,'B',tab_lengths,count)
            self.get_notes(tab,i,'G',tab_lengths,count)
            self.get_notes(tab,i,'D',tab_lengths,count)
            self.get_notes(tab,i,'A',tab_lengths,count)
            self.get_notes(tab,i,'E',tab_lengths,count)

          count+=1

        
        #Now we have the tabs in a prettier format

        self.string_e = ''.join(self.string_e)
        self.string_B = ''.join(self.string_B)
        self.string_G = ''.join(self.string_G)
        self.string_D = ''.join(self.string_D)
        self.string_A = ''.join(self.string_A)
        self.string_E = ''.join(self.string_E)



        #Make each string of a consistent length
        longest_len = max(len(self.string_e),len(self.string_B),len(self.string_G),len(self.string_D),len(self.string_A),len(self.string_E))



        self.add_dash(self.string_e,longest_len)
        self.add_dash(self.string_B,longest_len)
        self.add_dash(self.string_G,longest_len)
        self.add_dash(self.string_D,longest_len)
        self.add_dash(self.string_A,longest_len)
        self.add_dash(self.string_E,longest_len)
          
        return (self.string_e,self.string_B,self.string_G,self.string_D,self.string_A,self.string_E,longest_len)
        
     
     
     
     
     
    def twelve_note(self,i):
        """
        Helper function for vertical_slice. It appends two vertical slices of our tab when we have double digit notes
        """
        self.notes.append(self.string_e[i])
        self.notes.append(self.string_B[i])
        self.notes.append(self.string_G[i])
        self.notes.append(self.string_D[i])
        self.notes.append(self.string_A[i])
        self.notes.append(self.string_E[i])
        self.notes.append(self.string_e[i+1])
        self.notes.append(self.string_B[i+1])
        self.notes.append(self.string_G[i+1])
        self.notes.append(self.string_D[i+1])
        self.notes.append(self.string_A[i+1])
        self.notes.append(self.string_E[i+1])
        self.final_notes.append(self.notes)

    def six_note(self,i):
        """
        Helper function for vertical_slice. It appends one vertical slice of our tab
        """
        self.notes.append(self.string_e[i])
        self.notes.append(self.string_B[i])
        self.notes.append(self.string_G[i])
        self.notes.append(self.string_D[i])
        self.notes.append(self.string_A[i])
        self.notes.append(self.string_E[i])
        self.final_notes.append(self.notes)


    def note_check(self,string,i,longest_len):
        """
        Helper function for vertical_slice. It checks whether we have a 2 digit or 1 digit note
        """
        if string[i].isdigit() == True:
            if i != longest_len-1:
              if string[i+1].isdigit() == True:
                return 2
              else:
                return 1

     
     

    def vertical_slice(self,longest_len):
        """
        This cell basically takes a vertical slice of the tablature to get a single note/chord and it appends that note/chord into a list
        Only reason I have more 'repetitive' code is because I need the flag to check for double digit notes,
        and that uses the continue function
        """

        flag=True
        for i in range(longest_len):
            if flag == False:
                flag = True
                continue
            self.notes = []
            if self.note_check(self.string_e,i,longest_len) == 2:
                self.twelve_note(i)
                flag = False
                continue
            elif self.note_check(self.string_e,i,longest_len) == 1:
                self.six_note(i)
                continue
            if self.note_check(self.string_B,i,longest_len) == 2:
                self.twelve_note(i)
                flag = False
                continue
            elif self.note_check(self.string_B,i,longest_len) == 1:
                self.six_note(i)
                continue
            if self.note_check(self.string_G,i,longest_len) == 2:
                self.twelve_note(i)
                flag = False
                continue
            elif self.note_check(self.string_G,i,longest_len) == 1:
                self.six_note(i)
                continue
            if self.note_check(self.string_D,i,longest_len) == 2:
                self.twelve_note(i)
                flag = False
                continue
            elif self.note_check(self.string_D,i,longest_len) == 1:
                self.six_note(i)
                continue
            if self.note_check(self.string_A,i,longest_len) == 2:
                self.twelve_note(i)
                flag = False
                continue
            elif self.note_check(self.string_A,i,longest_len) == 1:
                self.six_note(i)
                continue
            if self.note_check(self.string_E,i,longest_len) == 2:
                self.twelve_note(i)
                flag = False
                continue
            elif self.note_check(self.string_E,i,longest_len) == 1:
                self.six_note(i)
                continue
        return self.final_notes
     
     
    def remove_wrong_notes(self,final_notes):
        """
        Function that processes final notes to get rid of wrongly processed notes. For example,
        consecutive 5's can be read as 55, but the guitar only has 24 frets.
        """
        
        #Array to store indices of notes which are to be removed
        removal_index = []

        for note in range(len(self.final_notes)):
          if len(self.final_notes[note]) > 8:
            for i in range(6):
              if self.final_notes[note][i].isdigit() == True and self.final_notes[note][i+6].isdigit() == True:
                if (int(self.final_notes[note][i] + self.final_notes[note][i+6])) > 24:
                  self.final_notes.append(self.final_notes[note][0:6])
                  self.final_notes.append(self.final_notes[note][6:12])
                  removal_index.append(note)
                  break


        #Get rid of the wrong notes
        self.final_notes = [i for j, i in enumerate(self.final_notes) if j not in removal_index]

        #Join different string notes or dashes
        for i in range(len(self.final_notes)):
          self.final_notes[i] = ''.join(self.final_notes[i])
          
        return self.final_notes
    
    
