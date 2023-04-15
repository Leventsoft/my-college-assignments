#include <iostream>

using namespace std;

int sum(int number)
{
    int sum = 0;
    for (int i = 1; i < number; i++)
    {
        if(number % i == 0)
        {
            sum += i;
        }

    }
    return sum;
}

int main()
{
    int a, b;
    for (int i = 1100; i <= 1300; i++)
    {
        a = i;
        b = sum(a);

        if (a == sum(b) && b < 1300 && b > 1100)
        {
            cout << a << " and " << b << " are friendly numbers." << endl;
            break;
        }
    }
    
    
}