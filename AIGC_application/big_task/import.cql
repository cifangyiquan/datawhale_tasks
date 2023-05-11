LOAD CSV WITH HEADERS FROM 'file:///movies.csv' AS row
MERGE (m:Movie {name:row.Title, area:row.Area, year:row.Year, score:row.Score, info:row.Information})
WITH m, row
UNWIND split(row.Tags, '|') AS tag
MERGE (t:Tag {name: tag})
MERGE (m)-[:TYPE]->(t)
MERGE (a:Area {name: row.Area})
MERGE (m)-[:AREA]->(a)
MERGE (y:Year {name: row.Year})
MERGE (m)-[:TIME]->(y)
WITH m, row
UNWIND split(row.Directors, '|') AS director
MERGE (d:Director {name: director})
MERGE (m)-[:DIRECTOR]->(d)
WITH m, row
UNWIND split(row.Stars, '|') AS star
MERGE (st:Actor {name: star})
MERGE (m)-[:Actor]->(st)
