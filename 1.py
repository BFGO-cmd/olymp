v = int(input())
a = int(input())
b = int(input())
n = int(input())
water_in = n // a
water_out = n // b
final_volume = v + water_in - water_out
print(final_volume)