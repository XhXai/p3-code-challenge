class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.all_magazines.append(self)

    def get_name(self):
        return self.name
    
    def get_category(self):
        return self.category
    

    @classmethod
    def all(cls):
        return cls.all_magazines
    

# Create magazine instances
magazine1 = Magazine("Magazine A", "Category Y")
magazine2 = Magazine("Magazine B", "Category X")
magazine3 = Magazine("Magazine C", "Category Z")

#Get the name and category of magazine1
print(magazine1.get_name())
print(magazine1.get_category())

#Get the list of all magazine instances
all_magazines = Magazine.all()
for magazine in all_magazines:
    print(magazine.get_name(), magazine.get_category())