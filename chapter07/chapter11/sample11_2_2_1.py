import csv

with open("sample11_2_.csv","w",newline="")as f:
    cout=csv.DictWriter(f,["name","age","gender"])
    cout.writeheader()
    cout.writerow({"name":"Alice","age":23,"gender":"F"})
    cout.writerow({"name":"Bob","age":31,"gender":"F"})
    cout.writerow({"name":"Charlie","age":26,"gender":"M"})