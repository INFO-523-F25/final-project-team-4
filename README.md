[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wojP3-_r)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21237964)
# project-final

Final project repo for INFO 523 - Fall 2025.

# Data
-   Dataset 1: United States Environmental Protection Agency’s (EPA) 2025 daily Air Quality Index (AQI) dataset: contains 57,012 rows with 8 variables showing insight into daily air quality and how it changes over days, months, and seasons.
-   Dataset 2: United States Environmental Protection Agency’s 2025 daily wind dataset: contains 129,451 rows with 29 variables showing insight into daily wind speed and how it changes over regions and the year.
-   Dataset 3: United States Environmental Protection Agency’s 2025 daily temperature dataset: contains 82,755 rows with 29 variables showing insight into daily temperature and how it changes over regions and the year.
-   Source URL for all: https://aqs.epa.gov/aqsweb/airdata/download_files.html 

# High-level goal and expanded description:
The overall goal of our project is to generate an interactive dashboard that displays information about air quality in the United States over the past year. Ideally, this dashboard could serve as a tool for people to better understand the factors influencing air quality both in their area and across the United States more broadly. We are aiming to have visualizations for each of the major air pollutants in addition to an overall graph of the AQI over time. Further visualizations could include a rendering of the AQI scale showing the range from good to hazardous, a graph of the top 10 counties with the worst air quality on average, or another similar visual displaying patterns or outliers in our data. The dashboard will include filters for time period, season, and geographic region. During the EDA phase of our project, we may also choose to enrich the data further with population density by county or other key features that may provide further context to the dashboard. Our dashboard will be one page to ensure data can be easily compared and it is as intuitive to use as possible. 

# Data and motivation:  
We decided to use the United States Environmental Protection Agency’s (EPA) 2025 daily Air Quality Index (AQI) dataset by county, 2025 daily wind dataset, and 2025 daily temperature dataset. It contains 105,869 rows with 10 variables showing insight into daily air quality and how it changes over days, months, and seasons.  The datasets come from collections of air quality, wind and temperature measurements by specific monitoring stations over the year. Key variables include the location of the measurement, temperature, the AQI value (standardized value representing the pollution level), and the air quality category (qualitative variable representing how poor or great the air quality is on a scale). 
This dataset was ideal for our goal to create an interactive dashboard portraying visual patterns and trends with air quality in different regions and seasons over time. Additionally, it will allow for further discovery into the differences in air quality over weeks, months and the whole year. Furthermore, being able to create a dashboard with real environmental implications was important as we would be able to visualize how pollution has affected certain regions over the last year. Using daily data with several data points will also allow us to create a more accurate representation of pollution and air quality in different regions and seasons over 2025. Ultimately, the EPA’s daily AQI index dataset was ideal for portraying air quality in an interactive dashboard through data driven visualization.


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

This week should be focused on implementing wireframed dashboards using the Stream-lit library. This should include the building, testing, and finding key interactions between the visuals to demonstrate during the final presentation. By the end of this week, we should have a deployed dashboard with 2-3 patterns identified by the dashboard that demonstrate correlation between the AQI value and chosen features of the dashboard.
 
**Week 5 - Final Report**

This week should be focused on completing the final write-up and presentation. The group members for each week should discuss their decision about the work they were responsible for. By the end of the week, we should have a finalized report and recorded video. 


## Repository Structure 

**Data-** 

This folder should contain the datasets that are being used for this analysis. This folder should have a README.md  that contains the description of the dataset as well. 

**Image-** 

This folder should contain any graphs / images that we plan on using for the presentation. This is where the wireframe of the dashboard will 
be stored. 

**notebook-** 

This folder should contain the work that we complete each week. These notebooks should be used to demonstrate analytical thought process behind the problem and experimentation. 

**src-** 

This is where any scripts will be stored to referenced in the notebooks. This could be any custom graphing, preprocessing, or model validation functions. 

**All other files / folders** 

This items will be used to generate the final presenation and site of our findings. 


#### Disclosure:
Derived from the original data viz course by Mine Çetinkaya-Rundel @ Duke University
