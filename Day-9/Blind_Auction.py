
from art import logo
print(logo)
new_bids = True
user_data = {}
while new_bids:
    name = input("What is your name?\n")
    price = int(input("What is your price?\n$"))

    user_data[name] = price
    new_bidder = input("Is there any other bidder?(Y/N)\n").lower()
    if new_bidder == "n":
        new_bids = False
    elif new_bidder == "y":
        print("\n" * 30)

max_value = max(user_data, key = user_data.get)

print(f"{max_value} is the max bidder with a price of {user_data[max_value]}" )

