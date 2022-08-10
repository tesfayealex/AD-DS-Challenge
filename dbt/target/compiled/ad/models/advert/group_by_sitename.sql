

select "site_name" , count("type")
from "trial"."public"."cleaner_model"
group by "site_name"