import sklearn.datasets
import matplotlib.pyplot as pit

digits = sklearn.datasets.load_digits()

print("データの個数＝", len(digits.images))
print("画像データ＝", digits.images[8])
print("何の数字か＝", digits.target[8])

pit.imshow(digits.images[9], cmap="Greys")
pit.show()
