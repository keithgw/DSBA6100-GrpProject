library(stringr)
library(dplyr)

# load patent csv
patents_raw <- read.csv(patent_file, stringsAsFactors=FALSE, na.strings="None")

# remove duplicate entries
patents <- unique(patents_raw)

# remove leading zero from patent numbers
patents$patent_number <- str_replace(patents$patent_number, '0', '')

# add main classification labels

# add citation counts

# write out
