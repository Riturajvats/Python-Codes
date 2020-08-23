import random

class Pound:

   def __init__(self,rare=False):

       self.rare=rare

       if rare:
           self.value=1.25
       else:
            self.value=1.00
            
       self.color="gold"
       self.num_edges=1
       self.diameter=22.5 #mm
       self.thickness=3.15 #mm
       self.heads=True

   def __def__(self):      #It will deleted the coin and the coin become not defined
       print("Coin Spent!")

   def rust(self):
       self.color = "greenish"

   def clean(self):
       self.color="gold"

   def flip(self):
       heads_option=[True,False]
       choice = random.choice(heads_option)
       self.heads=choice
