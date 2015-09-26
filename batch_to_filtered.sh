# bash script for concatentating batch opplYY.txt files,
# and filtering for each company

cat *.txt > oppl_combined.txt

grep -i -E "medtronic|covidien" oppl_combined.txt > oppl_medtronic.txt
grep -i "stryker" oppl_combined.txt > oppl_stryker.txt
grep -i "boston scientific" oppl_combined.txt > oppl_boston_scientific.txt
grep -i "abbott" oppl_combined.txt > oppl_abbott.txt