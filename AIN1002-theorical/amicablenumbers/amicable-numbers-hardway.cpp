#include <iostream>

using namespace std;

int main()
{

    for (int a = 1100; a < 1300; a++)
    {
        int suma = 0;
        int sumb = 0;
        int d;

        for (int i = 1; i <= a / 2; i++)
        {
            if (a % i == 0)
            {
                suma = suma + i;
            }
        }

        for (int b = a+1; b < 1300; b++)
        {
             for (int i = 1; i <= b / 2; i++)
            {
               //if (a!=b)
                //{
                    if (b % i == 0)
                    {
                        sumb = sumb + i;
                        
                    }
                //}
            }
        

            if (suma == sumb)
            {
                d = b;
                cout << a << " and " << d << " are amicable numbers" << endl;
                break;
            }

        sumb = 0;
        
        }
    }

    return 0;
}
