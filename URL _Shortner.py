class URLShortener:
    def __init__(self):
        self.id = 0
        self.short_to_long = {}
        self.long_to_short = {}

    def encode(self, long_url):
        # Check if URL is already shortened
        if long_url in self.long_to_short:
            return f"http://short.url/{self.long_to_short[long_url]}"

        # Generate a new ID and convert to Base 62
        self.id += 1
        short_code = self.to_base62(self.id)

        # Store in hash maps
        self.short_to_long[short_code] = long_url
        self.long_to_short[long_url] = short_code

        return f"http://short.url/{short_code}"

    def decode(self, short_url):
        short_code = short_url.split("/")[-1]
        return self.short_to_long.get(short_code, "URL not found")

    def to_base62(self, num):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        result = []
        while num > 0:
            result.append(chars[num % 62])
            num //= 62
        return "".join(reversed(result))

# Example Usage
shortener = URLShortener()
short_url = shortener.encode("https://www.example.com")
print("Short URL:", short_url)
print("Long URL:", shortener.decode(short_url))

