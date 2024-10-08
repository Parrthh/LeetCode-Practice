# Write your MySQL query statement below
WITH firstlogin AS (
    SELECT player_id, MIN(event_date) AS first_login_date 
    -- MIN(event_date) -> gives us the earliest login date
    -- GROUP BY player_id -> ensures you get the earliest date for each player
    FROM Activity
    GROUP BY player_id
),
nextdaylogin AS (
    SELECT fl.player_id 
    FROM firstlogin fl
    JOIN Activity a
    -- To check if there is any entry in the "Activity" table for the next day for the same player
    ON fl.player_id = a.player_id
    -- To calculate the day after the first login date
    AND Date_Add( fl.first_login_date, INTERVAL 1 DAY) = a.event_date
)
SELECT ROUND(COUNT(DISTINCT ndl.player_id)/COUNT(DISTINCT fl.player_id), 2) AS FRACTION
FROM firstlogin fl
LEFT JOIN nextdaylogin ndl
ON fl.player_id = ndl.player_id;