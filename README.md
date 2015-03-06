# Biomarker-Extraction

Given an XML file with elibility information for a cancer study (using data from https://clinicaltrials.gov/ct2/results?term=NCT01625234&show_down=Y), returns the eligibility criteria that contain information about biomarkers.

I.E. from the above study, we return the criteria: 
"
Histologically or cytologically confirmed diagnosis of advanced solid tumor
             malignancy. Patients may have received prior crizotinib and/or second generation ALK
             TKIs.

          
Patients with treated asymptomatic CNS metastases are eligible. ALK positive patients
             with untreated asymptomatic CNS lesions may be allowed to enroll.

          
For the expanded cohort portion of the study, NSCLC patients with ALK        genomic
             alterations.

"
