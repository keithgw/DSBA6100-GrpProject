# DSBA-6100-Group-Project

## Files

### Raw  
- ipgb20140325.xml is one of the many .xml patent biblio files to which we have access  
- testpatent.xml is the first two patents from ipgb20140325.xml for testing processing functions 
- patent_classification_lookup_table is a codebook from the USPTO website, that gives labels for 3-digit main classifications  

### Scripts  
- one-patent-per-line.py is a python script. It takes as an input a patent.xml file and outputs a stdout file object (unix) where each patent in the file is on a single line.  
- extract-fields.py is a python script. It takes as an input a .txt file (the output of one-patent-per-line.py) and outputs a tidy .csv with features of pertinent patents.  
- original-format.py is a python script that reverts the one-patent-per-line.py output to the original structure. Can be used after filtering some of the patents.  
- unzip-notes.bsh contains a bash (Unix) script to programatically unzip patent biblio files, and iteratively process them for input into extract-fields.py.  
- batch_to_filtered.sh contains a shell (Unix) script to concatenate the batch runs of unzip-notes.bsh and filter for each company to input into extract-fields.py  
- EDA.Rmd contains all of the exploratory analysis on medtronic_and_competitor_patents_05-15.csv.  

### Outputs
- testcsv.csv is a proof of concept of extract-fields.py done on testpatent.xml  
- patent_title wordcloud.png is a wordcloud built in R on testcsv.csv  
- widetestpatent.txt is a proof of concept of one-patent-per-line.py run on tesetpatent.xml  
- oppl.txt is a proof of concept of unzip-notes.bsh done on all of the wk1 patent files from 2005-2015.  
- wk1test.csv is a proof of concept of extract-fields.py run on oppl.txt  
- medtronic_and_competitor_patents_05-15.csv is the cleaned CSV after the output of extract-fields.py  
- raw-to-csv.Rmd is a description of the data cleaning process.  
- ipgb_batch_log.txt is a log of the iterative unzip - transform - extract batches distributed on 5 machines.  
- patent-extraction-instructions.Rmd is a document explaining how to set-up a raw-to-csv batch job.  

### Figures  
All figures are in the /Figures sub-directory. These figures were used in the technical reports, executive summaries, and presentation slide decks.  