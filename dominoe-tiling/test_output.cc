#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cassert>
#include <sstream>
#include <set>

using namespace std;
vector<pair<int, int>> read_pieces(ifstream &fin)
{
  vector<pair<int, int>> pieces;
  while (!fin.fail())
  {
    int i;
    int j;
    char c;
    fin >> i;
    fin >> c;
    fin >> j;

    if (!fin.fail())
    {
      pieces.push_back(make_pair(i, j));
    }
  }

  return pieces;
}

vector<string> read_board(ifstream &fin)
{
  vector<string> board;
  while (!fin.fail())
  {
    string line;
    getline(fin, line);
    if (!fin.fail())
    {
      board.push_back(line);
    }
  }

  return board;
}
bool valid2(int i, int l)
{
  if (i < 0)
    return false;
  if (i >= l)
    return false;
  return true;
}

bool valid(int i, int j, int l, int m)
{
  if (i < 0)
    return false;
  if (j < 0)
    return false;
  if (i >= l)
    return false;
  if (j >= m)
    return false;
  return true;
}

pair<int, int> dirs(int d)
{
  int dirx, diry;

  if (d == 0)
  {
    dirx = 0;
    diry = 1;
  }
  if (d == 1)
  {
    dirx = 1;
    diry = 0;
  }
  if (d == 2)
  {
    dirx = -1;
    diry = 0;
  }
  if (d == 3)
  {
    dirx = 0;
    diry = -1;
  }
  return make_pair(dirx, diry);
}

vector<pair<int, int>> locs(vector<string> &board, char c)
{
  vector<pair<int, int>> locs_ret;
  for (int i = 0; i < board.size(); i++)
  {
    for (int j = 0; j < board[i].size(); j++)
    {
      if (board[i][j] == c)
      {
        locs_ret.push_back(make_pair(i, j));
      }
    }
  }
  return locs_ret;
}

bool sat_constraints(vector<pair<int, int>> &pieces,
                     vector<string> &board,
                     vector<string> &sol)
{
  vector<bool> found;
  set<pair<int, int>> found_pieces;

  found.resize(pieces.size(), false);

  for (int i = 0; i < board.size(); i++)
  {
    for (int j = 0; j < board[i].length(); j++)
    {
      if (board[i][j] != ' ')
      {
        vector<pair<int, int>> locs_ret;
        locs_ret = locs(sol, sol[i][j]);
        if (locs_ret.size() != 2)
        {
          cout << "# of matches " << locs_ret.size() << endl;
          return false;
        }
        int a, b, c;
        a = abs(locs_ret[0].first - locs_ret[1].first);
        b = abs(locs_ret[0].second - locs_ret[1].second);
        c = a + b;
        if (a + b != 1)
        {
          cout << "Failed not close -- " << a << " " << b << endl;
          return false;
        }
        int x, y;
        x = board[locs_ret[0].first][locs_ret[0].second] - '0';
        y = board[locs_ret[1].first][locs_ret[1].second] - '0';

        pair<int, int> found;

        if (x < y)
        {
          found = make_pair(x, y);
        }
        else
        {
          found = make_pair(y, x);
        }
        found_pieces.insert(found);
      }
    }
  }
  // sort(found_pieces.begin(),found_pieces.end());
  sort(pieces.begin(), pieces.end());
  for (int i = 0; i < pieces.size(); i++)
  {
    if (found_pieces.count(pieces[i]) == 0)
    {
      cout << "Not found" << pieces[i].first << " " << pieces[i].second << endl;
    }
  }

  if (found_pieces.size() == pieces.size())
  {
    return true;
  }
  else
  {
    cout << found_pieces.size() << endl;
    cout << pieces.size() << endl;
    cout << "Failed -- vecs sizes not equal " << endl;
    return false;
  }
}

int main(int argc, char *argv[])
{

  ifstream fin;
  ifstream fin1;
  ifstream fin2;
  fin.open(argv[1]);
  fin1.open(argv[2]);
  fin2.open(argv[3]);

  vector<pair<int, int>> pieces;
  vector<string> board;
  vector<string> sol;
  pieces = read_pieces(fin);

  board = read_board(fin1);
  sol = read_board(fin2);

  if (sat_constraints(pieces, board, sol))
  {
    cout << "Correct Solution" << endl;
  }
  else
  {
    cout << "Error" << endl;
  }
}
