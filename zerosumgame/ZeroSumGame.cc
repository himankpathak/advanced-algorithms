//
// Fill in the details in this code.
//
#include <set>
#include <iostream>
#include <vector>
#include <bitset>

using namespace std;

class ZeroSumGame
{

  // Write the following function
  // ToZero
  // Input --- k
  //           set<int> S
  // Output --- True if there exists a set Sp (subset of S)
  //            such that the sum of the elements in Sp is 0
  //            and |Sp| >=k
  //       ---  False otherwise
  // If this function returns true, then Sp is the witness.
  //
private:
  // Use any private functions that you want.
  set<int> getEl(std::vector<std::vector<std::vector<set<int>>>> arr, int k, int i, int j)
  {
    std::set<int> empty;
    if (k < 0 || i < 0 || j < 0 || j >= arr[0][0].size())
    {
      return empty;
    }
    return arr[k][i][j];
  }

public:
  bool ToZero(int k,
              const set<int> &S,
              set<int> &Sp)
  {
    // Implement this code.   If there exists a set with at least k elements
    // that adds to 0, return true -- and, set Sp to be the set.
    // Else return false.

    std::vector<int> inp(S.begin(), S.end());
    int n = S.size();

    int sumplus = 0, summinus = 0;

    for (int i : inp)
    {
      if (i > 0)
      {
        sumplus += i;
      }
      else
      {
        summinus += i;
      }
    }

    std::vector<std::vector<std::vector<set<int>>>> arr;
    set<int> empty;

    int j_max = abs(summinus) + sumplus + 1;
    arr.resize(n, std::vector(n, std::vector<set<int>>(j_max)));

    for (vector<int>::size_type ki = 0; ki != n; ki++)
    {
      for (vector<int>::size_type i = 0; i != n; i++)
      {
        for (vector<int>::size_type j = 0; j != j_max; j++)
        {
          if (ki == 1)
          {

            if ((j - abs(summinus)) == inp[i])
            {
              arr[ki][i][j] = {inp[i]};
            }
          }
          else
          {
            set<int> prev = getEl(arr, ki, i - 1, j);
            if (!prev.empty())
            {
              arr[ki][i][j] = prev;
            }
            else
            {
              set<int> curr = getEl(arr, ki - 1, i - 1, j - inp[i]);

              set<int> setcurr;
              if (!curr.empty())
              {
                setcurr = curr;
                setcurr.insert(inp[i]);
              }
              arr[ki][i][j] = setcurr;
            }
          }
        }
      }
    }

    bool ans = false;
    for (auto i = k; i != arr.size(); i++)
    {
      if (!arr[i][n - 1][abs(summinus)].empty())
      {
        // for (int i : arr[i][n - 1][abs(summinus)])
        // {
        //   cout << " " << i;
        // }
        ans = true;
        Sp = arr[i][n - 1][abs(summinus)];
        break;
      }
    }

    return ans;
  }
};
