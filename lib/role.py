from audition import Audition
class Role:

    all = []
    
    def __init__(self, character_name):
            self.character_name = character_name
            Role.all.append(self)
    
    def auditions(self):
        return [audition for audition in Audition.all if audition.role == self.character_name]
    
    def add_audition(self, audition):
        if not isinstance(audition, Audition):
            raise Exception("audition must be an instance of the audition class")
        audition.role = self  

    @property
    def character_name(self):
        return self._character_name
    
    @character_name.setter
    def character_name(self, new_character_name):
        if isinstance(new_character_name, str) and len(new_character_name) > 0:
            self._character_name = new_character_name
        else:
            raise Exception("name must be a string greater than 0 characters long")

    def __str__(self):
        return self.role   

    def actors(self):
        return [audition.actor for audition in self.auditions()]
    
    def locations(self):
        return [audition.location for audition in self.auditions()]

    def lead(self):
        return [audition for audition in self.auditions() if audition.hired][0]

    def understudy(self):    
        return [audition for audition in self.auditions() if audition.hired][1]

    def cast(self):
        return [audition for audition in self.auditions() if audition.hired]
    
    @classmethod
    def not_cast(cls):
        return [role for role in Role.all if not role.cast()]
        

anakin = Role("Anakin")
padme = Role("Padme")
obiwan = Role("Obiwan")
luke = Role("Luke")


print(luke.actors())
print(padme.locations())
print(anakin.lead())
print(Role.not_cast())
