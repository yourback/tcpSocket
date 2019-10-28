#include <stdio.h>
#include <string.h>
#include <stdlib.h >

#define DLLEXPORT __declspec(dllexport)
//传递与返回数值
//gcc -o libpycall.so -shared -fPIC pycall.c
DLLEXPORT char* get_order_str(int order){
    char * return_str = "";
    switch(order){
        case 0:
            return_str  = "go ahead";
            break;
        case 1:
            return_str  = "go back";
            break;
        case 2:
            return_str  = "go left";
            break;
        case 3:
            return_str  = "go right";
            break;
    }
	return return_str;
}

