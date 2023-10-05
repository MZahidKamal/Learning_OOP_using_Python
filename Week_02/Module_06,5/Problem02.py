#-----------------------------------------------------------------------------------------------------------------------
# Python Week 2 Practice Day 01
# https://docs.google.com/document/d/1oz0kZt1_XdofqfxH0qeiNYTkpUmvLyma0Pdf4CeMkig/edit
# Problem 02: Inside the Shop class, create a method name add_product which adds products using the Product class to the
# Shop class.
#-----------------------------------------------------------------------------------------------------------------------

class Shop:
    def __init__(self, name, road, house_no, zip_code, city, state, country, owner, established_year):
        self.name = name
        self.road = road
        self.house_no = house_no
        self.zip_code = zip_code
        self.city = city
        self.state = state
        self.country = country
        self.owner = owner
        self.established_year = established_year
        self.books = []

    def shop_details(self):
        print()
        print('----- Shop Details -----')
        print(f'Owner: {self.owner}')
        print(f'Location: {self.city}, {self.state}, {self.country}')
        print(f'Established on: {self.established_year}')
        return '-----'

    def shop_location(self):
        print()
        print('----- Shop Address -----')
        print(f'Name: {self.name}')
        print(f'Address: {self.road} {self.house_no}, {self.zip_code} {self.city}, {self.state}, {self.country}')
        return '-----'

shBookStore = Shop('S & H Book Store', 'Central Train Station Road', 10, 60329, 'Frankfurt am Main', 'Hessen', 'Germany', 'Mr. Schmidt and Mr. Hahn', 1978)

print(shBookStore.shop_details())
print(shBookStore.shop_location())

#-----------------------------------------------------------------------------------------------------------------------

class Book:
    def __init__(self, name, author, isbn, edition, published_on, publisher):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.edition = edition
        self.published_on = published_on
        self.publisher = publisher
        self.selling_stores = []

    def book_details(self):
        print('----- Book Details -----')
        print(f'Title: {self.name}')
        print(f'Author: {self.author}')
        print(f'Edition: {self.edition}, ISBN: {self.isbn}')
        print(f'Published on: {self.published_on}, from {self.publisher} Publishers')
        return '-----'


theLearnStartup = Book('The Lean Startup', 'Eric Ries', '978-0307887894', '1st', '2011-09-13', 'Crown Business')
zeroToOne = Book('Zero to One', 'Peter Thiel', '978-0804139298', '1st', '2014-09-16', 'Crown Business')
goodToGreat = Book('Good to Great', 'Jim Collins', '978-0066620992', '1st', '2001-10-16', 'Harper Business')
theInnovatorsDilemma = Book('The Innovator\'s Dilemma', 'Clayton Christensen', '978-1633691780', '1st', '1997-05-01', 'Harper Business')
thinkingFastAndSlow = Book('Thinking, Fast and Slow', 'Daniel Kahneman', '978-0374533557', '1st', '2011-10-25', 'Farrar, Straus and Giroux')

print(theLearnStartup.book_details())
