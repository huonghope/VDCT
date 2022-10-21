#include <iostream>

using namespace std;

int main() {
    int a[10];
    a[11] = 1;
    cout << "hi";

    return 0;
}

void test() {
  char x[4];
  char *y = "abcd";

  strcpy(x, y); // warn
}