#include <iostream>
#include <string>

using namespace std;
// FINISHED

int solve(string word, string keyboard)
{
    int len = word.length();

    int prev = -1;
    int time = 0;
    for(int i = 0; i < len; i ++)
        for(int j = 0; j < 26; j++)
            if(word[i] == keyboard[j])
            {
                if(prev != -1)
                    time += abs(prev - j);
                prev = j;
            }
    return time;
}

int main()
{
    int t;
    cin >> t;
    for(int i = 0; i < t; i ++)
    {
        string w, k;
        cin >> k >> w;
        cout << solve(w, k) << endl;
    }
    return 0;
}
