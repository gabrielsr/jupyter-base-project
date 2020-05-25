# python src/rest_json_apis/examples/world-population_kapsarc.py

from __init__ import setup_path
setup_path()

from rest_json_apis.world_population_kapsarc import world_population

# world population
print("world_population >>")
c = world_population({})
print(c)
print(c.columns)

