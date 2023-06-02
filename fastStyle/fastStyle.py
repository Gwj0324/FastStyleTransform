import functools
import PIL.Image
from matplotlib import gridspec
import matplotlib.pylab as plt
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

def crop_center(image):
  """Returns a cropped square image."""
  shape = image.shape
  new_shape = min(shape[1], shape[2])
  offset_y = max(shape[1] - shape[2], 0) // 2
  offset_x = max(shape[2] - shape[1], 0) // 2
  image = tf.image.crop_to_bounding_box(
      image, offset_y, offset_x, new_shape, new_shape)
  return image

@functools.lru_cache(maxsize=None)
def load_image(image_path, image_size=(256, 256), preserve_aspect_ratio=True):
  """Loads and preprocesses images."""
  # Cache image file locally.
  # image_path = tf.keras.utils.get_file(os.path.basename(image_url)[-128:], image_url)
  # Load and convert to float32 numpy array, add batch dimension, and normalize to range [0, 1].
  img = tf.io.decode_image(
      tf.io.read_file(image_path),
      channels=3, dtype=tf.float32)[tf.newaxis, ...]
  img = crop_center(img)
  img = tf.image.resize(img, image_size, preserve_aspect_ratio=True)
  return img

def tensor_to_image(tensor):
  tensor = tensor*255
  tensor = np.array(tensor, dtype=np.uint8)
  if np.ndim(tensor)>3:
    assert tensor.shape[0] == 1
    tensor = tensor[0]
  return PIL.Image.fromarray(tensor)

def image_generation(content_image_path,style_image_path,output_image_path):
  # @title Load example images  { display-mode: "form" }
  content_image_url = content_image_path  # @param {type:"string"}
  style_image_url = style_image_path  # @param {type:"string"}
  output_path = output_image_path
  output_image_size = 384  # @param {type:"integer"}
  # The content image size can be arbitrary.
  content_img_size = (output_image_size, output_image_size)
  # The style prediction model was trained with image size 256 and it's the 
  # recommended image size for the style image (though, other sizes work as 
  # well but will lead to different results).
  style_img_size = (256, 256)  # Recommended to keep it at 256.
  content_image = load_image(content_image_url, content_img_size)
  style_image = load_image(style_image_url, style_img_size)
  style_image = tf.nn.avg_pool(style_image, ksize=[3,3], strides=[1,1], padding='SAME')
  # show_n([content_image, style_image], ['Content image', 'Style image'])
  # Load TF Hub module.
  hub_handle = './magenta_arbitrary-image-stylization-v1-256_2/'
  hub_module = hub.load(hub_handle)
  # Stylize content image with given style image.
  # This is pretty fast within a few milliseconds on a GPU.
  outputs = hub_module(tf.constant(content_image), tf.constant(style_image))
  stylized_image = outputs[0]
  tensor_to_image(stylized_image).save(output_path)