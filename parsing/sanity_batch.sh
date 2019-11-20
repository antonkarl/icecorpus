#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "ERROR: missing parameter. Please indicate the directory with the .psd files for conversion."
fi
# Does sanity check on all .psd files in a given directory
for file in $1/*.psd; do ./sanity.sh ${file%.psd}; done