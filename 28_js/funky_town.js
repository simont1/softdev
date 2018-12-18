var fib = function(n){
    if( n < 2){
	return n;
    }
    else{
	return fib(n-2) + fib(n-1);
    };
};


var gcd = function(a, b){
    if( b == 0){
	return a ;
    }
    else{
	return gcd( b, a%b);
    }
};

var randomStudent = function(a){
    return a[Math.floor(Math.random() * a.length)]
}
