def listManipulation(_list , order):
    even_list =[] 
    odd_list =[] 
    if order:
        _list.sort()
        # print(_list)
        for items in _list:
            if items.isdigit():
                if int(items) % 2 == 0 :
                    even_list.append(items)
                else:
                    odd_list.append(items)
            else:
                print("Entered invalid Number")
                return
        print(f"Sorted Ascending Even List : {even_list} and Odd List : {odd_list} ")
    else:
        _list.sort(reverse = True)
        for items in _list:
            if items.isdigit():
                if int(items) % 2 == 0 :
                    even_list.append(items)
                else:
                    odd_list.append(items)
            else:
                print("Entered invalid Number")
                return
        print(f"Sorted Descending Even List : {even_list} and Odd List : {odd_list} ")

input_string = input("Enter a list value separated by comma(,)").strip()
_list = input_string.split(",");
# print(_list)

order = True
input_order = input("Enter 'A' for Ascending and 'D' for Descending order : ")
if input_order.lower() == 'a':
    order = True
elif input_order.lower() == 'd':
    order = False
else:
    print("No input match taking ascending order")

listManipulation(_list , order)