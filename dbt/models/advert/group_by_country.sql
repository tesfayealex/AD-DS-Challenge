
{{ config(materialized='view') }}

select "geo_country" , count("type")
from {{ ref('cleaner_model') }}
group by "geo_country"