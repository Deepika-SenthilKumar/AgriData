#1. Year-wise Trend of Rice Production Across States (Top 3 states)
"""SELECT YEAR, STATE_NAME, SUM(RICE_PRODUCTION) AS TOTAL_RICE_PRODUCTION
FROM agriculture_data
GROUP BY YEAR, STATE_NAME
ORDER BY YEAR, TOTAL_RICE_PRODUCTION DESC
LIMIT 3;"""
#2. Top 5 Districts by Wheat Yield Increase Over the Last 5 Years
#Dataset ends in 2017 → last 5 years = 2013–2017)
"""SELECT DIST_NAME,
       (MAX(WHEAT_YIELD) - MIN(WHEAT_YIELD)) AS YIELD_INCREASE
FROM agriculture_data
WHERE YEAR BETWEEN 2013 AND 2017
GROUP BY DIST_NAME
ORDER BY YIELD_INCREASE DESC
LIMIT 5;"""
#3. States with the Highest Growth in Oilseed Production (5-Year Growth Rate)
"""SELECT STATE_NAME,
       (MAX(OILSEEDS_PRODUCTION) - MIN(OILSEEDS_PRODUCTION)) / MIN(OILSEEDS_PRODUCTION) * 100 AS GROWTH_PERCENT
FROM agriculture_data
WHERE YEAR BETWEEN 2013 AND 2017
GROUP BY STATE_NAME
ORDER BY GROWTH_PERCENT DESC
LIMIT 5; """
#4. District-wise Correlation Between Area and Production (Rice, Wheat, Maize)
"""SELECT DIST_NAME, YEAR, 'RICE' AS CROP, RICE_AREA AS AREA, RICE_PRODUCTION AS PRODUCTION
FROM agriculture_data
UNION ALL
SELECT DIST_NAME, YEAR, 'WHEAT', WHEAT_AREA, WHEAT_PRODUCTION
FROM agriculture_data
UNION ALL
SELECT DIST_NAME, YEAR, 'MAIZE', MAIZE_AREA_HA, MAIZE_PRODUCTION
FROM agriculture_data; """
#5. Yearly Production Growth of Cotton in Top 5 Cotton Producing States
"""SELECT YEAR, STATE_NAME, SUM(COTTON_PRODUCTION) AS TOTAL_COTTON_PRODUCTION
FROM agriculture_data
GROUP BY YEAR, STATE_NAME
ORDER BY TOTAL_COTTON_PRODUCTION DESC
LIMIT 5;"""
#6. Districts with the Highest Groundnut Production in 2020
# Dataset ends in 2017 
"""SELECT DIST_NAME, SUM(GROUNDNUT_PRODUCTION) AS TOTAL_GROUNDNUT_PRODUCTION
FROM agriculture_data
WHERE YEAR = 2017
GROUP BY DIST_NAME
ORDER BY TOTAL_GROUNDNUT_PRODUCTION DESC
LIMIT 5;"""
#7. Annual Average Maize Yield Across All States
"""SELECT YEAR, STATE_NAME, AVG(MAIZE_YIELD) AS AVG_MAIZE_YIELD
FROM agriculture_data
GROUP BY YEAR, STATE_NAME
ORDER BY YEAR, STATE_NAME;"""
#8. Total Area Cultivated for Oilseeds in Each State
"""SELECT STATE_NAME, SUM(OILSEEDS_AREA) AS TOTAL_OILSEEDS_AREA
FROM agriculture_data
GROUP BY STATE_NAME
ORDER BY TOTAL_OILSEEDS_AREA DESC;"""
#9. Districts with the Highest Rice Yield
"""SELECT DIST_NAME, AVG(RICE_YIELD) AS AVG_RICE_YIELD
FROM agriculture_data
GROUP BY DIST_NAME
ORDER BY AVG_RICE_YIELD DESC
LIMIT 5; """
#10.Compare the Production of Wheat and Rice for the Top 5 States Over 10 Years
#FINDING FIRST FOR TOP 5 STATES
"""WITH state_totals AS (
    SELECT
        STATE_NAME,SUM(RICE_PRODUCTION) AS total_rice_prod,
        SUM(WHEAT_PRODUCTION) AS total_wheat_prod
    FROM agriculture_data
    GROUP BY STATE_NAME
),
top_5_states AS (
    SELECT
        STATE_NAME
    FROM state_totals
    ORDER BY (total_rice_prod + total_wheat_prod) DESC
    LIMIT 5
)
SELECT
    a.STATE_NAME,
    a.YEAR,
    SUM(a.RICE_PRODUCTION) AS rice_production,
    SUM(a.WHEAT_PRODUCTION) AS wheat_production
FROM agriculture_data a
JOIN top_5_states t
    ON a.STATE_NAME = t.STATE_NAME
WHERE a.YEAR BETWEEN 2010 AND 2019
GROUP BY a.STATE_NAME, a.YEAR
ORDER BY a.STATE_NAME, a.YEAR;"""