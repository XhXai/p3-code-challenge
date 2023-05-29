class Article:
    all_articles = []


    def __init__ (self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.all_articles.append(self)

    def get_title(self):
        return self.title
    

    @classmethod
    def all(cls):
        return cls.all_articles
    

#Create article instances
article1 = Article("Author A", "Magazine A", "Article A")
article2 = Article("Author B", "Magazine B", "Article B")


print(article1.get_title())

#Get the list off all article instances.
all_articles = Article.all()
for article in all_articles:
    print(article.get_title())