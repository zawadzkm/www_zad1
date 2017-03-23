import os, sys, pandas, time
from classes.country import Country

df = pandas.read_csv(os.path.join(os.path.join(os.path.dirname(sys.argv[0]), "data"), "data.csv"), sep=";")
df["Frekwencja"] = round(df["Oddane"]*100/df["Uprawnieni"], 2)

all_time = time.time()
poland = Country(df)
start_time = time.time()
poland.load()
print("load: %s seconds" % round(time.time() - start_time, 2))

start_time = time.time()
poland.render()
print("render %s seconds" % round(time.time() - start_time, 2))
print("all: %s seconds" % round(time.time() - all_time, 2))
