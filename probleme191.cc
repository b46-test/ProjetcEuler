#include <iostream>
#include <math.h>
#include<string>

using namespace std;

int nombre_de_jours=30;

int compte(string s){
//     def compte(s):
//     #print s
//     #if(not prix(s)):
//         #return 0
//     if(len(s)==nombre_de_jours):
//         return 1
//     else:
//         total=0
//         if not s.count("L"):
//             total+=compte(s+"L")
//         
//         if not s[-2:]=="AA":
//             total+=compte(s+"A")
//         
//         total+=compte(s+"O")
//         
//         return total
//     cout << s << endl;
    int longueur=s.length();
    if(longueur==nombre_de_jours){
//         cout << s << endl;
        return 1;
    }else{
        int total=0;
//         cout << (int)s.find("L")<<s<<endl;
        if((int)s.find("L")==-1){
//             cout << "Il y a pas encore eu d'absences" << s.find("L") << endl;
            total+=compte(s+"L");
        }
        if(longueur<2 || s.rfind("AA")!=longueur-2){
            total+=compte(s+"A");
        }
        
        total+=compte(s+"O");
        
        return total;
    }
    


};

int main(){
    cout <<compte("")<<endl;
}
