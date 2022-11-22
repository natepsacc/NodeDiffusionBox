const http = require('http');
const busboy = require('busboy');
const fs = require('fs');
const path = require('path');
const glob =  require('glob');


const server = http.createServer((req, res) => {

  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.write(`
      <form action="/upload" enctype="multipart/form-data" method="post">
        <input type="file" name="someCoolFiles"><br>
        <button>Upload</button>
      </form>
    `);
    res.end('<iframe src="http://192.168.86.62:3000" style="width:100vw; height:100%;"/>');
        glob("diffusionOut/outdir/*.png", function (er, files) {
      files.forEach(function(value){
        res.write('<img src="/'+ value+ '" ></img>');      });
    })
  } else if (req.url === '/upload') {
    let filename = '';
    let dirname = 'indir'
    const bb = busboy({ headers: req.headers });
    bb.on('file', (name, file, info) => {
      filename = info.filename;
      const saveTo = path.join(dirname, filename);
      file.pipe(fs.createWriteStream(saveTo));
    });
    bb.on('close', () => {
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.end(`upload success: ${filename}`);
    });
    req.pipe(bb);
  } else {
    var staticBasePath = '/diffusionOut';
    var resolvedBase = path.resolve(staticBasePath);
    var safeSuffix = path.normalize(req.url).replace(/^(\.\.[\/\\])+/, '');
    var fileLoc = path.join(resolvedBase, safeSuffix);
    
    fs.readFile(fileLoc, function(err, data) {
        if (err) {
            res.writeHead(404, 'Not Found');
            res.write('404: File Not Found!');
            return res.end();
        }
        
        res.statusCode = 200;

        res.write(data);
        return res.end();
    });  
  }
});

var express    = require('express')
var serveIndex = require('serve-index')

var app = express()

// Serve URLs like /ftp/thing as public/ftp/thing
// The express.static serves the file contents
// The serveIndex is this module serving the directory
app.use('/', express.static('diffusionOut'), serveIndex('diffusionOut', {'icons': true}))

// Listen
app.listen(3000)


server.listen(4000, () => {
  console.log('Server listening on http://localhost:4000 ...');
});
