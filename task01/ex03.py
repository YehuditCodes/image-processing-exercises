import numpy as np

x = np.array([100, 200, 250], dtype=np.uint8)

print("=" * 45)
print("תרגיל 3: גלישה של ערכים".center(45))
print("=" * 45)
print("x =", x, "| dtype =", x.dtype)
print("-" * 45)

print("1. x + 10                    =", x + 10)
print("2. x + 100                   =", x + 100)
print("3. x - 150                   =", x - 150)
print("4. x * 2                     =", x * 2)
print("5. x.astype(np.int16) + 100  =", x.astype(np.int16) + 100)
print("6. x * 1.5                   =", x * 1.5)
print("7. (x * 1.5).dtype           =", (x * 1.5).dtype)

print("=" * 45)

# סעיף 2
# print("2. x + 300 =", x + 300)
print("NumPy version:", np.__version__)

# סעיף 3
def add_safe(x, b):
    return np.clip(x.astype(np.int32) + b, 0, 255).astype(np.uint8)

print("3a. add_safe(x, 100)  =", add_safe(x, 100))
print("3b. add_safe(x, -150) =", add_safe(x, -150))

# סעיף 4
print("4. np.clip(x + 100, 0, 255) =", np.clip(x + 100, 0, 255))

# סעיף 5 (בונוס)
y = np.array([127], dtype=np.int8)
print("5. int8 range:", np.iinfo(np.int8).min, "to", np.iinfo(np.int8).max)
print("5. 127 + 1 =", y + 1)