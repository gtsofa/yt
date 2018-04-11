// home.js

var button = document.querySelector('button');

button.onclick = function(){
    var name = prompt("What is your name? ");
    alert("hello, "+name+" nice to see you.");
}