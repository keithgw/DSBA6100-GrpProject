# DSBA-6100-Group-Project

## Files

### Raw  
- ipgb20140325.xml is one of the many .xml patent biblio files to which we have access  
- testpatent.xml is the first two patents from ipgb20140325.xml for testing processing functions 

### Scripts  
- one-patent-per-line.py is a python script. It takes as an input a patent.xml file and outputs a stdout file object (unix) where each patent in the file is on a single line.  
- extract-fields.py is a python script. It takes as an input a .txt file (the output of one-patent-per-line.py) and outputs a tidy .csv with features of pertinent patents.  
- original-format.py is a python script that reverts the one-patent-per-line.py output to the original structure. Can be used after filtering some of the patents.  
- unzip-notes.bsh contains a bash (Unix) script to programatically unzip patent biblio files, and iteratively process them for input into extract-fields.py.  
- batch_to_filtered.sh contains a shell (Unix) script to concatenate the batch runs of unzip-notes.bsh and filter for each company to input into extract-fields.py

### Outputs
- testcsv.csv is a proof of concept of extract-fields.py done on testpatent.xml  
- patent_title wordcloud.png is a wordcloud built in R on testcsv.csv  
- widetestpatent.txt is a proof of concept of one-patent-per-line.py run on tesetpatent.xml  
- oppl.txt is a proof of concept of unzip-notes.bsh done on all of the wk1 patent files from 2005-2015.  
- wk1test.csv is a proof of concept of extract-fields.py run on oppl.txt  