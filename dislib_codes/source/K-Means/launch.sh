export COMPSS_PYTHON_VERSION=3-ML
module load dislib
module unload COMPSs
module load COMPSs/2.8
module load mkl/2019.2

enqueue_compss -t --qos=debug --reservation=DISLIB21 --log_level=off  --job_name=kmeans_compss --worker_in_master_cpus=0 --max_tasks_per_node=48 --exec_time=20 --num_nodes=2  kmeans_example.py 

