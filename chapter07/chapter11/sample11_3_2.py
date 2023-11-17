import xml.etree.ElementTree as et

tree = et.parse("sample11_3.xml")
root = tree.getroot()
print(f"ルート要素のタグ名:{root.tag}")
print(f"ルート直下の要素数:{len(root)}")

for person in root:
    name=person.find("name").text
    age=person.find("age").text
    gender=person.find("gender").text
    print(f"名前:{name},年齢:{age},性別:{gender}")