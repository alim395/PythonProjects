# Good Morning Canada by Ali Mohamed(251192600)
print('Good Morning Canada!\n')


# Input Formatting Function
def format_input(text_line):
    text_line = text_line.lower().strip()
    word_list = text_line.split()
    text_line = "".join(word_list)
    return text_line


# Variables
breakfast_item = ["egg", "bacon", "sausage", "hashbrown", "toast", "coffee", "tea", "smallbreakfast", "regularbreakfast", "bigbreakfast"]  # list of items
breakfast_price = [0.99, 0.49, 1.49, 1.19, 0.79, 1.49, 1.09]  # list of prices for individual components
small_breakfast = breakfast_price[0] + breakfast_price[3] + (2 * breakfast_price[4]) + (2 * breakfast_price[1]) + breakfast_price[2]
regular_breakfast = (2 * breakfast_price[0]) + breakfast_price[3] + (2 * breakfast_price[4]) + (4 * breakfast_price[1]) + (2 * breakfast_price[2])
big_breakfast = (3 * breakfast_price[0]) + (2 * breakfast_price[3]) + (4 * breakfast_price[4]) + (6 * breakfast_price[1]) + (3 * breakfast_price[2])
order_items = []  # list to store items
item_id = 0  # keeps track of items
order_prices = []  # list to store price of ordered items
ordering = ""  # temporarily holds requested item
quantifying = "0"  # temporarily holds quantity of requested item

while ordering != "q":
    count = 0
    verify = True
    ordering = str(input("What would you like to order?(Type 'q' to finish): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea\n"))
    ordering = format_input(ordering)
    while ordering != breakfast_item[count] and ordering != "q":  # Validates the requested item
        if count < 9:
            count += 1
        else:
            count = 0
            verify = False
            ordering = str(input("Item not found, please try again.(Type 'q' to finish) \n"))
            ordering = format_input(ordering)
        verify = True
    if verify:
        if ordering == "q":
            break
        else:
            order_items.append(ordering)
            quantifying = str(input("How many?\n"))
            while not quantifying.isdigit() or quantifying == "0":  # appends the correct price(s) based on requested item and quantity
                quantifying = str(input("Invalid Input. Please Try again?\n"))
            quantifying = float(quantifying)
            if order_items[item_id] == breakfast_item[0]:
                order_prices.append(quantifying * breakfast_price[0])
            elif order_items[item_id] == breakfast_item[1]:
                order_prices.append(quantifying * breakfast_price[1])
            elif order_items[item_id] == breakfast_item[2]:
                order_prices.append(quantifying * breakfast_price[2])
            elif order_items[item_id] == breakfast_item[3]:
                order_prices.append(quantifying * breakfast_price[3])
            elif order_items[item_id] == breakfast_item[4]:
                order_prices.append(quantifying * breakfast_price[4])
            elif order_items[item_id] == breakfast_item[5]:
                order_prices.append(quantifying * breakfast_price[5])
            elif order_items[item_id] == breakfast_item[6]:
                order_prices.append(quantifying * breakfast_price[6])
            elif order_items[item_id] == breakfast_item[7]:
                order_prices.append(quantifying * small_breakfast)
            elif order_items[item_id] == breakfast_item[8]:
                order_prices.append(quantifying * regular_breakfast)
            elif order_items[item_id] == breakfast_item[9]:
                order_prices.append(quantifying * big_breakfast)
            item_id += 1

print("RECEIPT")  # prints receipts
format_receipt = '{item:<16}${price:>5.2f}'
print(format_receipt.format(item="COST", price=sum(order_prices)))
print(format_receipt.format(item="TAX", price=0.13 * sum(order_prices)))
print(format_receipt.format(item="TOTAL", price=1.13 * sum(order_prices)))
