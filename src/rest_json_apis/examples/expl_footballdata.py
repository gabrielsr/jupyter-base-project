# python src/rest_json_apis/examples/test_api_wrapper.py

from __init__ import setup_path
setup_path()

from rest_json_apis.footballdata import competitions, matches, players, teams

# list competitions
print("competionts >>")
c = competitions({})
print(c)

# list matches
print("matches >>")
m = matches({})
print(m)

# list teams
print("teams >>")
t = teams({})
print(t)


