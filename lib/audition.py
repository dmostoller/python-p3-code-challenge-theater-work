class Audition:

    all = []
    
    def __init__(self, role, actor, location, phone, hired = False):
        self._actor = actor
        self._location = location
        self._phone = phone
        self._hired = hired
        self._role = role
        Audition.all.append(self)
   
    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, value):
        from role import Role
        if not isinstance(value, Role):
            raise Exception("role must be an instance of the role class")
        self._role = value

    @property
    def actor(self):
        return self._actor
    
    @actor.setter
    def actor(self, actor):
        if isinstance(actor, str) and 3 < len(actor) < 20:
            self._actor = actor
        else:
            raise Exception("must be string between 3 and 20 characters")

    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        self._location = location

    @property
    def phone(self):
        return self.phone
    
    @actor.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def hired(self):
        return self._hired
    
    @hired.setter
    def hired(self, hired):
        self._hired = hired

    def call_back(self):
        self._hired = True     

    def __str__(self):
        return self.actor

first = Audition("Padme", "Liz", "NYC", "555-555-5555")
second = Audition("Anakin", "John", "LA", "666-666-6666")
third = Audition("Anakin", "Merv", "SF", "456-888-0987")
fourth = Audition("Luke", "Scott", "Philly", "632-986-9843")
fifth = Audition("Anakin", "Tim", "Burlington", "666-666-6666")
sixth = Audition("Padme", "Alice", "Reno", "456-888-0987")
seventh = Audition("Luke", "Peter", "Atlanta", "632-986-9843")
eigth = Audition("Luke", "Will", "Asheville", "632-986-9843")
ninth = Audition("Padme", "Lily", "Miami", "456-888-0987")
tenth = Audition("Obiwan", "Jason", "Sacramento", "456-888-0987")



second.call_back()
fifth.call_back()
sixth.call_back()

# for audition in Audition.all:
#     print(audition)
