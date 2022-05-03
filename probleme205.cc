#include <iostream>
#include <math.h>

using namespace std;




int main(){
    double j;
    int64_t max=pow(2,50);
    cout << max << endl;
    for(int64_t i=0;i<max;i++){
        if(i%10000000==0){
            cout << i << "\t" << max << endl;
        }
    }
}
