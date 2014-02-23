#!/bin/bash
# This is an example script that loops over two parameters
# (from 1 to 5 for each) and submits 25 jobs to the slurm
# cluster.
#
# Author:  Ralph Bean <rjbpop@rit.edu>

# Just a constant variable used throughout the script to name our jobs
#   in a meaningful way.
basejobname="test"

# Another constant variable used to name the slurm submission file that
#   this script is going to submit to slurm.
jobfile="slurm-payload.sh"

param_limit_alpha=5
param_limit_beta=5

# Make an output directory if it doesn't already exist.
mkdir -p output

# Loop and submit all the jobs
echo
echo " * Getting ready to submit a number of jobs:"
echo
for alpha in $(seq 1 $param_limit_alpha); do
	for beta in $(seq 1 $param_limit_beta); do
		# Give our job a meaningful name
		jobname=$basejobname-$alpha-$beta
		echo "Submitting job $jobname"

		# Setup where we want the output from each job to go
		outfile=output/output-alpha.$alpha-beta.$beta.txt
		
		# "exporting" variables in bash make them available to your slurm
		# workload.
		export alpha;
		export beta;
			
		# Actually submit the job.
		sbatch --qos=rc-normal -J $jobname -o $outfile $jobfile
	done;
done

echo
echo " * Done submitting all those jobs (whew!)"
echo " * Now you can run the following command to see your jobs in the queue:"
echo
echo " $ squeue"
echo
