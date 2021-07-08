import dislib as ds
from dislib.data.array import random_array
from dislib.math import qr
import numpy as np
import pytraj as pt
from pycompss.api.api import compss_barrier, compss_wait_on
import time


np.set_printoptions(precision=2)
np.random.seed(8)

matrix_size = (10000, 5000)
block_size = (1000, 1000)


def main():
    ini_time = time.time()
    
    m2b_ds = random_array(matrix_size, block_size)
    compss_barrier()

    load_time = time.time()
    print ("Load time", load_time - ini_time)

    print("Decomposing...")
    s_time = time.time()
     
    q, r = qr(m2b_ds, mode="full")

    compss_barrier()

    print("Decomposition time: ", time.time() - s_time)

    print("q.shape", q.shape)
    print("r.shape", r.shape)


if __name__ == "__main__":
    main()

