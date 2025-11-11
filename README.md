[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wojP3-_r)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21237964)
# project-final

Final project repo for INFO 523 - Fall 2025.

# Data
-   **[Dataset]**: United States Environmental Protection Agency’s (EPA) 2025 daily Air Quality Index (AQI) dataset: contains 57,012 rows with 8 variables showing insight into daily air quality and how it changes over days, months, and seasons.
-   Source URL: https://aqs.epa.gov/aqsweb/airdata/download_files.html

# Codebook for our Dataset

## Variable Names and Descriptions:

-   **variable**: Description (with units, where applicable)
-   State Name: US State
-   County Name: US County Name
-   State Code: Code for State
-   County Code: Code for County
-   Date: date of measurement
-   AQI: Air Quality Index value
-   Category: Qualitative value for AQI
-   Defining Paramter: AQS code corresponding to the parameter measured
-   Defining Site: Site corresponding to the site where measurement was reported from
-   Number of Sites Reporting: Total amount of sites with recording measurement

## Data Types:

-   State Name: String
-   County Name: String
-   State Code: Int
-   County Code: Int
-   Date: String
-   AQI: Int
-   Category: String
-   Defining Parameter: String
-   Defining Site: String
-   Number of Sites Reporting: Int


## Questions

1. How the Air Quality Index (AQI) changes across different regions and over time: Are there any extreme fluctuations in AQI within certain regions or shifts in patterns throughout the year?

2. How do AQI factors change over time: Are there seasonality or geographic factors that contribute to the AQI or its key contributors?

## Analysis plan
**Week 1 - EDA / Preprocessing**

This week should be focused on understanding the data and any interesting relationships between the features and the target variable (AQI value).
Next, using the findings from the EDA stage, the focus should be handling any data quality issues (missing value, encoding categorical variables, scaling values) and removing any unnecessary columns.
By the end of this week, we should have a summary of key findings from the EDA and a preprocessed dataset.
 
**Week 2 - Modeling**

This week should be focused on performing advanced modeling techniques, such as OLS and other regression models to understand the importance of the features and rank the influence that the features have on the target variable. By the end of this week, we should have a list of features that contribute to the Air Quality Index.
 
**Week 3 - Dashboard Wireframing**

This week should be focused on designing and mapping out the metrics to use on the interactive dashboard. This should include the type of visuals, the expected interactions of variables and require data structures to build the report. By the end of this week, we should have a rough sketch of the dashboard that answers the questions above.
 
**Week 4 - Dashboard Building**

This week should be focused on implementing wireframed dashboards using the Stream-lit library. This should include the building, testing, and finding key interactions between the visuals to demonstrate during the final presentation. By the end of this week, we should have a deployed dashboard with 2-3 patterns identified by the dashboard.
 
**Week 5 - Final Report**

This week should be focused on completing the final write-up and presentation. The group members for each week should discuss their decision about the work they were responsible for. By the end of the week, we should have a finalized report and recorded video. 


## Repository Structure 

**Data-** 

This folder should contain the datasets that are being used for this analysis. This folder should have a README.md  that contains the description of the dataset as well. 

**Image-** 

This folder should contain any graphs / images that we plan on using for the presentation. 

**extra-**

This folder should contain any additional notebooks that we would like to store for generating graphs. 


#### Disclosure:
Derived from the original data viz course by Mine Çetinkaya-Rundel @ Duke University
