var watch = require('node-watch');
var low = require('lowdb');
var md5 = require('md5');
var fs = require('fs');



const FileSync = require('lowdb/adapters/FileSync');

const adapter = new FileSync('db.json');
const db = low(adapter);


// db.get('user').push({id:1,name:'Rohit'}).write()
// db.set('user.name','roy').write();




// var path = '../../project'
// watch(path,{recursive : true},function(evt,name){
// 	console.log("%s changed",name)
// });

// watch('../../project', { recursive: true }, console.log);


// Reading directires

// function read(dir,onfilecon,onerr) {
// 	fs.readdir(dir,function(err,filenames) {
// 		// if(err){
// 		// 	onError(err);
// 		// 	return;
// 		// }
// 		filenames.forEach(function(filename){
// 			var f =filename
// 			var mdhash 
// 			// console.log(filenames)

// 			fs.readFile('package.json',function(err,buf) {
// 				// if(err){
// 				// 		onError(err);
// 				// 		return;
// 				// 	}
// 				mdhash = md5(buf);
// 				db.get('files').push({filename:f ,hash:mdhash}).write();
// 			});

// 		});
// 	});
// };
// db.defaults({files:[]}).write()
// read('../../project')


var walkSync = function(dir, filelist) {
  var fs = fs || require('fs'),
      files = fs.readdirSync(dir);
  filelist = filelist || [];
  files.forEach(function(file) {
    if (fs.statSync(dir + file).isDirectory()) {
      filelist = walkSync(dir + file + '/', filelist);
    }
    else {
      filelist.push(file);
    }
  });
  return filelist;
 };

 console.log(walkSync('/home/roy/Code/project/Test/'))