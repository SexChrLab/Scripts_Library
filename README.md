# Scripts_Library
Contains a library of scripts used frequently

## RNAseq_analysis
1. `merge_counts_data.py`
What: after running featureCounts or salmon for each individual, we would like to merge the count from each individual into a file for downstream processing, such as running differential gene expression. 
Usage:
- This script takes in:
    + `--type`: indicates whether it's `featureCounts` or `salmon`
    + `--sample_list`: this is a space delimited file where the first column is the sample name and the second column is the full path to the count file for that sample
    + `--outfile`: this is the path to the output file. The number of column in this output file is equal to the number of individuals (number of rows) in the sample_list file. 
