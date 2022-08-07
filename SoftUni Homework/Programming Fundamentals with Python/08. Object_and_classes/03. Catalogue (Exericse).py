class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):

        return [product_name for product_name in self.products if product_name.startswith(first_letter)]

    def __repr__(self):
        unpacked_products = "\n".join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n{unpacked_products}"
