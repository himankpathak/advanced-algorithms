//
// Test Harness for HW #1, part 3.
//
// Complete maxWIS_class.cc
// Compile
// Test as follows
// ./a.out GRAPHFILE WEIGHTSFILE
//
#include <iostream>
#include <fstream>

#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <cassert>
#include "maxWIS_class.cc"

using namespace std;

vector<set<int>> read_graph(istream &in)
{
  vector<set<int>> temp;

  int n;
  in >> n;
  temp.resize(n);
  string line;
  getline(in, line);
  for (int i = 0; i < n; i++)
  {

    getline(in, line);
    istringstream in1(line);
    int j;
    in1 >> j;
    assert(i == j);
    while (!in1.fail())
    {
      int k;
      in1 >> k;
      if (!in1.fail())
      {
        temp[i].insert(k);
      }
    }
  }
  return temp;
}

int sumweight(set<int> &S,
              vector<int> &weights)
{
  int sum = 0;
  for (set<int>::iterator p = S.begin();
       p != S.end();
       ++p)
  {
    sum += weights[*p];
  }
  return sum;
}

bool isaIS(vector<set<int>> &graph,
           set<int> &VC)
{

  for (int i = 0; i < graph.size(); i++)
  {
    for (set<int>::iterator p = graph[i].begin();
         p != graph[i].end();
         ++p)
    {
      if ((VC.count(*p) != 0) && (VC.count(i) != 0))
      {
        return false;
      }
    }
  }

  return true;
}

int main(int argv, char *argc[])
{
  assert(argv == 3); // Three arguments File1, File2, File3;

  ifstream fin2;
  ifstream fin3;

  fin2.open(argc[1]);
  fin3.open(argc[2]);

  vector<set<int>> graph;

  graph = read_graph(fin2);

  vector<int> weights;
  int N;
  fin3 >> N;
  weights.resize(N);

  for (int j = 0; j < N; j++)
  {
    fin3 >> weights[j];
  }
  assert(N == graph.size());

  // for (int i=0;i<graph.size(); i++) {
  //   cout << i << " degree = " << graph[i].size() << endl;
  // }
  set<int> T1;
  maxWIS obj;
  T1 = obj.Maximum_WIS(graph, weights);

  vector<bool> left;
  left.resize(graph.size(), true);
  cout << sumweight(T1, weights) << endl;
  for (set<int>::iterator p = T1.begin();
       p != T1.end(); ++p)
  {
    cout << *p << endl;
  }
  assert(isaIS(graph, T1));
}
