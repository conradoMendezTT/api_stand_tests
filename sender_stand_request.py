import configuration
import requests
import data


def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def get_logs(number_of_params):
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count" : number_of_params})

def get_user_table():
    return  requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH ,
                     json= body,
                     headers= data.headers    )

def post_products_kits(products_ids):
    return  requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                          json= products_ids,
                          headers= data.headers)


response = get_user_table()
print(response.status_code)

print("Starting from here with status and request URL")
response_logs = get_logs(50).url
print("La url utilizada a la que le estamos haciendo un request de los logs es: " , response_logs)


print("Starting from here with USER")
response = post_new_user(data.user_body)
print(response.status_code)
print(response.ok)
print(response.json())


print("Starting from here with KITS")
response = post_products_kits(data.product_ids)
print(response.status_code)
print(response.json())
