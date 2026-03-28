item = input("What is the item? ")
quantity = int(input("What is the quantity? "))
price = float(input("What is the price per unit? "))

def bill():
    total = price * quantity
    gst = 0.18 * total
    grand_total = total + gst

    print(f"Item     : {item}")
    print(f"Quantity : {quantity}")
    print(f"Price    : ₹{price:.2f} each")
    print(f"Total    : ₹{total:.2f}")
    print(f"GST(18%) : ₹{gst:.2f}")
    print(f"Grand Total: ₹{grand_total:.2f}")

bill()
