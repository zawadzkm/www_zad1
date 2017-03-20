import os, sys, pandas, time
from classes.country import Country

df = pandas.read_csv(os.path.join(os.path.join(os.path.dirname(sys.argv[0]), "data"), "data.csv"), sep=";")
df["Frekwencja"] = round(df["Oddane"]*100/df["Uprawnieni"], 2)

all_time = time.time()
poland = Country(df)
start_time = time.time()
poland.load()
print("-- %s seconds load --" % (time.time() - start_time))

start_time = time.time()
poland.render()
print("-- %s seconds render --" % (time.time() - start_time))
print("-- %s seconds all --" % (time.time() - all_time))
