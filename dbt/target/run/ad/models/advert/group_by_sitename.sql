
  create view "trial"."public"."group_by_sitename__dbt_tmp" as (
    

select "site_name" , count("type")
from "trial"."public"."cleaner_model"
group by "site_name"
  );