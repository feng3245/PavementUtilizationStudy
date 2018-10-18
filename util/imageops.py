import random
from skimage.transform import resize

def sliceimage(image, x, y, length):
    return image[y:y+length, x:x+length, :]
    
def randomslices(dataimage, classifyimage, minres, maxres, numofslices):
	slices = []
	for _ in range(numofslices):
		res = random.randint(minres, maxres)
		y = random.randint(0, len(dataimage)-1-res)
		x = random.randint(0, len(dataimage[0])-1-res)
		slices.append((sliceimage(dataimage, x, y, res), sliceimage(classifyimage, x, y, res)))
	return slices

def uniforminput(imagepairs, res):
	uniformSlices = []
	for ip in imagepairs:
		uniformSlices.append((resize(ip[0], (res, res)), resize(ip[1], (res, res))))
	return uniformSlices
		