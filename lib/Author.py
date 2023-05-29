class Author:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    

author = Author("Albert Joseph")

print(author.get_name())