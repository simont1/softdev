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

var students = ["a", "b", "c", "d", "e"]

var randomStudent = function(){
    return students[Math.floor(Math.random() * students.length)];
};

var display1 = function(){
  console.log(fibonacci(8));
}
var display2 = function(){
  console.log(gcd(18, 42));
}
var display3 = function(){
  console.log(randomStudent(students));
}

var clicked1 = document.getElementById("1");
clicked1.addEventListener('click', display1);

var clicked2 = document.getElementById("2");
clicked2.addEventListener('click', display2);

var clicked3 = document.getElementById("3");
clicked3.addEventListener('click', display3);


var display4 = document.getElementById("4");


if(clicked1){
  display4.innerHTML = fibonacci(8);
}
else if(clicked2){
  display4.innerHTML = gcd(18,42);
}
else if(clicked3){
  display4.innerHTML = randomStudent(students);
}
