#Import libraries
from sklearn.neighbors import KernelDensity
from sklearn.preprocessing import LabelEncoder
from math import ceil, floor




class density_estimator():

    def __init__(self):
        
        self.encoder = LabelEncoder()
        self.model = None

    def density_estimate(self,notes,bandwidth=0.5,kernel='gaussian'):
        """
        Function that performs density estimation on a dataset
        """
        
        #Label encoding to transform notes
        transformed_notes = self.encoder.fit_transform(notes)

        #Fit our kernel density estimate for the data
        self.model = KernelDensity(bandwidth=bandwidth,kernel=kernel)
        self.model.fit([transformed_notes])
        
        
      

    def generate_samples(self):  
        """
        This cell ensures that our samples don't go out of the range. This is a minor
        drawback of density estimation that we can get samples out of the range of our 
        data e.g. if your dataset just consists of 1's, there is a VERY small chance
        you might just sample a 2 or a -1. 
        """
        sampled_notes = self.model.sample(1)
        #print(encoder.classes_)
        classes_len = len(self.encoder.classes_)

        processed_notes = []
        for samples in sampled_notes:
          for i in samples:
            try:
              note = [int(ceil(i))]
              if note[0] >= classes_len:
                note[0] = classes_len-1
              elif note[0] < 0:
                note[0] = 0
              processed_notes.append(self.encoder.inverse_transform(note)[0])
            except:
              note[0] = [int(floor(i))]
              if note[0] >= classes_len:
                note[0] = classes_len -1
              elif note[0] < 0:
                note[0] = 0
              processed_notes.append(self.encoder.inverse_transform(note)[0])
        return processed_notes