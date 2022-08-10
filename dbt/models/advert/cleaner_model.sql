
{{ config(materialized='table') }}
select *
from {{ ref('merger_model') }}
where row_num = 1