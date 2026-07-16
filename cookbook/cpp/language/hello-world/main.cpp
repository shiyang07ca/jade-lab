#include <iostream>

using namespace std;

void fn() {
    int i = 0;
    do {
        break;
        i++;
    } while( i<5 );
// while (i < 5) {
//     if (i == 1) break;
//         i++;
//     }
}

int main()
{
    for (int i = 0; i < 20; i++) {
        fn();
        printf("%d ", i);
    }
}
