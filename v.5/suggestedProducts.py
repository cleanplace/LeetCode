
class Solution:
    def suggestedProducts(self, products, searchWord):
        result = []
        products.sort()
        for i, c in enumerate(searchWord):
            products = [ p for p in products if len(p) > i and p[i] == c ]
            result.append(products[:3])
        return result


if __name__ == "__main__":
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    s = Solution()
    print(s.suggestedProducts(products,searchWord))