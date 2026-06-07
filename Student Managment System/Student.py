class student:
    def __init__(self,rollno:int,name:str,Fname:str,phone:int):
        self.rollno=rollno
        self.name=name
        self.Fname=Fname
        self.phone=phone
    def __str__(self):
         return f"{self.rollno},{self.name},{self.Fname},{self.phone}"