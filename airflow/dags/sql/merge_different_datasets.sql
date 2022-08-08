create temporary table if not exists tempbriefing as
    SELECT 
       *,
        ROW_NUMBER() OVER (
            PARTITION BY 
               campaign_id
            ORDER BY 
               campaign_id
        ) row_num
     FROM 
        public.briefing;

create table if not exists public.warehouse as 
SELECT * FROM public.campaigns_inventory left join public.design using (game_key) left join tempbriefing using (campaign_id);