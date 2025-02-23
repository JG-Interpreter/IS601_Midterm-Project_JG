import json

class DosaOrderParse():
    """
        order_parse function: entire function reads in json file (filename as arguement) from Dosa restuarant and performs two operations. 
        The first operation reads customer info and outputs another json file with phone # and customer name. 
        Second operation reads items ordered and outputs a json file with oder item name, price of item, and count of orders of such type. 
    """
    def order_parse(filename):
        try: 
            with open(filename, 'r') as f:
                data = json.load(f)

            #check if data in list (json array format)
            if not isinstance(data, list) or not data:
                print("Error: Input JSON file does not contain a valid array.")
                return
        
        except FileNotFoundError: print(f"Error: Input file '{filename}' not found.")
        except json.JSONDecodeError: print(f"Error: Invalid JSON format in '{filename}'.")
        
        """
            Customers.json output: establish customer info as an empty dictionary. When reading the JSON file, 
            identfy instances of a dictionary with name and phone as keys. Combine the two objects with phone as key and
            name as value for output to new json using the 'w' write mode. 
        """
        customer_info = {}
        for item in data:
            if isinstance(item, dict) and 'name' in item and 'phone' in item:
                customer_info[item['phone']] = item['name']
            else:
                print("Warning: One or more entries in the input JSON is not in the expected format.")
        
        with open('customers.json', 'w') as f:
            json.dump(customer_info, f)

        """
            items.json output: create another empty dictionary. Since items are an array nested within json a dictionary, 
            iterate trhough each order and identify instances of item lists inside of each dictionary format. 
            Identify keys: name and store as new dictionary key. 
            Next, price and count of orders will nested as a dictionay within each order dictionary occurence.
            lastly, output will be written to a new json using using the 'w' write mode. 
        """
        orders = {}
        for order_data in data:
            if isinstance(order_data, dict) and 'items' in order_data and isinstance(order_data['items'], list):
                for item in order_data['items']:
                    if isinstance(item, dict) and 'name' in item and 'price' in item:
                        item_name = item['name']
                        item_price = item['price']
                        if item_name in orders:
                            orders[item_name]['orders'] += 1
                        else:
                            orders[item_name] = {'price': item_price, 'orders': 1}
                    else:
                        print("Warning: One or more item entries is not in the expected format.")
            else:
                print("Warning: One or more customer entries is missing 'items' or 'items' is not a list.")
       
        with open('items.json', 'w') as f:
            json.dump(orders, f)

        




            
