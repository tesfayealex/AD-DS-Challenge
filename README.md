# AD-DS-Challenge

- Adludio, an online mobile ad business , wants to develop a Machine Learning framework in a modular way to determine the KPI likelihood (engagement & click) of an impression. The goal of this challenge is to provide an implementation that satisfies the requirements for the tasks listed below and demonstrate your coding style and software design and engineering skills.
    - Data Engineering Skills
    - Machine learning skills

**Table of content**

[AD-DS-Challenge](#AD-DS-Challenge)

- [Included Technologies and tools](#Included-Technologies-and-tools)
- [Dev setup](#Dev-setup)
- [Project Structure](#project-structure)
  - [airflow](#airflow)
  - [data](#data)
  - [dbt](#dbt)
  - [images](#images)
  - [notebooks](#notebooks)
  - [scripts](#scripts)

## Included Technologies and Tools

<p>
Apache Airflow - A workflow manager to schedule, orchestrate & monitor workflows. Directed acyclic graphs (DAG) are used by Airflow to control workflow orchestration.
</p>
<p>
Postgresql - is an object-relational database management system (ORDBMS) with an emphasis on extensibility and standards compliance. It is used as the primary data 
store or data warehouse for many webs, mobile, geospatial, and analytics applications.
</p>
<p>
DBT (data build tool) - enables transforming data in warehouses by simply writing select statements. It handles turning these select statements into tables and views.
</p>

## Dev Setup

    Clone this repo

      https://github.com/tesfayealex/AD-DS-Challenge

    Install python requirements

      cd  AD-DS-Challenge
      pip install -r requirements
    
    Run docker scripts to install docker and airflow
        cd docker-scripts
        ./docker_setup.sh
        cd ../
        docker-compose up

## airflow
    - dags - holds dag and sql files taht will be executed as an ETL pipeline
    - logs - holds log data for airflow dags

## data
    - holds data v ersions used in the project

## dbt
    - holds modeling sql files

## images
    - holds images produced by the project

## notebooks
    - bonus task - holds image processing and analysis
    - EDA - holds warehouse insights and processes
    - Impression_prediction - holds trial on predicting impression types
    - kpi_likelihood_model - holds main kpi prediction models
    - preprocessing - holds data preprocessing codes 
## scripts
    - holds helper script files to be used 
