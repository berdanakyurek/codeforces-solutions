#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    int n, k;
    for(int i = 0; i < t; i ++)
    {
        cin >> n >> k;


        unsigned long long int arr[n];
        int inp;
        for(int j = 0; j < n; j ++)
        {

            cin >> inp;
            arr[j] = pow(10, inp );

        }

        int noOfBanknotes = 0;
        unsigned long long int totalMoney = 0;
        for(int j = 0; j < n; j ++)
        {

            int maxNumber;

            if(j == n - 1)
                maxNumber = -1;
            else
                maxNumber = arr[j+1] / arr[j] - 1;

            if(maxNumber != -1 && noOfBanknotes + maxNumber <= k)
            {
                noOfBanknotes += maxNumber;
                totalMoney += maxNumber * arr[j];
            }
            else
            {
                totalMoney += (k+1 - noOfBanknotes)*arr[j];
                noOfBanknotes += k + 1 - noOfBanknotes ;
                break;
            }
        }
        cout << totalMoney << endl;
    }

    return 0;
}
