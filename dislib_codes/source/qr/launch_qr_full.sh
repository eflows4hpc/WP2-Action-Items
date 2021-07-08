#!/bin/sh

export COMPSS_PYTHON_VERSION=none
module load python/3.7.4
module load COMPSs/2.9

export computingUnits=1

queue=debug
time_limit=20

# log level off for better performance

enqueue_compss --qos=$queue  --reservation=DISLIB21 --log_level=off --job_name=qr_f1 --worker_in_master_cpus=0 --max_tasks_per_node=48 --exec_time=$time_limit --num_nodes=2 --pythonpath=/home/nct00/nct00001/source/QR/dislib_qr qr_full.py
