def flipAndInvertImage(image):
    image = [i[::-1] for i in image]
    return [[0 if i == 1 else 1 for i in j] for j in image]

print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))