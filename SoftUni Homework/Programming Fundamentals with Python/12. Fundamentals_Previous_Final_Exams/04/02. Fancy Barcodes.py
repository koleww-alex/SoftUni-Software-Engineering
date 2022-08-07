import re
number_of_iterations = int(input())
pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'
pattern_for_digits = r'\d+'
for _ in range(number_of_iterations):
    current_barcode = input()
    match = re.findall(pattern, current_barcode)
    if match:
        valid_barcode = ''.join(match)
        list_of_digits = re.findall(pattern_for_digits, valid_barcode)
        if list_of_digits:
            number = ''.join(list_of_digits)
            print(f'Product group: {number}')
        else:
            print('Product group: 00')
    else:
        print('Invalid barcode')
