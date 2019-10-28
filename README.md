# tcpSocket
python tcp_socket server and client with C command resolutions


# news
1 add key "space" to let machine move free

2 when release keys(up down left right) send a stop order  


# how to use:
C file to .so file order 
//gcc -o py2cso.so -shared -fPIC order_analysis.c

contain 6 order below

up      go ahead    1
down    go back     2
left    go left     3
right   go right    4
space   move free   5

the keys release all above trigger stop order 0
and the keys follows will help you to define some new functions

home        customize1  5
end         customize2  6
page_up     customize3  7
page_down   customize4  8

remember to write c file use these order codes





