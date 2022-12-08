mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}
# Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT
#   Your Code Starts from here

# for mobile in mobile_data:
for mobile in mobile_data.get('data'):

    name = mobile.get('name')
    made = mobile.get('made')
    price = mobile.get('price')
    price_to_float = float(price.replace("USD",' '))
    usd_to_bdt = mobile_data.get('exchnage_rate')*price_to_float
    sentence = f'The {name} is made in the {made} and available for purchase at the {price}, which equivalent to approximatel {usd_to_bdt} BDT'

    print(sentence)