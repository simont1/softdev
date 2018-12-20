//Byteme -- Robin Han & Simon Tsui
//Softdev pd8
//K28 -- Sequential Progression
//2018-12-18

var fibonacci = function(n){
    if (n < 2){
    return n;
    }
    else{
    return fibonacci(n-1) + fibonacci(n-2);
    };
};

var gcd = function(a,b){
    if(b == 0) {
        return a;
    }
    else {
        return gcd(b, a % b);
    };
};

var students = ["a", "b", "c", "d", "e"];

var randomStudent = function(){
    return students[Math.floor(Math.random() * students.length)];
};

var display1 = function(){

  var ans = fibonacci(8);
  console.log(ans);
  document.getElementById('info').innerHTML = 'fibonacci(8)';
  document.getElementById('demo').innerHTML = ans;
};
var display2 = function(){
  var ans = gcd(18, 42);
  console.log(ans);
    document.getElementById('info').innerHTML = 'gcd(18, 42)';
  document.getElementById('demo').innerHTML = ans;
};
var display3 = function(){
  var ans = (randomStudent(students));
  console.log(ans);
    document.getElementById('info').innerHTML = 'students = ["a", "b", "c", "d", "e"]';
  document.getElementById('demo').innerHTML = ans;
};


var func1 = document.getElementById("1");
func1.addEventListener('click', display1);
var func2 = document.getElementById("2");
func2.addEventListener('click', display2);
var func3 = document.getElementById("3");
func3.addEventListener('click', display3);
