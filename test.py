from mock_data import mock_data

class Dog:
    def __init__(self, name):
        self.name = name


me = {
    "name" :"Andrew",
    "last" : "Singo",
    "email" : "test@email.com",
    "age" : 32,
    "hobbies" : [],
    "address" : {
        "street" : "main",
        "number" : "100"
    }

}

def print_data ():
    print(me["name"])
    print(me["name"] + " " + me["last"])

    # creat an object of Dog class
    fido = Dog("Fido")
    print(fido.name)

    # print_data()

def test_list():
        print("Working with lists")
        names = []

        # add elements to list
        names.append("Sergio")
        names.append("Angel")
        names.append("Andrew")

        print(names)

        # get elements from a list
        print(names[0])

        for name in names:
            print(name)

# test_list()

def product_search():
    print("search a product in the catalog")
    id = "test-id"


    found = False
    for prod in mock_data:
        if prod["_id"] == id:
            found = True
            print(prod)
            return prod

    if not found:
        print("Error: Product not found")        
        return None

product_search("test-id")
product_search("123")

