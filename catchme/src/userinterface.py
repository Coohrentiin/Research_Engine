from query import *

def get_request():
    return input("Enter your query (empty to quit): ")

def get_result(request):
    return HandleQuery(request)

print("Hello, welcome to catch_me")
request = get_request()
while len(request) > 0:
    j = 0
    for i in get_result(request):
        print(j + "- " + i)
        j += 1
    request = get_request()
print("Good bye")

