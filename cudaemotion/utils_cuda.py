import numpy as np
import cupy as cp

def to_gpu(data):
    """Transfer data to GPU."""
    return cp.asarray(data)

def from_gpu(data):
    """Transfer data back to CPU."""
    return cp.asnumpy(data)

def allocate_memory(shape):
    """Allocate memory on the GPU."""
    return cp.zeros(shape, dtype=np.float32)
