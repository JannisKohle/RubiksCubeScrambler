const { app, BrowserWindow } = require('electron')
const exec = require('child_process').exec
const fs = require("fs");

function createWindow () {
  // Create the browser window.
  let win = new BrowserWindow({
    width: 1000,
    height: 700,
    webPreferences: {
      nodeIntegration: true
    }
  })


  // and load the index.html of the app.
  win.loadFile('index.html')
}

app.whenReady().then(createWindow)


function generate() {
    exec("python3 backend.py")
}

function get_scramble () {
    var data = fs.readFileSync("scrambles.json");
    var scrambles = JSON.parse(data);

    var data = JSON.stringify(scrambles, null, 4);
    fs.writeFile("scrambles.json", data, finished);

    function finished(err) {}

    keys = Object.keys(scrambles);
    return keys.slice(-1)[0];
}
