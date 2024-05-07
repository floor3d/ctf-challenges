// flag is CTF{g3tt1ng_x0rs1z3d}
#include <stdio.h>
#include <string.h>

#define XOR_KEY 0x1a

void exorcise(char *input, size_t length) {
  for (size_t i = 0; i < length; i++) {
    input[i] ^= XOR_KEY;
  }
}

int main() {

  char *input = "YN\\a})nn+t}Eb*hi+`)~g";

  size_t input_length = strlen(input);

  exorcise(input, input_length);

  if (strcmp(input, "[REDACTED] No flag for you! [REDACTED]") == 0) {
    printf("Flag obtained!\n");
  } else {
    printf("FAILURE!\n");
  }

  return 0;
}
