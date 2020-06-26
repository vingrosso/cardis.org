#! /usr/bin/env python

import os

#years_with_bib=[2013, 2014]
years_with_bib=[2014]

for i in years_with_bib:
    os.system("./bib_parse -r html/ -o html  proceedings/cardis_%s/ > html/proceedings/%s.html"%(i,i))
