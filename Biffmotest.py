import math
import datetime as dt

#  Här kan en kommentera
#  This variable contains an integer
quantity = 5
#  This variable contains a float
unit_price = 123.45
#  This variable contains the result of multiplying quantity times unit price
extended_price = quantity * unit_price
#  Show the results
print(extended_price)

first_name = "Markus\nDolores\nPino"
last_name = "\nHölbling"
print(first_name, last_name)

x = -4
y = abs(x)
print(x)
print(y)

a = 4.453423345645439587645326783949587463
b = round(a, 1)
print(a)
print(b)

c = -345.45678
print(int(abs(c)))

sqrt = math.sqrt
print(sqrt(84567))

pi = math.pi
print(pi)

username = "Lilo"
print(f"Hello {username}")

unit_price = 49.99
quantity = 30
print(f"Subtotal: ${quantity * unit_price:,.2f}")

sales_tax_rate = 0.065
print(f"Sales Tax Rate {sales_tax_rate:.1%}")

namn1 = "Ellen"
namn2 = "Dolores"
namn3 = "Markus"
output = f"""
{namn1}

{namn2}

{namn3}
"""
print(output)

kostnad = 412
kvantitet = 54
moms = 0.32
subtotal = kostnad * kvantitet
skatt = subtotal * moms
total = subtotal + skatt

s_subtotal = f"{subtotal:.2f}" + "€"
s_skatt = f"{skatt:.2f}" + "€"
s_brutto = f"{total:.2f}" + "€"

utdata = f"""
Subtotal:   {s_subtotal:>10}
Moms:       {s_skatt:>10}
Brutto:     {s_brutto:>10}
"""
print(utdata)

print(hex(255))

x = 300
print(bin(x))
print(oct(x))
print(hex(x))

print(0b100101100)
print(0o454)
print(0x12c)

print(len(s_brutto))

s = "esrdfaAtgyhuijokpl"
print("t" in s)
print("h" not in s)
print("H" not in s)
print(s * 100)
print(s[14])
print(s[5:20])
print(s[5:10:20])
print(min(s))
print(max(s))
# The total number of times string x appears in larger string s.

print(ord("g"))
print(chr(103))

p = "gyjbgyujbgyujnbgyujbhyujnbhyujhujh"
print(p.capitalize())
print(p.count("j"))
print(p.islower())
print(p.lower())

today = dt.date.today()
print(today)
print(today.month)
print(f"{today:%A, %B %d, %Y}")
print(f"{today:%a, %B %d, %Y}")
print(f"{today:%Y, %d %b, %H, %M, %S}")
print(f"{today:%d/%m/%Y}")
print(f"{today:%a, %b %d %Y}")
print(f"{today:%x}")
print(f"{today:%A %B %d is day number %j of %Y}")

right_now = dt.datetime.now()
print(right_now)
print(f"{right_now:%H:%M:%S and %f microseconds}")
print(f"{right_now:%X}")
print(f"{right_now:%c}")

new_years_day = dt.date(2019,1,1)
memorial_day = dt.date(2019,5,27)
days_between = memorial_day - new_years_day
print(days_between)
