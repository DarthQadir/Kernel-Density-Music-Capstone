
#List of fret numbers on guitar strings and the corresponding musical note

e_notes = {
    0:'E4',
    1:'F4',
    2:'F#4',
    3:'G4',
    4:'G#4',
    5:'A4',
    6:'A#4',
    7:'B4',
    8:'C4',
    9:'C#4',
    10:'D4',
    11:'D#4',
    12:'E5',
    13:'F5',
    14:'F#5',
    15:'G5',
    16:'G#5',
    17:'A5',
    18:'A#5',
    19:'B5',
    20:'C5',
    21:'C#5',
    22:'D5',
    23:'D#5',
    24:'E6'

}

B_notes = {
    0:'B3',
    1:'C4',
    2:'C#4',
    3:'D4',
    4:'D#4',
    5:'E4',
    6:'F4',
    7:'F#4',
    8:'G4',
    9:'G#4',
    10:'A4',
    11:'A#4',
    12:'B4',
    13:'C5',
    14:'C#5',
    15:'D5',
    16:'D#5',
    17:'E5',
    18:'F5',
    19:'F#5',
    20:'G5',
    21:'G#5',
    22:'A5',
    23:'A#5',
    24:'B5'

}


G_notes = {
    0:'G3',
    1:'G#3',
    2:'A3',
    3:'A#3',
    4:'B3',
    5:'C3',
    6:'C#3',
    7:'D3',
    8:'D#3',
    9:'E3',
    10:'F3',
    11:'F#3',
    12:'G4',
    13:'G#4',
    14:'A4',
    15:'A#4',
    16:'B4',
    17:'C4',
    18:'C#4',
    19:'D4',
    20:'D#4',
    21:'E4',
    22:'F4',
    23:'F#4',
    24:'G5'

}

D_notes = {
    0:'D3',
    1:'D#3',
    2:'E3',
    3:'F3',
    4:'F#3',
    5:'G3',
    6:'G#3',
    7:'A3',
    8:'A#3',
    9:'B3',
    10:'C3',
    11:'C#3',
    12:'D4',
    13:'D#4',
    14:'E4',
    15:'F4',
    16:'F#4',
    17:'G4',
    18:'G#4',
    19:'A4',
    20:'A#4',
    21:'B4',
    22:'C4',
    23:'C#4',
    24:'D5'

}

A_notes = {
    0:'A2',
    1:'A#2',
    2:'B2',
    3:'C2',
    4:'C#2',
    5:'D2',
    6:'D#2',
    7:'E2',
    8:'F2',
    9:'F#2',
    10:'G2',
    11:'G#2',
    12:'A3',
    13:'A#3',
    14:'B3',
    15:'C3',
    16:'C#3',
    17:'D3',
    18:'D#3',
    19:'E3',
    20:'F3',
    21:'F#3',
    22:'G3',
    23:'G#3',
    24:'A4'

}


E_notes = {
    0:'E2',
    1:'F2',
    2:'F#2',
    3:'G2',
    4:'G#2',
    5:'A2',
    6:'A#2',
    7:'B2',
    8:'C2',
    9:'C#2',
    10:'D2',
    11:'D#2',
    12:'E3',
    13:'F3',
    14:'F#3',
    15:'G3',
    16:'G#3',
    17:'A3',
    18:'A#3',
    19:'B3',
    20:'C3',
    21:'C#3',
    22:'D3',
    23:'D#3',
    24:'E4'

}

def shift(seq, shift):
    """
    Helper function for mode_notes()
    """
    return seq[shift:] + seq[:shift]


def mode_notes(mode,key):

    """
    Function that holds the notes for each different key and mode_notes
    The filter_notes function uses the notes provided by this function to filter
    by
    """

    major = [0,2,4,5,7,9,11]
    Dorian = [0,2,3,5,7,9,10]
    Phrygian = [0,1,3,5,7,8,10]
    Lydian = [0,2,4,6,7,9,11]
    Mixolydian = [0,2,4,5,7,9,10]
    Aeolian = [0,2,3,5,7,8,10]
    Locrian = [0,1,3,5,6,8,10]

    if mode == 'Ionian (Major Scale)':
        chosen_mode = major
    elif mode == 'Aeolian (Minor Scale)':
        chosen_mode = aeolian
    else:
        chosen_mode = eval(mode)

    notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    shifted_notes = shift(notes,notes.index(key))
    new_notes = [ shifted_notes[i] for i in chosen_mode]

    return new_notes



def filter_notes(e_notes,B_notes,G_notes,D_notes,A_notes,E_notes,processed_notes,new_notes):
    """
    Filter notes according to the specified key and mode by the user
    """

    string_notes = [e_notes,B_notes,G_notes,D_notes,A_notes,E_notes]
    filtered_notes = []

    #Filter notes according to major scale
    for note in processed_notes:
      if len(note) == 6:

        for index in range(len(note)):

          if note[index].isdigit() == True:

            temp_note = string_notes[index][int(note[index])]

            if len(temp_note) == 2 and temp_note[0] in new_notes:
              filtered_notes.append(note)

            elif temp_note[0:2] in new_notes:
              filtered_notes.append(note)

      else:
        for index in range(len(note)):
          if note[index].isdigit() == True:
            temp_note = string_notes[index][int(note[index]+note[index+6])]

            if len(temp_note) == 2 and temp_note[0] in new_notes:
              filtered_notes.append(note)

            elif temp_note[0:2] in new_notes:
              filtered_notes.append(note)
            break

    return filtered_notes


def print_notes(filtered_notes):
    #Lists for holding notes
    print_e = []
    print_B = []
    print_G = []
    print_D = []
    print_A = []
    print_E = []

    for note in filtered_notes:
      if len(note) == 6:
        print_e.append(note[0])
        print_B.append(note[1])
        print_G.append(note[2])
        print_D.append(note[3])
        print_A.append(note[4])
        print_E.append(note[5])

        print_e.append('-')
        print_B.append('-')
        print_G.append('-')
        print_D.append('-')
        print_A.append('-')
        print_E.append('-')
      else:
        print_e.append(note[0])
        print_B.append(note[1])
        print_G.append(note[2])
        print_D.append(note[3])
        print_A.append(note[4])
        print_E.append(note[5])
        print_e.append(note[6])
        print_B.append(note[7])
        print_G.append(note[8])
        print_D.append(note[9])
        print_A.append(note[10])
        print_E.append(note[11])
        print_e.append('-')
        print_B.append('-')
        print_G.append('-')
        print_D.append('-')
        print_A.append('-')
        print_E.append('-')

    return(''.join(print_e), ''.join(print_B), ''.join(print_G),''.join(print_D),''.join(print_A),''.join(print_E))
