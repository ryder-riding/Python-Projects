def get_milk_money(money,product,product_price,product_qty,shop_name):
    print(f" i will buy {product} from {shop_name} and i am taking {money} rs")
    total_bill = product_price * product_qty
    return_money = money - total_bill
    print(f"and i am giving you {return_money} amount back")