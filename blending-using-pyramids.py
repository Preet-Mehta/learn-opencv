import cv2
import numpy as np

apple = cv2.imread('images/apple.jpg')
orange = cv2.imread('images/orange.jpg')
app_or = np.hstack((apple[:, :256], orange[:, 256:]))

# Gaussian Apple
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6):
    gp_apple.append(cv2.pyrDown(gp_apple[i]))
    # cv2.imshow(str(i), gp_apple[-1])

# Gaussian Orange
orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(6):
    gp_orange.append(cv2.pyrDown(gp_orange[i]))
    # cv2.imshow(str(i), gp_orange[-1])

# Laplacian Apple
lp_apple = [gp_apple[-2]]
for i in range(5, 0, -1):
    lp_apple.append(cv2.subtract(gp_apple[i-1], cv2.pyrUp(gp_apple[i])))
    # cv2.imshow(str(i), lp_apple[-1])

# Laplacian Orange
lp_orange = [gp_orange[-2]]
for i in range(5, 0, -1):
    lp_orange.append(cv2.subtract(gp_orange[i-1], cv2.pyrUp(gp_orange[i])))
    # cv2.imshow(str(i), lp_orange[-1])

# Stack left-right of each level
apple_orange_stack = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    apple_orange_stack.append(np.hstack((apple_lap[:, :int(apple_lap.shape[0]/2)],
                                         orange_lap[:, int(apple_lap.shape[0]/2):])))
    # cv2.imshow(str(n), apple_orange_stack[n-1])

# Reconstruct
apple_orange_recon = apple_orange_stack[0]
for i in range(1, 6):
    apple_orange_recon = cv2.pyrUp(apple_orange_recon)
    apple_orange_recon = cv2.add(apple_orange_stack[i], apple_orange_recon)

cv2.imshow('Apple', apple)
cv2.imshow('Orange', orange)
cv2.imshow('Stacked', app_or)
cv2.imshow("final", apple_orange_recon)

cv2.waitKey(0)
cv2.destroyAllWindows()
