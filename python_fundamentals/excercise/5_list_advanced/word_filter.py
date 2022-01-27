some_text = input().split()

print("\n".join([word for word in some_text if len(word) % 2 == 0]))
