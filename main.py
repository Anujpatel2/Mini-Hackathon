import json
import requests


def main():
    cocktail_by_name = get_cocktail_by_name()

    for key in cocktail_by_name.keys():
        for items in cocktail_by_name[key]:
            for key2 in items:
                print(key2 + ": " +str(items[key2]))

    print("***********************************************************")

    ingredients_by_name=get_ingredients_by_name()
    for key in ingredients_by_name.keys():
        for items in ingredients_by_name[key]:
            for key2 in items:
                print(key2 + ": " + str(items[key2]))

    print("***********************************************************")


    full_details=get_full_cocktail_details()

    for key in full_details.keys():
        for items in full_details[key]:
            for key2 in items:
                print(key2 + ": " + str(items[key2]))

    print("***********************************************************")

    print(get_random_cocktail())





def get_cocktail_by_name():
    name = str(input("Enter the name of the drink: "))

    api_token = 1
    api_url_base = "https://www.thecocktaildb.com/api/json/v1/1/search.php?i=" + name

    headers = [u'drinks']

    api_url = format(api_url_base)

    response = requests.get(api_url_base)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def get_ingredients_by_name():
    ingredient = str(input("Enter the name of the ingredient: "))

    api_token = 1
    api_url_base = "https://www.thecocktaildb.com/api/json/v1/1/search.php?i=" + ingredient

    headers = [u'ingredients']

    api_url = format(api_url_base)

    response = requests.get(api_url_base)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def get_full_cocktail_details():
    fullDetails = str(input("Enter the name of the cocktail: "))

    api_token = 1
    api_url_base = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=" + fullDetails

    headers = [u'ingredients']

    api_url = format(api_url_base)

    response = requests.get(api_url_base)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def get_random_cocktail():

    api_token = 1
    api_url_base = "https://www.thecocktaildb.com/api/json/v1/1/random.php"

    headers = [u'ingredients']

    api_url = format(api_url_base)

    response = requests.get(api_url_base)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def get_ingredient():
    ingredient = str(input("Enter the name of the ingredient: "))

    api_token = 1
    api_url_base = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?i="+ingredient

    headers = [u'ingredients']

    api_url = format(api_url_base)

    response = requests.get(api_url_base)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None












if __name__ == "__main__":
    main()