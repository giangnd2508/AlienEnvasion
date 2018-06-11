prompt_type = "\nWhich type of pizza do you want: "
prompt_size = "\nWhich size?: "
prompt_topping = "\nWhich topping do you want "
prompt_continue = "\nDo you want to continue order (yes/no) "

active = True
continue_order = 'yes'
order = {}


while active:
    if continue_order != 'no':
        active = True
        type_order = input(prompt_type)
        order['Type'] = type_order
        size = input(prompt_size)
        order['Size'] = size
        topping = input(prompt_topping)
        order['Topping'] = topping
        continue_order = input(prompt_continue)
        print("\nYou order a pizza " + type_order.upper() + ", size " + size + " with topping " + topping)
        print(order)
    else:
        active = False
