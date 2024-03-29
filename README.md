# Fault Localization Evaluation Framework

This is the detailed setup guide for our evaluation framework. All the code are placed under the programs folder


Overview
========
Our experiments evaluate several 


- Use the GZoltar toolset to collect the coverage informa- tion for one bug of the defec4j project.

- Collect the buggy line number of the defect4j project buggy line data corpus.

- Use the script based on the open source project[6] to compute the accuracy score of each technique, and save it in the CSV file.

- Use the python program parse csvp ̇y to parse data and generate the plot for the score of each program.



Environment Setup
======

Requirements
----------------
 - Java 1.7
 - Git >= 1.9
 - SVN >= 1.8
 - Perl >= 5.0.10


Before doing anything else, run `./setup.sh`. This:

- Clone the defect4j project.
- updates the `.bashrc` file to export some environment variables:
    + `D4J_HOME` and `DEFECTS4J_HOME`, pointing to the new `defects4j` repository, if it needed
    + `GZOLTAR_JAR`, pointing to `./gzoltar/gzoltar.jar`

### How to

- Use the GZoltar toolset to collect the coverage information for one bug of the defec4j project.

	* To run GZoltar, use `gzoltar/run_gzoltar.sh`.
	
	    > Example: `bash run_gzoltar.sh Lang 37 . developer`
	    >
	    > Creates the files `./matrix` and `./spectra` for the coverage 			information

- Collect the buggy line number of the defect4j project buggy line.
	* Use the `d4j_integration/get_buggy_lines.sh` script to collect the buggy line information from the defects4j project/

- Use the script based on the open source project[6] to compute the accuracy score of each technique, and save it in the CSV file.

	* Use the integrated script to get the computed result of each bug

	`./job.sh
    --project <project_name>
    --bug <bug_id>
    --output_dir <output_dir_path>` 
        
- Use the python program `parse_csv.py` to parse csv file that generated by the last step and generate the plot for the score of each program.




