def linearSearchProduct(productList, targetProduct):
    indices = []
    for Index, product in enumerate(productList):
        if product == targetproduct:
            indices.append(index)
    return indices
products = ["Apple", "Banana", "Orange", "Grapes", "Apple", "Grapes","Apple"]
target1 = "Apple"

result = linearSearchProduct(products, target)
print(result)