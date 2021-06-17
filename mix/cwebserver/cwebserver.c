#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <stdbool.h>
#include <stdarg.h>


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



// FUNCTION DEFINITIONS -------------------------------------------------------
void help_text(void) {
    printf("Input CLI parameters:\n");
    printf("--help               - Print help\n");
    printf("--port NUMBER        - Webserver PORT NUMBER\n");
    printf("--keep-alive SECONDS - Switch on keep-alive by inserting NUMBER of seconds\n");
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

// MAIN ***********************************************************************
int main(int argc, char* argv[])
{
    int used_port     = DEFAULT_PORT;
    int keep_alive    = 0;
    bool chunked_mode = false;
    char root_dir[256] = "./";


    //dbg_printf("aaaa %s", "bbb\n");

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
                // JUST IGNORE NON-INTERGER VALUES OR NEXT OR NON-EXISTING PARAMETERS
                if (counter+1<argc) 
                    if (atoi(argv[counter+1])>0)                
                        keep_alive = atoi(argv[counter+1]);
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
    dbg_printf(INFO_LOGLEVEL, "KEEP-ALIVE: %d, ROOT_DIR: %s, LOGLEVEL:%d\n",  keep_alive, root_dir, loglevel_set);








    // PRINT ERROR IF OCCURS
    if (errno>0) perror("ERR:");
    return errno;
}