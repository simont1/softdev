//Simon Tsui
//Softdev pd8
//K30 -- Sequential Progression III: Season of the Witch
//2018-12-21F

var fibonacci = function(n){
    if (n < 2){
    return n;
    }
    else{
    return fibonacci(n-1) + fibonacci(n-2);
    };
};


var target = document.getElementById("thelist");
var fibby = document.getElementById("fiblist");
var fibCtr = 1;

var add1 = function(){
    var tag = document.createElement('li');
    var node = document.createTextNode("word");
    tag.addEventListener("mouseover", changeHeading);
    tag.addEventListener("mouseout", function() {
        document.getElementById("h").innerHTML = "Hello World!";
    });
    tag.addEventListener("click", removeItem);
    tag.appendChild(node);
    target.appendChild(tag);
    console.log('word');
};

var changeHeading = function(e) {
    var heading = document.getElementById("h");
    heading.innerHTML = this.innerHTML;
};

var removeItem = function(e) {
    this.remove();
    var heading = document.getElementById("h");
    heading.innerHTML = "Hello World!";
};

var lis = document.getElementsByTagName("li");
for (var i = 0; i < lis.length; i++) {
    lis[i].addEventListener("mouseover", changeHeading);
    lis[i].addEventListener("mouseout", function() {
        document.getElementById("h").innerHTML = "Hello World!";
    });
    lis[i].addEventListener("click", removeItem);
};

var fibAdd = function(){
  var total = fibonacci(fibCtr);
  fibCtr += 1;
  var tag = document.createElement('li');
  var node = document.createTextNode(total);
  tag.appendChild(node);
  fibby.appendChild(tag);
  console.log(total);
}

var func1 = document.getElementById("b");
func1.addEventListener('click', add1);
var func2 = document.getElementById("fb");
func2.addEventListener("click", fibAdd);
