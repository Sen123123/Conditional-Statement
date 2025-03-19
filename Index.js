var http = require('http')
http.createServer(function(req,res) {
    res.write('introduction to NodeJS');
    res.end();
}).listen(8080);