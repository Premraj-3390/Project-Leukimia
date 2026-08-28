import cv2
import numpy as np
import skfuzzy as fuzz

def segment_image_fcm(image_path, img_size=224, n_clusters=3):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (img_size, img_size))

    pixels = img.reshape((-1, 3)).astype(np.float32)

    cntr, u, *_ = fuzz.cluster.cmeans(
        pixels.T, n_clusters, 2, error=0.005, maxiter=1000, init=None
    )

    membership = np.argmax(u, axis=0)
    counts = np.bincount(membership)
    target_cluster = np.argmin(counts[np.nonzero(counts)]) if len(counts) > 1 else 0

    segmented = np.zeros_like(pixels, dtype=np.uint8)
    segmented[membership == target_cluster] = pixels[membership == target_cluster]

    return segmented.reshape(img.shape)
