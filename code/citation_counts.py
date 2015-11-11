"""Creates a citation count for each patent in the input file.
Inputs should be a list of patent numbers for which counts are needed, and
a file of ipgb biblio files for which each patent is on a single line.
The latter is the output of one-patent-per-line.py on an ipgb*.xml file or set
of files.

Created as part of an Innovation Strategy project for DSBA-6100: Big Data
Analytics for Competitive Advantage, Fall 2015. UNC-Charlotte

Keith G. Williams
"""

# load libraries
import re as re
import pandas as pd

# define function for extracting patent citation numbers
def extract_citations(patent):
    """Input: string, patent on a single line
    Output: list, patent ID numbers cited by patent
    """
    # define regular expressions
    re_ref = '<.*?references-cited.*?</.*?references-cited>'
    re_trash = '<doc-number>|</doc-number>|-|/| '

    ref_cited = re.search(re_ref, patent)
    if ref_cited:
        citation_ids = re.findall('<doc-number>.*?</doc-number>', ref_cited.group())
                
        return [re.sub(re_trash, '', citation)[-8:-1] for citation in citation_ids]
    else:
        return []

def patents_cited(relevant_patents, ipgb):
    """Function for creating dictionary of patents and their citations.
        Inputs:
            relevant_patents - set of patent ids for which back citations are 
                relevant.
            ipgb - file from ipgb. patents are on a single line.
        Output: Dictionary, key=patent id, val=set of cited patents
    """
    # define regular expressions
    re_id = '<publication-reference>.*?<doc-number>.*?</doc-number>'
    re_xml_tags = '.*<doc-number>|</doc-number>.*'
        
    # create dictionary
    citations = {}

    # extract citations for each patent
    with open(ipgb) as patent_file:
        for patent in patent_file:
        
            # extract patent number
            pub_ref = re.search(re_id, patent)
            if pub_ref:
                pat_id = re.sub(re_xml_tags, '', pub_ref.group())
        
            # extract set of patent citations
            references_cited = set(extract_citations(patent))
        
            # check that patent has citations of interest
            if references_cited.intersection(relevant_patents):
                # update patent-citation dictionary
                citations[pat_id] = references_cited
            
    return citations
    
def back_citation_count(patent_id, citation_dict):
    """Count times each patent_id is referenced in citation_list
    Inputs:
        patent_id - patent id number
        citation_dict - dictionary of patents and the patent ids referenced.
   Output:
        integer - number of times patent is referenced
    """
    count = 0
    for patent in citation_dict.keys():
        if patent_id in citation_dict[patent]:
            count += 1
    return count

def run():
    # load medtronic and competitor patent list
    with open('patent_numbers_medtronic_and_competitors.txt') as f:
        pat_numbers = set(f.read().splitlines()) #strip \n

    # load one-patent-per-line.txt file
    ipgb_file = 'oppl11-15.txt'
    
    # create dictionary of patents that cite relevant patents
    citations = patents_cited(pat_numbers, ipgb_file)
    
    # create dictionary of relevant patents and back citation counts
    back_citations = {}
    for patent in pat_numbers:
        back_citations[patent] = back_citation_count(patent, citations)
    
    # convert back citation dictionary to tidy pandas data frame for export    
    cit_df = pd.DataFrame.from_dict(back_citations, orient='index')
    cit_df.index.name = 'patent_number'
    cit_df.columns = ['citation_count']
    cit_df.to_csv('back_citations11-15v2.csv')

if __name__ == "__main__":
    run()
        