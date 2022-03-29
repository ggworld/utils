grep -i -o -m 1 -P '.{0,10}material_type' *.json | awk -F '::' '{print $2}' | sort | uniq

# find files that containes value
grep -c dbt *.py |  awk -F: '$NF+0 > 0'
