class passenger:
    def __init__(self,name,age,p_id):
        self.name=name
        self.age=age
        self.p_id = p_id

    # def __str__(self):
    #     return f"{self.name} {self.age} {self.p_id}"
        
x = passenger("yesha",27,1010)
print(x.name)
print(x.age)
print(x.p_id)

