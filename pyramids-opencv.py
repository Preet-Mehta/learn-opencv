import cv2

img = cv2.imread('images/lena.jpg')
lr = img.copy()
gp = [lr]

# Gaussian Pyramids
for i in range(3):
    lr = cv2.pyrDown(gp[-1])
    gp.append(lr)
    # cv2.imshow(f"Down {i}", gp[-1])

# Laplacian Pyramids - Difference between Gauss Lvl and Extended Gauss Lvl of upper layer.
lp = [gp[-1]]
for i in range(len(gp)-1, 0, -1):
    extended = cv2.pyrUp(gp[i])
    lp.append(cv2.subtract(gp[i-1], extended))
    cv2.imshow(f"Laplacian {i}", lp[-1])

cv2.waitKey(0)
cv2.destroyAllWindows()
