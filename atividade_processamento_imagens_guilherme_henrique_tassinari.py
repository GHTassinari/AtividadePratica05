# pip install opencv-python matplotlib numpy
import os
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img_path = "photo.jpg"

# Converte a imagem para o modo RGB
img_rgb = cv.cvtColor(cv.imread(img_path), cv.COLOR_BGR2RGB)

img_original = img_rgb.copy()

# Aqui, é definido a height e a width com base na shape da imagem original
height, width, _ = img_original.shape

# Rotaciona a imagem em 45 graus
rotation_matrix_45 = cv.getRotationMatrix2D((width // 2, height // 2), 45, 1)

img_1 = cv.warpAffine(img_original, rotation_matrix_45, (width, height))

# Rotaciona a imagem em 90 graus
rotation_matrix_90 = cv.getRotationMatrix2D((width // 2, height // 2), 90, 1)

img_2 = cv.warpAffine(img_original, rotation_matrix_90, (width, height))

plt.imshow(img_1)
plt.title("Rotacionado em 45 graus")
plt.show()

plt.imshow(img_2)
plt.title("Rotacionado em 90 graus")
plt.show()

# É uma matriz de translação, ele vai mover a 
# imagem 100 pixels para a direita e 50 pixels para baixo
translation_matrix = np.float32([[1, 0, 100], 
                                  [0, 1, 50]])

# A imagem vai ser translada 50 pixels para baixo e 100 pixels para a direita
img_3 = cv.warpAffine(img_original, translation_matrix, (width, height))

plt.imshow(img_3)
plt.title("Transladado")
plt.show()

# Redimensiona a imagem para metade do tamanho original
img_4 = cv.resize(img_original, (width//2, height//2), interpolation=cv.INTER_LINEAR)

# Redimensiona a imagem para 150% o tamanho da original
img_5 = cv.resize(img_original, (int(width*1.5), int(height*1.5)), interpolation=cv.INTER_CUBIC)


# Para mostrar a diferença, aqui usei o extent para mudar os eixos
# Assim, podemos ver o tamanho real da imagem em px, com base no eixo x e y
plt.imshow(img_4, extent=[0, img_4.shape[1], img_4.shape[0], 0])
plt.title("Redimensionado para metade do tamanho")
plt.show()

plt.imshow(img_5, extent=[0, img_5.shape[1], img_5.shape[0], 0])
plt.title("Redimensionado para 150% do tamanho")
plt.show()

# Centro da imagem
cx, cy = width // 2, height // 2

# Defino o tamanho do quadrado a ser removido
square_size = 400

# Coordenadas do quadrado
# Aqui, ele pegará os valores centrais, e reduzirá o valor do quadrado, e depois aumentará
# Assim, será a onde ele começa, até onde ele termina em y1:y2 e x1:x2
x1, x2 = cx - square_size, cx + square_size
y1, y2 = cy - square_size, cy + square_size

img_6 = img_original.copy()
img_6[y1:y2, x1:x2] = (0, 0, 0) 

plt.imshow(img_6)
plt.title("Parte do centro removida por um quadrado preto")
plt.show()

# Será realizado um flip horizontal, utilizando o 1
img_7 = cv.flip(img_original, 1)

# Já aqui, é realizado um flip vertical, utilizando o 0
img_8 = cv.flip(img_original, 0)

plt.imshow(img_7)
plt.title("Flip horizontal")
plt.show()

plt.imshow(img_8)
plt.title("Flip vertical")
plt.show()
