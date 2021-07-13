# find all with file name and display mach once per file
grep -io --color '[A-Z]*_tape' *.json | sort -u

#find only the combinations 
grep -io --color '[A-Z]*_tape' *.json | awk -F':' '{print $2}'  | sort -u
