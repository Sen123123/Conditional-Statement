var fs = require('fs');
fs.unlink('TEXT.txt',function (err) 
{ if (err) throw err;
     console.log('Deleted'); 
    });
// var fs = require('fs')
// fs.writeFile('TEXT.txt','HELLO',
// function (err) {
//   if (err) throw err;
//   console.log('content changed')
// });
