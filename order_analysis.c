#include <stdio.h>
#include <string.h>
#include <stdlib.h >

#define DLLEXPORT __declspec(dllexport)
//传递与返回数值
//gcc -o py2cso.so -shared -fPIC order_analysis.c
DLLEXPORT char* get_order_str(int order){
    char * return_str = "";
    switch(order){
        case 0:
            return_str  = "stop";
            break;
        case 1:
            return_str  = "go ahead";
            break;
        case 2:
            return_str  = "go back";
            break;
        case 3:
            return_str  = "go left";
            break;
        case 4:
            return_str  = "go right";
            break;
        case 5:
            return_str  = "move free";
            break;
        case 6:
            return_str  = "customize1";
            break;
        case 7:
            return_str  = "customize2";
            break;
        case 8:
            return_str  = "customize3";
            break;
        case 9:
            return_str  = "customize4";
            break;
        case 10:
            return_str  = "get_status";
            break;
    }
	return return_str;
}

