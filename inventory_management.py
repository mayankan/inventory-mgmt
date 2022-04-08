"""

    @Author: Mayank Anand
    @Date: 2022-04-08
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-04-08
    @Title : JSON Inventory Management of Rice, Pulses and Wheat Inventory

"""
import json


def create_inventory():
    """
    Description: 
        Create Dictionary with list values containing name, weight and price per kg of Inventory values.
    Parameter:
        None.
    Return:
        Inventory Dictionary with list values containing name, weight and price per kg of Rice, Pulses and Wheat inventory.
    """
    inventory = {'Rice': []}
    inventory['Rice'].append({
        'name': 'Sharbati',
        'weight_kg': 10,
        'price_per_kg': 1000
    })
    inventory['Rice'].append({
        'name': 'Basmati',
        'weight_kg': 10,
        'price_per_kg': 1500
    })
    inventory['Rice'].append({
        'name': 'Ankur',
        'weight_kg': 10,
        'price_per_kg': 500
    })

    inventory['Pulses'] = []
    inventory['Pulses'].append({
        'name': 'Groundnuts',
        'weight_kg': 10,
        'price_per_kg': 200
    })
    inventory['Pulses'].append({
        'name': 'Peanuts',
        'weight_kg': 10,
        'price_per_kg': 100
    })
    inventory['Pulses'].append({
        'name': 'Green peas',
        'weight_kg': 10,
        'price_per_kg': 150
    })

    inventory['Wheat'] = []
    inventory['Wheat'].append({
        'name': 'Rahet',
        'weight_kg': 10,
        'price_per_kg': 100
    })
    inventory['Wheat'].append({
        'name': 'Karet',
        'weight_kg': 10,
        'price_per_kg': 200
    })
    inventory['Wheat'].append({
        'name': 'Shahet',
        'weight_kg': 10,
        'price_per_kg': 300
    })
    return inventory


def write_json(file_name, inventory_data):
    with open(file_name, "w") as json_file:
        json.dump(inventory_data, json_file, indent=4, sort_keys=True)


def read_json(file_name):
    with open(file_name) as json_file:
        inventory_data = json.load(json_file)
        inventory_list = ['Rice', 'Pulses', "Wheat"]
        total_list_amt = [0, 0, 0]
        for inventory_cat in range(len(inventory_list)):
            total_amt = 0
            for each_inventory in inventory_data[inventory_list[inventory_cat]]:
                total_amt = total_amt + (each_inventory['price_per_kg'] * each_inventory['weight_kg'])
            total_list_amt[inventory_cat] = total_amt
        return total_list_amt

def main():
    data = create_inventory()
    write_json("test.json", data)
    inventory_total_price = read_json("test.json")
    inventory_list = ['Rice', 'Pulses', "Wheat"]
    for inventory_total in range(len(inventory_total_price)):
        print(f"Total Amount for {inventory_list[inventory_total]} is Rs." \
        f"{inventory_total_price[inventory_total]}")


if __name__ == "__main__":
    main()
