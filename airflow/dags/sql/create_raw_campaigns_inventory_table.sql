create table IF NOT EXISTS "campaigns_inventory" (
    "type" varchar(19), 
    "width" text null,
    "height" text null, 
    "campaign_id" varchar(7), 
    "creative_id" varchar(8), 
    "auction_id" varchar(36), 
    "browser_ts" timestamptz, 
    "game_key" varchar(99), 
    "geo_country" text null, 
    "site_name" text, 
    "platform_os" varchar(7), 
    "device_type" text null, 
    "browser" varchar(26) null)