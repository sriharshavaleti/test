#/bin/bash
data = cat <filename>|head -5
echo data
no_of_clm = awk -F',' '{print NF; exit}' <filename> or cat <filename>|awk -F ',' {print NF; exit}'
sed 's/,/\t/g' <filename> > <new_filename>
echo "delimiter changed in new file"
