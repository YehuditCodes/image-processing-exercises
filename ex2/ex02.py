import numpy as np

# Part 1: black grayscale image (height 100, width 200)
black = np.zeros((100, 200), dtype=np.uint8)

# Part 2: white image of the same size
white = np.full((100, 200), 255, dtype=np.uint8)

# Part 3: color image filled with a single color (red, in RGB order)
color = np.zeros((100, 200, 3), dtype=np.uint8)
color[:, :] = [255, 0, 0]
# The shape of a 100x200 color image is (100, 200, 3):
# height, width, and 3 channels (R, G, B)

# Part 4: print the properties of the three images
for name, img in [("black", black), ("white", white), ("color", color)]:
    print(f"{name}: shape={img.shape}, ndim={img.ndim}, size={img.size}, nbytes={img.nbytes}")

# Part 5: memory size of color images
# Each pixel takes 3 bytes (R, G, B), one byte per channel.

# 1920 x 1080: 1920 * 1080 * 3 = 6,220,800 bytes
print("1920x1080 nbytes:", np.zeros((1080, 1920, 3), dtype=np.uint8).nbytes)

# 12 megapixels = 12,000,000 pixels (for example 4000 x 3000)
# 12,000,000 * 3 = 36,000,000 bytes
print("12MP nbytes:", np.zeros((3000, 4000, 3), dtype=np.uint8).nbytes)

# Part 6: sums along axes
b = np.arange(12).reshape(3, 4)
print(b)
print(b.sum())
print(b.sum(axis=0))
print(b.sum(axis=1))
print(b[2, 3], b[-1, -1])

# Explanation of axis (in my own words):
# axis=0 - the function runs from top to bottom (across the rows)
#          and gives one value per column.
#          For example, b.sum(axis=0) sums each column: [12 15 18 21]
# axis=1 - the function runs from left to right (within each row)
#          and gives one value per row.
#          For example, b.sum(axis=1) sums each row: [6 22 38]