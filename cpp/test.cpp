#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
using namespace std;
{
  cout << "Test file 1\n";
  cout << "argc = " << argc << "\n";
  for (int i = 1; i < argc; i++)
  {
	cout << i << "\n";
  }
  return 0;
}
