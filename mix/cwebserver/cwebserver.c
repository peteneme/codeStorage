#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <stdbool.h>
#include <stdarg.h>
#include <unistd.h>
#include <netdb.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>


// DEFINITIONS ----------------------------------------------------------------
#define DEFAULT_PORT  80
#define STRING_LEN    10

#define EMERGENCY_LOGLEVEL 0	
#define ALERT_LOGLEVEL	   1
#define CRITICAL_LOGLEVEL  2	
#define ERROR_LOGLEVEL	   3
#define WARNING_LOGLEVEL   4
#define NOTICE_LOGLEVEL    5	
#define INFO_LOGLEVEL      6
#define DEBUG_LOGLEVEL     7

// GLOBAL VARIABLES -----------------------------------------------------------
int loglevel_set = EMERGENCY_LOGLEVEL;


// FUNCTION DECLARATIONS ------------------------------------------------------
void help_text(void);
void dbg_printf(int level, const char *fmt, ...);
void exit_if_error(void);
void print_chunk(char *msg, char *chunked_msg);


// FUNCTION DEFINITIONS -------------------------------------------------------
void help_text(void) {
    printf("Input CLI parameters:\n");
    printf("--help               - Print help\n");
    printf("--port NUMBER        - Webserver PORT NUMBER\n");
    printf("--keep-alive         - Switch on keep-alive, by default is off\n");
    printf("--root_dir DIRECTORY - Set webserver root directory, by default is ./ \n");
    printf("--chunked            - Switch on http1.1 chunked mode, by default is off\n");
    printf("--loglevel NUMBER    - Switch on debug level, by default is OFF, use 0..7, 7 is debug\n");
}

void dbg_printf(int level, const char *fmt, ...)
{
    if (level<=loglevel_set) {
        va_list args;
        va_start(args, fmt);
        vfprintf(stderr, fmt, args);
        va_end(args);
    }
}

void print_chunk(char *msg, char *chunked_msg) {
    sprintf(chunked_msg, "\r\n%X\r\n%s", (int)strlen(msg), msg);
}



void exit_if_error(void)
{
    if (errno>0) {
        perror("ERR:");
        exit(errno);
    }    
}


// MAIN ***********************************************************************
int main(int argc, char* argv[])
{
    int used_port     = DEFAULT_PORT;
    bool keep_alive    = false;
    bool chunked_mode = false;
    char root_dir[256] = "./";

    // CLI PARAMETERS PARSING
    if(argc>1) {
        int counter;
        for(counter=0; counter<argc; counter++) {
            if (strcmp(argv[counter], "--help")==0) { help_text(); return errno; };
            if (strcmp(argv[counter], "--port")==0) 
                // JUST IGNORE NON-INTERGER VALUES OR NEXT OR NON-EXISTING PARAMETERS
                if (counter+1<argc)
                    if ((atoi(argv[counter+1])>0) && (atoi(argv[counter+1])<=0xffff))                
                        used_port = atoi(argv[counter+1]);
            if (strcmp(argv[counter], "--keep-alive")==0)               
                keep_alive = true;
            if (strcmp(argv[counter], "--root_dir")==0) 
                // JUST IGNORE NON-EXISTING PARAMETERS
                if (counter+1<argc) sprintf(root_dir, "%s", argv[counter+1]);                                                      
            if (strcmp(argv[counter], "--chunked")==0) chunked_mode = true;  
            if (strcmp(argv[counter], "--loglevel")==0) 
                // JUST IGNORE NON-INTERGER VALUES OR NEXT OR NON-EXISTING PARAMETERS
                if (counter+1<argc) 
                    if (atoi(argv[counter+1])>0)                
                        loglevel_set = atoi(argv[counter+1]);
        }
    }
    // PRINT ACCEPTED PARAMETERS
    dbg_printf(INFO_LOGLEVEL, "BINARY: %s, USED_PORT: %d, CHUNKED_MODE: %s, ", argv[0], used_port, chunked_mode ? "true" : "false");
    dbg_printf(INFO_LOGLEVEL, "KEEP-ALIVE: %s, ROOT_DIR: %s, LOGLEVEL:%d\n",  keep_alive ? "true" : "false", root_dir, loglevel_set);


    // OPEN SOCKET
    int serverSocket = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in serverAddress;
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_port = htons(used_port);
    serverAddress.sin_addr.s_addr = htonl(INADDR_LOOPBACK);

    bind(serverSocket, (struct sockaddr *) &serverAddress, sizeof(serverAddress));

    int listening = listen(serverSocket, 10);
    if (listening < 0) {
        dbg_printf(ERROR_LOGLEVEL,"Error: The server is not listening.\n");
        return errno;
    }

    char httpResponse[512] = "HTTP/1.1 200 OK\r\n";
    char htmlFile[65000] = "";
    #define READ_BYTES 1000
    char line[READ_BYTES];
    FILE *file;
    char fname[256]; 
    
    strcat(fname, root_dir);
    strcat(fname, "index.html");

    if ((file = fopen(fname, "r"))){
        while (fgets(line, READ_BYTES, file) != 0) strcat(htmlFile, line);
        fclose(file);
        return 1;
    } else {
        strcpy(httpResponse, "HTTP/1.1 404 Not found\r\n");
        strcat(htmlFile, "<html><head><title>title</title></head><body>404 - file not found.</body></html>");
    }

    // CONSTRUCT HEADER FORMAT
    if (keep_alive) strcat(httpResponse, "Connection: keep-alive\r\n");
    if (chunked_mode) strcat(httpResponse, "Transfer-Encoding: chunked\r\n");
    strcat(httpResponse, "Content-Type: text/html\r\n\r\n");

    // CHUNKED MODE htmlFile ENCODING
    if (chunked_mode) {
        char chunked_msg[10000];
        print_chunk(htmlFile, chunked_msg);
        strcpy(htmlFile, chunked_msg);
    }

    // JOIN HTTP+HTML
    strcat(httpResponse, htmlFile);

    dbg_printf(INFO_LOGLEVEL, "HTML_FILE: %s\nFILE_CONTENT:\n%s\n",  fname, httpResponse);
    
    // Wait for a connection, create a connected socket if a connection is pending
    int clientSocket;
    while(1) {
        clientSocket = accept(serverSocket, NULL, NULL);
        send(clientSocket, httpResponse, sizeof(httpResponse), 0);
        close(clientSocket);
    }



    // PRINT ERROR IF OCCURS
    if (errno>0) perror("ERR:");
    return errno;
}