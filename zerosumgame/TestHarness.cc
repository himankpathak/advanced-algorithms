/* Test Harness for ZeroSum Game

Reads in the data file

Checks to see whether there is a set that sums to 0 of size k or larger.

*/

#include <iostream>

#include <set>

#include "ZeroSumGame.cc"

#include <cassert>


using namespace std;
void print_set(set<int> &X) {

  cout << "{";
  for (auto p=X.begin();
       p!=X.end();
       ++p) {
    if (p!=X.begin()) {
      cout <<",";
    }
    cout << *p;
  }
  cout << "}" << endl;
}


int setsum(set<int> &Sp) {

  int sum=0;
  for (auto p=Sp.begin();
       p!=Sp.end();
       ++p) {
    sum+=(*p);
  }
  return sum;
}

bool is_subset(set<int> &witness, set<int> &S) {

  for (auto p=witness.begin();
       p!=witness.end(); ++p) {
    if (S.count(*p) == 0) {
      return false;
    }
  }
  return true;
}
       

int main() {

  set<int> S;

  int k;

  cin >> k;
  while (!cin.eof()) {
    int i;
    cin >> i;
    if (!cin.fail()) {
      S.insert(i);
    }
  }

  cout << "Answering the question:" << endl;
  cout << "Does there exist a subset of " << endl;
  print_set(S);
  cout << "of size " << k << " or larger " << endl;
  cout << "that sums to zero." << endl;
  
  ZeroSumGame obj;

  set<int> witness;
  if (obj.ToZero(k,S,witness)) {
    assert(setsum(witness) == 0);
    assert(is_subset(witness,S));
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
}
 
  
