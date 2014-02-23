#!/bin/bash -l
# NOTE the -l flag!
#

# This is an example job file for a single core CPU bound program
# Note that all of the following statements below that begin
# with #SBATCH are actually commands to the SLURM scheduler.
# Please copy this file to your home directory and modify it
# to suit your needs.
# 
# If you need any help, please email rc-help@rit.edu
#

# Where to send mail...
#To send emails, set the adcdress below and remove one of the "#" signs.
##SBATCH --mail-user USER@rit.edu

# notify on state change: BEGIN, END, FAIL or ALL
#SBATCH --mail-type=ALL

# Request 5 minutes run time MAX, anything over will be KILLED
#SBATCH -t 0:5:0

# Put the job in the "debug" partition and request one core
# You probably want to change "debug" to "work" once you have a sense of how
# this is working.
#SBATCH -p debug -n 1

# Job memory requirements in MB
#SBATCH --mem=300

echo "I am a job..."
echo "My value of alpha is $alpha"
echo "My value of beta is $beta"
echo "And now I'm going to simulate doing work based on those parameters..."

sleep 20

echo "All done with my work.  Exiting."
