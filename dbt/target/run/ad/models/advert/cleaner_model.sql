

  create  table "trial"."public"."cleaner_model__dbt_tmp"
  as (
    
select *
from "trial"."public"."merger_model"
where row_num = 1
  );