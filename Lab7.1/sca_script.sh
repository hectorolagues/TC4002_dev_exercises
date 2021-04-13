# sca_script.sh
# Shell script to clone the repo, run SCA (Static Code Analysis) with prospector and provide a JSON report

# -x enables verbose execution of scripts to see what is happening
# -e makes the shell exit immediately whenever something returns an error
set -xe

# Clone the repository
git clone https://github.com/hectorolagues/TC4002_dev_exercises.git

# Change directory
cd TC4002_dev_exercises

# Run the static analysis
prospector --zero-exit

#Provide a report
prospector --zero-exit --output-format json:./Lab7.1/report.json
