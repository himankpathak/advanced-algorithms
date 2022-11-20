//
// Implement this class.
//
//
#include <iostream>
#include <fstream>

#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <cassert>
#include <iterator>

using namespace std;

class maxWIS
{
private:
  // Implement whatever private functions you need.

public:
  set<int> Maximum_WIS(vector<set<int>> &graph, vector<int> &weights)
  {

    cout << "graph \n"
         << weights.size() << "\n";

    for (auto i : graph)
    {
      for (auto j : i)
      {

        cout << j << " | ";
      }

      cout << endl;
    }
    ostream_iterator<int> out_it(std::cout, ", ");
    copy(weights.begin(), weights.end(), out_it);

    set<int> T;
    return T;
  }
};
