import sklearn.datasets
import matplotlib.pyplot as pit

digits = sklearn.datasets.load_digits()

for i in range(50):
    pit.subplot(5, 10, i + 1)
    pit.axis("off")
    pit.title(digits.target[i])
    pit.imshow(digits.images[i], cmap="Greys")

pit.show()
