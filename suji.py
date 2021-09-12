import sklearn.datasets

digits = sklearn.datasets.load_digits()

print("Data =", len(digits.images))
print("Image Data=", len(digits.images[0]))
print("What Number", len(digits.target[0]))
