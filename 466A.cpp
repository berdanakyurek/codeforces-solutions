#include <iostream>

int main()
{
    using namespace std;
    int a,b,m,n;

    cin >> n >> m >> a >> b;
    //cout << a << " " << b << " " << m << " " << n << " " << endl;

    double abonmanPerRide = (double) b / (double) m;
    int totalRidesBought = 0;
    int totalCost = 0;

    if( abonmanPerRide <= a )
    {
        totalRidesBought += n - n % m;

        if( totalRidesBought < 0 )
            totalRidesBought = 0;
        totalCost += totalRidesBought / m * b;

        if( (n - totalRidesBought)*a < b )
            totalCost += (n - totalRidesBought)*a;
        else
            totalCost += b;
    }
    else
        totalCost = a * n;

    cout << totalCost << endl;
    return 0;
}
