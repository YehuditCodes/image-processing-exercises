import numpy as np

a = np.array([[10, 100, 200],
              [50, 150, 250]], dtype=np.uint8)

print("1. a.dtype =", a.dtype)
print("2. a.shape =", a.shape)
print("3. a.ndim =", a.ndim)
print("4. a.size =", a.size)
print("5. a.nbytes =", a.nbytes)
print("6. a[1, 2] =", a[1, 2])
print("7. a[0, 1] =", a[0, 1])
print("8. a + 10 =\n", a + 10)
print("9. a - 20 =\n", a - 20)
print("10. a * 2 =\n", a * 2)
print("11. a.max() =", a.max())
print("12. a.max(axis=0) =", a.max(axis=0))
print("13. a.max(axis=1) =", a.max(axis=1))