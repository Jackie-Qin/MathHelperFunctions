#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <cmath>
using namespace std;


//Evaluate the polynomial at the point indicated by using Horner’s algorithm.
//Ex: p(x) = x^5 − 3x^3 − 4x^2 + 10 at x = 2
vector<int> Hornor(vector<int> p, int x){
    vector<int> res;
    int temp = p[0];
    res.push_back(p[0]);
    for(int i = 1; i < p.size(); ++i){
        temp = x * temp + p[i];
        res.push_back(temp);
    }
    return res;
}



//correctly to specific decimal places (rounded) for numerator and denominator respectively.
double Tay_natural(double x, int digits){
    int factorial = 1;
    double errorTerm = 1;
    int i = 1;
    for(;; ++i){
        factorial *= i;
        errorTerm = pow(x, i) / factorial;
        if(abs(errorTerm) < (pow(10, -1 * digits) / 2)) break;
    }
    double actualTerm = 1;
    factorial = 1;
    for(int j = 1; j < i + 1; ++j){
        factorial *= j;
        actualTerm += pow(x, j) / factorial;
    }
    return actualTerm;
}


double Tay_cos(double x, int digits){
    int factorial = 1;
    double errorTerm = 1;
    int i = 1;
    for(;; i = i + 2){
        factorial = factorial * i * (i + 1);
        errorTerm = pow(x, 2 * i) / factorial;
        if(abs(errorTerm) < (pow(10, -1 * digits) / 2)) break;
    }
    double actualTerm = 1;
    factorial = 1;
    int sign = 1;
    for(int j = 1; j < (i + 1) / 2; j = j + 2){
        factorial = factorial * j * (j + 1);
        if(sign % 2 == 1) {
            actualTerm -= pow(x, j + 1) / factorial;
        } else {
            actualTerm += pow(x, j + 1) / factorial;
        }
        ++sign;
    }
    return actualTerm;
}


double Tay_sin(double x, int digits){
    int factorial = 1;
    double errorTerm = x;
    int i = 1;
    for(;; i = i + 2){
        factorial = factorial * (i + 1) * (i + 2);
        errorTerm = pow(x, 2 * i + 1) / factorial;
        if(abs(errorTerm) < (pow(10, -1 * digits) / 2)) break;
    }
    double actualTerm = x;
    factorial = 1;
    int sign = 1;
    for(int j = 1; j < (i + 1) / 2; j = j + 2){
        factorial = factorial * (j + 1) * (j + 2);
        if(sign % 2 == 1) {
            actualTerm -= pow(x, j + 2) / factorial;
        } else {
            actualTerm += pow(x, j + 2) / factorial;
        }
        ++sign;
    }
    return actualTerm;
}


//Greatest common divisor
int gcd(int a, int b){
    if (b == 0) return a;
    if (b > a){
        int temp = a;
        a = b;
        b = temp;
    }
    return gcd(b, a % b);
}


//find x and y, s.t. ex + phiy = 1;
void EuclideanAlgo(int e, int phi){
    if (gcd(e,phi) != 1) {
        cout << "They are not coprime." << endl;
        return;
    }
    int x = 1;
    int y = 1;
    while(e * x - phi * y != 1){
        if( e * x - phi * y > 0) {
            ++y;
        } else {
            ++x;
        }
    }
    cout << "x = " << x << ", y = " << y;
    return;
}


//find (base^power) (mod num)
int expMod(int base, int power, int mod){
    int res = 1;
    base = base % mod;

    if (base == 0) return 0;

    while (power > 0){
        if (power % 2 == 1) res = (res * base) % mod;
        power = power / 2;
        base = (base * base) % mod;
    }
    return res;
}


int twoMod(int a, int b, int mod){
    return (a * b) % mod;
}


int main(){


    return 0;
}
