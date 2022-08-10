
{{ config(materialized='view') }}

select "site_name" , count("type")
from {{ ref('cleaner_model') }}
group by "site_name"