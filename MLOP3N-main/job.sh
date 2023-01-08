#!/bin/bash
#PBS -l nodes=1:ppn=2,walltime=24:00:00

# cd $PBS_O_WORKDIR
# echo $(ls) > file_list.txt
source /opt/intel/oneapi/setvars.sh



conda activate base
cd ~/MLOP3N
python run.py
