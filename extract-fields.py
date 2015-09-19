# Takes as an input a .txt file in which each patent is on its own line:
# an output of one-patent-per-line.py | grep -i "COMPANY" > out.txt
#
# Extracts fields for output as a tidy .csv

import sys as sys
import re as re
import pandas as pd

COMPANY = 'Medtronic' # modify for each company
TESTFILE = open('C:\Users\keithg.williams\Documents\DSBA-6100\DSBA-6100-Group-Project\widetestpatent.txt')
    
def extract_fields(company, patent_file):
    
    # initialize fields as a dictionary
    fields = {'company_name' : [],
              'patent_assignee' : [],
              'year_granted' : [],
              'year_applied' : [],
              'patent_class' : [],
              'patent_number' : [],
              'patent_title' : [],
              'patent_abstract' : []}
    
    # specify regular expressions
    assignee_re = '<assignee>.*?</orgname>'
    pub_ref_re = '<publication-reference>.*?</publication-reference>'
    date_tags = '<publication-reference>.*<date>|</date>.*'
    id_tags = '<publication-reference>.*<doc-number>|</doc-number>.*'
    app_ref_re = '<application-reference.*?</application-reference>'
    class_re = '</classification-locarno>.*?</main-classification>'
    title_re = '<invention-title.*?</invention-title>'
    abstract_re = '<abstract.*?</abstract>'
  
    for line in patent_file.readlines():
        # Use regex to find fields, 
        # and append them to appropriate dictionary value
        
        # attach company name
        fields['company_name'].append(COMPANY)
        
        # extract patent assignee
        assignee = re.search(assignee_re, line)
        if assignee:
            patent_assignee = re.sub('<assignee>.*<orgname>|</orgname>', 
                                  '', 
                                  assignee.group())
            fields['patent_assignee'].append(patent_assignee)
        else:
            fields['patent_assignee'].append('None')
            
        # extract year granted and patent number, 
        # both in <publication-reference>
        pub_ref = re.search(pub_ref_re, line)
        if pub_ref:
            year_granted = re.sub(date_tags, '', pub_ref.group())
            patent_number = re.sub(id_tags, '', pub_ref.group())
            fields['year_granted'].append(year_granted[0:4])
            fields['patent_number'].append(patent_number)
        else:
            fields['year_granted'].append('None')
            fields['patent_number'].append('None')
            
        # extract year applied
        app_ref = re.search(app_ref_re, line)
        if app_ref:
            year_applied = re.sub('<application.*<date>|</date>.*',
                                  '',
                                  app_ref.group())
            fields['year_applied'].append(year_applied[0:4])
        else:
            fields['year_applied'].append('None')
        
        # extract patent classification
        classification = re.search(class_re, line)
        if classification:
            patent_class = re.sub('</class.*<main-classification>|</main.*',
                                  '',
                                  classification.group())
            fields['patent_class'].append(patent_class)
        else:
            fields['patent_class'].append('None')
                
        # extract patent title
        title = re.search(title_re, line)
        if title:
            patent_title = re.sub('<invention.*?>|</invention.*',
                                  '',
                                  title.group())
            fields['patent_title'].append(patent_title)
        else:
            fields['patent_title'].append('None')
        
        # extract patent abstract
        abstract_field = re.search(abstract_re, line)
        if abstract_field:
            abstract = re.sub('<abstract.*<p.*?>|</abstract>',
                              '',
                              abstract_field.group())
            fields['patent_abstract'].append(abstract)
        else:
            fields['patent_abstract'].append('None')
            
    # transform dictionary to pandas DataFrame
    df = pd.DataFrame(fields)
    # write DataFrame as a .csv
    df.to_csv('testcsv.csv')
    
    #sys.stdout.write(', '.join(fields['patent_abstract']))
    

if __name__ == "__main__":
    extract_fields(COMPANY, TESTFILE)