var fs = require('fs');
fs.writeFile('CIC.txt','On trial',
function(err) {
  if (err) throw err; 
  console.log('Hork in progress')
});

