#include <iostream>
#include <math.h>

using namespace std;



float f(float x){
//     f(x) = ⌊2^(30.403243784-x^(2))⌋ × 10^(-9
    return float(int(pow(2,(30.403243784-pow(x,2)))))/pow(10,9);
}

int main(){
    cout.precision(10);
    cout << f(-1) << endl;
    
}
