# bash script for concatentating batch opplYY.txt files,
# and filtering for each company

cat *.txt > oppl_combined.txt

grep -i -E "assignee>.*?medtronic.*?</assignee|assignee>.*?covidien.*?</assignee" oppl_combined.txt > oppl_medtronic.txt
grep -i -E "assignee>.*?stryker.*?</assignee" oppl_combined.txt > oppl_stryker.txt
grep -i -E "assignee>.*?boston scientific.*?</assignee" oppl_combined.txt > oppl_boston_scientific.txt
grep -i -E "assignee>.*?abbott.*?</assignee" oppl_combined.txt > oppl_abbott.txt