import sys, tensorflow as tf, numpy as np
print("python:", sys.version)
print("tf:", tf.__version__)
print("np:", np.__version__)
print("tf built w/ cuda:", tf.test.is_built_with_cuda())
print("gpus:", tf.config.list_physical_devices("GPU"))
