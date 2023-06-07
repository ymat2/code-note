#$ -S /bin/bash
#$ -t 1-3:1
#$ -cwd
#$ -o .
#$ -e .
#$ -l medium
#$ -l s_vmem=64G
#$ -l mem_req=64G
#$ -pe def_slot 4
#$ -tc 3

seq_ids=(hoge fuga piyo)
seq_id=${seq_ids[$SGE_TASK_ID-1]}

echo SGE_TASK_ID: $SGE_TASK_ID
echo ${seq_id}
