import json
import requests


def main():
    cocktail_by_name = get_cocktail_by_name()
    print(cocktail_by_name)




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





if __name__ == "__main__":
    main()