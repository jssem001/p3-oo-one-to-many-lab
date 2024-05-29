class Pet:
    all=[]
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    def __init__(self,name,pet_type,owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self.__pet_type

    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type in Pet.PET_TYPES:
            self.__pet_type = pet_type
        else:
            raise Exception(f"{pet_type} is not a valid pet type")

class Owner:
    def __init__(self,name):
        self.name = name