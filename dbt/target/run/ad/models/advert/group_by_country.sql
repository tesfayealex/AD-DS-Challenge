
  create view "trial"."public"."group_by_country__dbt_tmp" as (
    

select "geo_country" , count("type")
from "trial"."public"."cleaner_model"
group by "geo_country"
  );