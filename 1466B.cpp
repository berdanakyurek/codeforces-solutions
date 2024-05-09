#include <iostream>

int main()
{
    using namespace std;

    int t;
    cin >> t;

    for(int i = 0; i < t; i++)
    {
        int len;
        cin >> len;
        int song[len];
        int div = 0;
        bool inc = false;
        int incNo = 0;
        for(int j = 0; j < len; j ++)
        {
            cin >> song[j];

            if(song[j] > incNo)
                inc = false;

            if(j == 0)
                div ++;
            else if(song[j] > song[j - 1])
            {
                if(inc || incNo == song[j] - 1)
                {
                    incNo = song[j];
                    song[j] ++;
                }
                else
                    inc = false;

                div ++;
            }
            else if(song[j] == song[j-1])
            {
                if(!inc && incNo != song[j])
                {
                    div ++;
                    incNo = song[j];
                    song[j] ++;
                    inc = true;
                }
            }
            else
            {
                bool tempFlg = false;
                for(int n = j - 2; n >= 0; n --)
                {
                    if(song[j] == song[n])
                    {
                        tempFlg = true;
                        break;
                    }
                    else if(song[n] <= song[j]-2)
                        break;
                }

                if(!tempFlg)
                    div ++;
            }

            // cout << "div= " << div << endl;
            // for(int w = 0; w <= j; w ++)
            //     cout << song[w] << " ";
            // cout << endl;
        }
        cout << div << endl;

        // for(int j = 0; j < len; j ++)
        //         cout << song[j] << " ";
        //     cout << endl;


    }
}
