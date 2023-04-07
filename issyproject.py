f = input("Hello, may I know your name? ")
print("Hi", f, "you are playing a choose your own adventure game.")
print("This serves as a method for us to know you more.")
print("We would like for you to choose one of the following courses of action given this scenario.")
print("Right now, you find yourself hungry, what would you like to eat? Pick from the list.")
print()
print("hamburger")
print("apple")
print("parfait")
u = False
p = False
print()
while u == False:
    x = input("Which would you like to pick? ")
    if x == "hamburger":
        print()
        print("You now have acquired the hamburguer. When we found you, you also had a few more items in your posession, we shall list everything:")
        print()
        y = ("hamburguer")
        a = "10 dollars"
        b = "keychains"
        c = "cellphone"
        d = "napkin"
        z = ("bracelet")
        items = [y,a,b,c,d,z]
        print(items)
        u = True
    if x == "apple":
        print("You now have acquired an apple. When we found you, you also had a few more items in your posession, we shall list everything:")
        print()
        y = ("apple")
        a = "10 dollars"
        b = "keychains"
        c = "cellphone"
        d = "napkin"
        z = ("bracelet")
        items = [y,a,b,c,d,z]
        print(items)
        u = True
    if x == "parfait":
        print("Amazing choice! You now have acquired a parfait. We would like to praise you for correctly choosing the best option.")
        print("When we found you, you also had a few more items in your posession, we shall list everything, plus a second parfait for choosing the best food:")
        print()
        y = ("2 parfaits")
        a = "10 dollars"
        b = "keychains"
        c = "cellphone"
        d = "napkin"
        z = ("bracelet")
        items = [y,a,b,c,d,z]
        print(items)
        u = True
print("Now, you can go.")
print("Before leaving, though, I'd appreciate if you'd say your last interaction with me:")
print("hug")
print("handshake")
print("furious glance")
o = "pen"
itemsa = [y,a,b,c,d,z,o]
itemsb = [a,b,c,d,z]
while p == False:
    x = input("Which would you like to do? ")
    if x == "hug":
        print("Good. You win a pen. Now you have the following items:")
        print()
        print(itemsa)
        p = True
        print("Goodbye, it was a pleasure.")
    if x == "handshake":
        print("Goodbye, It was a pleasure. Here are all your items back.")
        p = True
        print(items)
    if x == "furious glance":
        print("Goodbye, I am sorry for any inconveniences. We will have to take your food away.")
        print()
        print(itemsb)
        print()
        print("It was a pleasure.")
        p = True
input("Select Enter to exit.")