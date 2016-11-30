#!/bin/sh


# Dirty as fuck
# This is horrible but it works

for file in 201*txt; do
    file_name=$(echo $file | rev | cut -c 5- | rev)  # Trim .txt ending
    # Clean twice cuz files are dirtyyyy
    ./clean_data.py $file > tmp1.txt
    ./clean_data.py tmp1.txt > tmp2.txt
    mv tmp2.txt ${file_name}_clean.txt
    rm tmp1.txt
done
