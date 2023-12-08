#include <stdio.h> // standard input and output library
#include <stdlib.h> // includes functions regarding memory allocation
#include <string.h> // contains string functions
#include <errno.h> // defines macros for reporting and retrieving error conditions
#include <time.h> // functions for manipulating date and time
#include <unistd.h> // contains various constants
#include <sys/types.h> // basic derived types
#include <arpa/inet.h> // defines in_addr structure
#include <sys/socket.h> // for socket creation
#include <netinet/in.h> // constants and structures for internet domain addresses

int main() {
    time_t clock;
    char dataSending[1025]; // packet in Network Communication
    int clintListn = 0, clintConnt = 0;
    struct sockaddr_in ipOfServer;
    clintListn = socket(AF_INET, SOCK_STREAM, 0); // creating socket
    memset(&ipOfServer, '0', sizeof(ipOfServer));
    memset(dataSending, '0', sizeof(dataSending));
    ipOfServer.sin_family = AF_INET;
    ipOfServer.sin_addr.s_addr = htonl(INADDR_ANY);
    ipOfServer.sin_port = htons(2017); // port number of running server
    bind(clintListn, (struct sockaddr*)&ipOfServer, sizeof(ipOfServer));
    listen(clintListn, 20);

    while(1) {
        printf("\n\nHi, I am running server. Some Client hit me\n");
        clintConnt = accept(clintListn, (struct sockaddr*)NULL, NULL);
        clock = time(NULL);
        snprintf(dataSending, sizeof(dataSending), "%.24s\r\n", ctime(&clock));
        write(clintConnt, dataSending, strlen(dataSending));
        close(clintConnt);
        sleep(1);
    }
    return 0;
}
