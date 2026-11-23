class ProductOfNumbers:
    def __init__(self):
        # Initialize with 1 to simplify multiplication logic
        self.prefix_products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # A zero resets the product chain
            self.prefix_products = [1]
        else:
            # Append the cumulative product
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k is larger than the non-zero suffix, a zero is in range
        if k >= len(self.prefix_products):
            return 0
        
        # Product of last k numbers = (total product) / (product before the k numbers)
        return self.prefix_products[-1] // self.prefix_products[-k - 1]