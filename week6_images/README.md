# Week 6 : Images As Arrays

**Focus:** pixels, channels, shape, resize, grayscale, crop.

## Load, inspect, resize, grayscale, crop
`image_basics.py` demonstrates that an image is just a NumPy array of shape
`(height, width, channels)`. It:
1. Loads an image (or **auto-generates a synthetic one** so the lab runs with no external file).
2. Inspects and prints the shape, dtype, and pixel value range.
3. Resizes to 640×640.
4. Converts BGR → grayscale (3 channels → 1; colour information is lost).
5. Crops the centre region of interest with NumPy slicing.

```bash
python image_basics.py                 # synthetic sample image
python image_basics.py path/to/img.jpg # your own image
```

Before/after images are written to `week6_images/output/` (git-ignored) so you can compare them
side by side.

## Before/after images + short explanation
Run the script, then compare:
- **`01_original.png` vs `03_grayscale.png`** : grayscale collapses 3 colour channels into 1
  intensity channel. We lose the ability to distinguish objects by colour (e.g. a red vs green
  jacket), but keep shape/edges : and the array is 3× smaller, so it is cheaper to process.
- **`01_original.png` vs `02_resized.png`** : forcing a non-square image into 640×640 stretches it,
  distorting aspect ratio. Real pipelines usually *letterbox* (pad) instead to preserve proportions.

## Key lesson
Before object detection, understand that every model input is just numbers in a useful shape.
Resizing changes spatial resolution; cropping selects a region; normalization rescales values into
a model-friendly range. None of it is magic : it is array manipulation.
