import utils
from skimage.data import cat
from skimage.data import astronaut


def test_rotated_image_astronaut():
    image = astronaut()                                     #image with equal width and height
    result = utils.rotated_image(image)
    assert result.shape == image.shape


def test_rotated_image_cat():
    image = cat()                                           #image with non-equal width and height
    result = utils.rotated_image(image)
    assert result.shape == image.shape
