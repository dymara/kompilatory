float a = 0, b = 0, c = 0;

int gcd(int m, int n) {

int res = 0;
if (m!=n) { 
    if (m > n) 
        res = gcd(m-n, n);
    else
        res = gcd(n-m, m);
}
else
    res = m;

print res;
return res;
}


while(a >= b ) {
    a = 1/2*(a+b/a);
}


