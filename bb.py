import numpy as np
import matplotlib.pyplot as plt


def f(c, n=10):
    z = 0
    while n:
        yield z
        z = z ** 2 + c
        n -= 1
    return StopIteration


def draw(data, c, delta_real, delta_imag, size):
    z = c
    while abs(z) <= 4:
        row = int((z.real + 2) // delta_real)
        col = int((z.imag + 2) // delta_imag)

        if row > -1 and row < size and col > -1 and col < size:
            data[row][col] += 1
        z = z ** 2 + c


def is_stable(c, n=10):
    return abs(list(f(c, n))[-1]) <= 2


def main(width=1000, height=1000, real=(-2.0, 2.0), imag=(-2.0, 2.0)):
    data = np.zeros((height, width))

    delta_real = (real[1] - real[0]) / width
    delta_imag = (imag[1] - imag[0]) / height

    for i in range(100000):
        real, imag = np.random.rand(2)
        real = 4 * real - 2
        imag = 4 * imag - 2
        c = real + 1j * imag
        if not is_stable(c, n=100):
            draw(data, c, delta_real, delta_imag, size=width)

    plt.imshow(data, cmap="gray")
    plt.gca().set_aspect("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("mid.png")


if __name__ == "__main__":
    main(width=500, height=500)
