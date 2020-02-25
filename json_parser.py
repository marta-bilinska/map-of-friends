import json


def read_json_file(f_path):
    """
    () -> dict
    This function reads the json file
    into the dictionary.
    """
    with open(f_path) as f:
        data = json.load(f)
    return data

def parse_data_from_dict(dictionary):
    """
    (dict,str)
    This function makes a dictionary of the information
    about the given class.
    """
    print("Please choose the key (all of the available options below): ")
    for i in dictionary:
        print(i)
    first = True
    key = input("Type a key: ")
    iterable = dictionary
    while key not in ['exit', 'e']:
        if first == False:
            key = input("Type a key: ")
            try:
                key = int(key) - 1
            except TypeError:
                pass
            except ValueError:
                pass
        try:
            iterable = iterable[key]
        except KeyError:
            print("You have inputted a wrong key.")
            break
        if keys_from_dict(iterable) != 'exit':
            pass
        else:
            break
        first = False


def keys_from_dict(iterable):
    """
    (list) -> str
    This function prints out the
    options of iterable's key for the user to choose.
    """
    if type(iterable) == list:
        if len(iterable) == 0:
            print("[]")
        else:
            print("There is a list of", len(iterable), "item.\nWhich item would you like to see? ")
    elif type(iterable) == dict:
        for i in list(iterable.keys()):
            print(i)
    else:
        print(iterable)
        return "exit"


if __name__ == "__main__":
    parse_data_from_dict(read_json_file('example.json'))
