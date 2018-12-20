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


var display1 = function(){

  //var ans = fibonacci(8);
  //console.log(ans);
  //document.getElementById('info').innerHTML = 'fibonacci(8)';
  //document.getElementById('demo').innerHTML = ans;
};


var func1 = document.getElementById("b");
func1.addEventListener('click', add1);


var add1 = function(){
    var tag = document.createElement('p');
    tag.appendChild("word");
    console.log('word');
};


