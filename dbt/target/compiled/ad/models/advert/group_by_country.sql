

select "geo_country" , count("type")
from "trial"."public"."cleaner_model"
group by "geo_country"