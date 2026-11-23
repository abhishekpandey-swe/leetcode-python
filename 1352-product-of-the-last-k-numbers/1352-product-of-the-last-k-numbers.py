class ProductOfNumbers:

    def __init__(self):
        # Use a list to store every number added to the stream
        self.stream = []

    def add(self, num: int) -> None:
        # Simply append the number to our list
        self.stream.append(num)

    def getProduct(self, k: int) -> int:
        # Start with 1 (since it's multiplication)
        product = 1
        
        # Slice the last k elements from the list
        last_k_elements = self.stream[-k:]
        
        # Multiply them all together
        for num in last_k_elements:
            product *= num
            
        return product