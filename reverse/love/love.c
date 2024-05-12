#include <stdio.h>

int main() {
  // Say hello
  printf("Hello, welcome to the simple calculator program!\n");
  printf("I will now calculate my love for you!\n");

  // Calculate some math problems
  int num1 = 10;
  int num2 = 5;
  int sum = num1 + num2;
  int difference = num1 - num2;
  int product = num1 * num2;

  // Display the results
  printf("The sum of %d and %d is: %d\n", num1, num2, sum);
  printf("The difference between %d and %d is: %d\n", num1, num2, difference);
  printf("The product of %d and %d is: %d\n", num1, num2, product);

  // Say what's up
  if (num1 + num2 == 16) {
    printf("CTF{str1ngs_m3}");
  }

  // Calculate some more math problems
  int num3 = 8;
  int num4 = 4;
  int division = num3 / num4;
  int remainder = num3 % num4;

  // Display the results
  printf("The division of %d by %d is: %d\n", num3, num4, division);
  printf("The remainder when %d is divided by %d is: %d\n", num3, num4,
         remainder);

  return 0;
}
