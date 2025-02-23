import json

class DosaOrderParse():
    """
        Explain context of code
    """

    def order_parse(filename):
        try: 
            with open(filename, 'r') as f:
                data = json.load(f)

            if not isinstance(data, list) or not data:
                print("Error: Input JSON file does not contain a valid array.")
                return
        
        except FileNotFoundError: print(f"Error: Input file '{filename}' not found.")
        except json.JSONDecodeError: print(f"Error: Invalid JSON format in '{filename}'.")
        
        """
            Explain code block below
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
            Explain code block below
        """
        orders = {}
        for order_data in data:
            if isinstance(order_data, dict) and 'items' in order_data and isinstance(order_data['items'], list):
                for item in order_data['items']:
                    if isinstance(item, dict) and 'name' in item and 'price' in item:
                        # orders[item['name']] = item['price']
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

        




            
