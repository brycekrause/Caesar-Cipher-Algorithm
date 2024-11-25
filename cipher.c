#include <stdio.h>
#include <string.h>
#include <ctype.h>

void encrypt(char text[], int shift, char result[]){
    char string[255];
    for (int i = 0; i < strlen(text); i++){
        int ascii = text[i];
        if (isupper(text[i])){
            result[i] = (ascii - 'A' + shift) % 26 + 'A';
        }else if (islower(text[i])){
            result[i] = (ascii  - 'a' + shift) % 26 + 'a';
        }else{
            result[i] = ascii;
        }
    }
    result[strlen(text)] = '\0';
}

void decrypt(char text[], int shift, char result[]){
    char string[255];
    for (int i = 0; i < strlen(text); i++){
        int ascii = text[i];
        if (isupper(text[i])){
            result[i] = (ascii - 65 - shift  + 26) % 26 + 65;
        }else if (islower(text[i])){
            result[i] = (ascii - 97 - shift + 26) % 26 + 97;
        }else{
            result[i] = ascii;
        }
    }
    result[strlen(text)] = '\0';
}

int main() {
    char encrypted_text[255];
    char decrypted_text[255];
    
    char str[] = "The quick brown fox jumps over the lazy dog";
    int shift = 3;
    encrypt(str, shift, encrypted_text);
    printf("%s\n", encrypted_text);
    decrypt(encrypted_text, shift, decrypted_text);
    printf("%s", decrypted_text);
    
    

    return 0;
}