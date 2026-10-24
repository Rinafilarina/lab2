import xml.dom.minidom as minidom

xml_file = open('currency.xml')
xml_data = xml_file.read()
dom = minidom.parseString(xml_data)
dom.normalize()

valutes = dom.getElementsByTagName('Valute')
currency_dict = {}

for valute in valutes:
    char_code = valute.getElementsByTagName('CharCode')[0].firstChild.nodeValue
    name = valute.getElementsByTagName('Name')[0].firstChild.nodeValue
    value_str = valute.getElementsByTagName('Value')[0].firstChild.nodeValue
    value_float = float(value_str.replace(',', '.'))
    currency_dict[char_code] = {
        'name': name,
        'value': value_float
    }


xml_file.close()


for code, info in list(currency_dict.items())[:5]:
    print(f"{code}: {info['name']} — {info['value']} руб.")