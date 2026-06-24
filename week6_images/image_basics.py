"""Week 6 — Images As Arrays.

Lab: load an image, inspect its shape, resize it, convert to grayscale, and crop a region.

The Week 6 lesson: every model input is just numbers arranged in a useful shape. An image is a
grid of pixels stored as a NumPy array of shape (height, width, channels).

Usage:
    python image_basics.py                 # auto-generates a synthetic sample image
    python image_basics.py path/to/img.jpg # use your own image

Outputs are written to ./output/ so you can compare before/after side by side (Week 6 homework).
"""

from __future__ import annotations

import os
import sys
from typing import Tuple

import cv2
import numpy as np

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")


def make_sample_image(height: int = 360, width: int = 480) -> np.ndarray:
    """Create a synthetic BGR image so the lab runs without any external file.

    Draws a colour gradient background plus a filled rectangle (a stand-in "object").
    """
    img = np.zeros((height, width, 3), dtype=np.uint8)
    # Horizontal blue->red gradient across the width.
    for x in range(width):
        img[:, x, 0] = int(255 * (1 - x / width))  # Blue channel
        img[:, x, 2] = int(255 * (x / width))       # Red channel
    # A green-ish rectangle to act as a region of interest.
    cv2.rectangle(img, (160, 90), (320, 270), (40, 200, 40), thickness=-1)
    cv2.putText(img, "UNI_VISION", (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                (255, 255, 255), 2, cv2.LINE_AA)
    return img


def inspect(img: np.ndarray, name: str = "image") -> Tuple[int, int, int]:
    """Print and return (height, width, channels)."""
    h, w = img.shape[:2]
    c = img.shape[2] if img.ndim == 3 else 1
    print(f"{name:18s} shape=(h={h}, w={w}, c={c})  dtype={img.dtype}  "
          f"min={img.min()} max={img.max()}")
    return h, w, c


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 1. Load (or synthesise) the image.
    if len(sys.argv) > 1:
        path = sys.argv[1]
        img = cv2.imread(path)
        if img is None:
            print(f"Could not read '{path}'. Falling back to a synthetic image.")
            img = make_sample_image()
        else:
            print(f"Loaded {path}")
    else:
        print("No image given - generating a synthetic sample image.")
        img = make_sample_image()

    # 2. Inspect shape.
    h, w, _ = inspect(img, "original")
    cv2.imwrite(os.path.join(OUTPUT_DIR, "01_original.png"), img)

    # 3. Resize to 640x640 (note: this distorts aspect ratio — discussed in the homework).
    resized = cv2.resize(img, (640, 640))
    inspect(resized, "resized 640x640")
    cv2.imwrite(os.path.join(OUTPUT_DIR, "02_resized.png"), resized)

    # 4. Convert to grayscale (3 channels -> 1 channel; colour information is lost).
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inspect(gray, "grayscale")
    cv2.imwrite(os.path.join(OUTPUT_DIR, "03_grayscale.png"), gray)

    # 5. Crop a centre region of interest (pure NumPy slicing: rows then columns).
    y1, y2 = h // 4, 3 * h // 4
    x1, x2 = w // 4, 3 * w // 4
    crop = img[y1:y2, x1:x2]
    inspect(crop, "centre crop")
    cv2.imwrite(os.path.join(OUTPUT_DIR, "04_crop.png"), crop)

    print(f"\nSaved before/after images to: {OUTPUT_DIR}")
    print("Compare 01_original vs 03_grayscale (colour lost) and 02_resized (aspect distorted).")


if __name__ == "__main__":
    main()
