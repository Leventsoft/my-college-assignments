#include <iostream>

using namespace std;

int main() {

    int b, d;

    for (int a = 1100; a < 1300; a++)
    {
        int suma = 0;
        int sumb = 0;

        for (i = 0; i <= a/2; i++)
        {
            if (a % i == 0)
            {
                suma = suma + i;
            
            }
            
        }


        if (suma == sumb)
        {
            cout << a << "and" << b << "are amicable numbers" << endl;
            break;
        }
    }
    

    return 0;
}
