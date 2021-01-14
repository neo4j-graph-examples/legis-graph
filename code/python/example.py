# pip3 install neo4j-driver
# python3 example.py

from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
  "bolt://<HOST>:<BOLTPORT>",
  auth=basic_auth("<USERNAME>", "<PASSWORD>"))

cypher_query = '''
MATCH (s:State {code: $state})<-[:REPRESENTS]-(l:Legislator) 
RETURN l.firstName+' '+l.lastName as name
'''

with driver.session(database="neo4j") as session:
  results = session.read_transaction(
    lambda tx: tx.run(cypher_query,
                      state="NY").data())
  for record in results:
    print(record['name'])

driver.close()
