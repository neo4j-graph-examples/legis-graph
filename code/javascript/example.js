// npm install --save neo4j-driver
// node example.js
const neo4j = require('neo4j-driver');
const driver = neo4j.driver('neo4j://<HOST>:<BOLTPORT>',
                  neo4j.auth.basic('<USERNAME>', '<PASSWORD>'), 
                  {});

const query =
  `
  MATCH (s:State {code: $state})<-[:REPRESENTS]-(l:Legislator)
  RETURN l.firstName+' '+l.lastName as name
  `;

const params = {"state": "NY"};

const session = driver.session({database:"neo4j"});

session.run(query, params)
  .then((result) => {
    result.records.forEach((record) => {
        console.log(record.get('name'));
    });
    session.close();
    driver.close();
  })
  .catch((error) => {
    console.error(error);
  });
