
# example of global pixel standardization
from numpy import asarray
from PIL import Image
# load image
image = Image.open('data/Acinetobacter.baumanii/img0.png')
pixels = asarray(image)
# convert from integers to floats
pixels = pixels.astype('float32')
# calculate global mean and standard deviation
mean, std = pixels.mean(), pixels.std()
print('For Acinobactor Mean: %.3f, Standard Deviation: %.3f' % (mean, std))
# global standardization of pixels
#pixels = (pixels - mean) / std
# confirm it had the desired effect
#mean, std = pixels.mean(), pixels.std()
#print('Mean: %.3f, Standard Deviation: %.3f' % (mean, std))

image = Image.open('data/Bacteroides.fragilis/img0.png')
pixels = asarray(image)
# convert from integers to floats
pixels = pixels.astype('float32')
# calculate global mean and standard deviation
mean, std = pixels.mean(), pixels.std()
print('For Bacteroides Mean: %.3f, Standard Deviation: %.3f' % (mean, std))