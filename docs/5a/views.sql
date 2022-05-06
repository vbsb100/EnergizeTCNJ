drop VIEW IF EXISTS totalUsage;
CREATE VIEW totalUsage AS 
SELECT meter_name , sum(usage_quantity) as Total_Usage
FROM metrics
GROUP BY meter_name
ORDER BY meter_name;

drop VIEW IF EXISTS totalEmissions;
CREATE VIEW totalEmissions AS 
SELECT * FROM totalUsage
NATURAL JOIN meters;

drop VIEW IF EXISTS totalAvgEmissions;
CREATE VIEW totalAvgEmissions AS 
SELECT meter_name, meter_type, Total_usage*avg_emissions as estCO2Emission
FROM totalEmissions
NATURAL JOIN emissions;

drop VIEW IF EXISTS totalCost;
CREATE VIEW totalCost AS 
SELECT meter_name, sum(cost) as Total_Cost , sum(usage_quantity) as Total_Usage
FROM metrics
GROUP BY meter_name
ORDER BY meter_name;
