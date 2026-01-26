def add_vat (price , vat_rate) : 
    return price * (100 + vat_rate)/100

orders = [10 , 20 , 30]

for price in orders:
    finalAmount = add_vat(price , 5)
    print(f"before VAT {price} : after VAT {finalAmount}")

