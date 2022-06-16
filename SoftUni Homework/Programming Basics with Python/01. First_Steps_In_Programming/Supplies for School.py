package_of_pens = int(input())
package_of_markers = int(input())
package_of_detergent = int(input())
percent_discount = int(input()) / 100
pens = 5.8
markers = 7.2
detergent = 1.2
final_sum_before_discount = (package_of_pens * pens) + (package_of_markers * markers) + (package_of_detergent * detergent)
discount = final_sum_before_discount * percent_discount
final_sum = final_sum_before_discount - discount
print(final_sum)
