import numpy as np

# סעיף 1: תמונה שחורה בגווני אפור (גובה 100, רוחב 200)
black = np.zeros((100, 200), dtype=np.uint8)

# סעיף 2: תמונה לבנה באותו גודל
white = np.full((100, 200), 255, dtype=np.uint8)

# סעיף 3: תמונה צבעונית בצבע אחד 
color = np.zeros((100, 200, 3), dtype=np.uint8)
color[:, :] = [255, 0, 0]
# ה-shape של תמונה צבעונית בגודל 100×200 הו3א)`:
#הSHAPE הוא 3 (r,g,b)

# סעיף 4: הדפסת מאפיינים
for name, img in [("black", black), ("white", white), ("color", color)]:
    print(f"{name}: shape={img.shape}, ndim={img.ndim}, size={img.size}, nbytes={img.nbytes}")

# סעיף 5: גודל בזיכרון
# סעיף 5: כל פיקסל = 3 בתים (R, G, B), בייט אחד לכל ערוץ

# 1920 x 1080
# 1920 * 1080 * 3 = 6,220,800 בייטים
print(np.zeros((1080, 1920, 3), dtype=np.uint8).nbytes)

# 12 מגה-פיקסל = 12,000,000 פיקסלים
# 12,000,000 * 3 = 36,000,000 בייטים
print(np.zeros((3000, 4000, 3), dtype=np.uint8).nbytes)


# סעיף 6
b = np.arange(12).reshape(3, 4)
print(b)
print(b.sum())
print(b.sum(axis=0))
print(b.sum(axis=1))
print(b[2, 3], b[-1, -1])

# הסבר על axis (במילים שלי):
# axis=0 - הפונקציה עוברת מלמעלה למטה (בין השורות), ונותנת ערך אחד לכל עמודה.
#          לדוגמה b.sum(axis=0) מחבר כל עמודה: [12 15 18 21]
# axis=1 - הפונקציה עוברת משמאל לימין (בתוך כל שורה), ונותנת ערך אחד לכל שורה.
#          לדוגמה b.sum(axis=1) מחבר כל שורה: [6 22 38]
