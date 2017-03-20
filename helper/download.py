import urllib.request

for i in range(10,69):
    file= "obw{}.xls".format(i)
    url = "http://prezydent2000.pkw.gov.pl/gminy/obwody/"+file
    file_path = "C:\\zawadzkm\\www\\zad1\\data\\"+file
    urllib.request.urlretrieve(url, file_path)
    print(file_path)