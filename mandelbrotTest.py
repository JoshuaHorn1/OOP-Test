from PIL import Image, ImageDraw

def mandelbrot_seq(c, max_iter):
  """
  Calculates the number of iterations required to determine if a complex number 'c' belongs to the Mandelbrot set.

  Args:
      c: A complex number represented as a tuple (real, imaginary).
      max_iter: The maximum number of iterations allowed to classify 'c' within the Mandelbrot set.

  Returns:
      The number of iterations needed to classify 'c' within the Mandelbrot set,
      or 'max_iter' if the limit is not reached.
  """
  z = 0
  for n in range(max_iter):
    if abs(z) > 2.0:
      return n
    z = z * z + c
  return max_iter

WIDTH = 600
HEIGHT = 400
RE_START = -2.5
RE_END = 1.5
IM_START = -2
IM_END = 2
MAX_ITER = 256

def color_calc(iterations, max_iter):
  """
  This function defines a simple coloring scheme for the Mandelbrot set.
  You can customize this function to create different visual effects.

  Args:
      iterations: The number of iterations needed to classify a complex number within the Mandelbrot set.
      max_iter: The maximum number of iterations allowed for classification.

  Returns:
      A color tuple representing the calculated color for the given number of iterations.
  """
  # This is a simple linear grayscale scheme
  grayscale = int(255 * iterations / max_iter)
  return (grayscale, grayscale, grayscale)

image = Image.new('RGB', (WIDTH, HEIGHT), color='black')
draw = ImageDraw.Draw(image)

for x in range(WIDTH):
    for y in range(HEIGHT):
        c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                    IM_START + (y / HEIGHT) * (IM_END - IM_START))
        iterations = mandelbrot_seq(c, MAX_ITER)
        color = color_calc(iterations, MAX_ITER)
        draw.point((x, y), fill=color)

image.save('mandelbrot.png')
