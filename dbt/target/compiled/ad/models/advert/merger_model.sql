

with tempbriefing as (
    SELECT 
       *,
        ROW_NUMBER() OVER (
            PARTITION BY 
               "campaign_id"
            ORDER BY 
               "campaign_id"
        ) "row_num"
     FROM 
        "trial"."public"."briefing"
        )

-- create table if not exists public.warehouse as 
SELECT * FROM "trial"."public"."campaigns_inventory" left join "trial"."public"."design" using ("game_key") left join tempbriefing using ("campaign_id")