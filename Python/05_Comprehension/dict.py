chaiPriceInr = {
    "masala-chai" : 30,
    "green-tea" : 400,
    "lemonTea" : 10
}

chaiPriceUsd = { chai:price*80 for chai, price in chaiPriceInr.items()}

print(f"{chaiPriceUsd}")