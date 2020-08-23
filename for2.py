students={
   "male":["Tom","Charlie","Rituraj","Sunny"],
   "female":["Elizabeth","Huda","Emily","Samantha"]
    }

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
