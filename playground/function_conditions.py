def computepay(h,r):
    if h <= 40:
        pay = 40 * r
    elif h > 40:
        pay = (40 * r) + (h - 40) * 1.5 * r

    return pay

    
hours = input("Enter Hours:")
rate = input("Enter Rate:")

print("Pay", computepay(float(hours), float(rate)))