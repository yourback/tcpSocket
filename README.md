# tcpSocket
python tcp_socket server and client with C command resolutions</br>

# news
1 add key "space" to let machine move free</br>

2 when release keys(up down left right) send a stop order</br>

3 add thread event to control send order stop


# how to use:
C file to .so file order</br>
gcc -o py2cso.so -shared -fPIC order_analysis.c</br>

contain 6 order below</br>

up      go ahead    1</br>
down    go back     2</br>
left    go left     3</br>
right   go right    4</br>
space   move free   5</br>

the keys release all above trigger stop order 0</br>
and the keys follows will help you to define some new functions</br>

home        customize1  5</br>
end         customize2  6</br>
page_up     customize3  7</br>
page_down   customize4  8</br>

remember to write c file use these order codes</br>





