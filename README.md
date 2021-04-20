# Microbial inflammatory networks in bronchiectasis exacerbators with Pseudomonas aeruginosa.
---
This document illustrates the use of the codes to implement the methods described in the article "Microbial inflammatory networks in bronchiectasis exacerbators with Pseudomonas aeruginosa.".
## Table of contents
1. [Pre requisites](#pre-requisities)
2. [Co-occurence analysis](#co-occurence-analysis)

---
## Pre requisites
You will need the following softwares and packages to run the codes.
For Linux systems, Install the following 
- Python3 
  - pandas library
- R
  - mboost package
  - boot package
  - foreach package
  - doParallel package
- Cytoscape (for network visualization)

Below is the directory structure of this repository
``` bash
.
├── Data
│   ├── cyto.csv
│   ├── Genus_rel.csv
│   └── necessary_variables.csv
├── LICENSE
├── README.md
├── With_Cytokines
│   ├── collate.py
│   ├── GBLM_parallel1.R
│   ├── N
│   └── Y
└── Without_Cytokines
    ├── collate.py
    ├── GBLM_parallel1.R
    ├── N
    └── Y
```

---
## Co-occurence analysis 
This code is adopted from https://github.com/translational-respiratory-lab/The_Interactome 
### Microbial association network without cytokines
Run the below code from your terminal from the root directory of this repository
```bash
cd Without_Cytokines/
python3 collate.py
Rscript GBLM_parallel1.R
```
This code will produce the adjacency matrix of the association networks named as `adj_to_cyto.csv` in `N/` for non-frequent exacerbator class and `Y/` for frequent exacerbator class. Import these adjacency matrix in Cytoscape to visualize the association networks.

### Microbial association network with cytokines
Run the below code from your terminal from the root directory of this repository
```bash
cd With_Cytokines/
python3 collate.py
Rscript GBLM_parallel1.R
```
This code will produce the adjacency matrix of the association networksnamed as `adj_to_cyto.csv` in `N/` for non-frequent exacerbator class and `Y/` for frequent exacerbator class. Import these adjacency matrix in Cytoscape to visualize the association networks.
