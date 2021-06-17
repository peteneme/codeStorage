#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <stdbool.h>


// DEFINITIONS ----------------------------------------------------------------
#define DEFAULT_PORT  80
#define STRING_LEN    10

// FUNCTION DECLARATIONS ------------------------------------------------------
void help_text(void);



// FUNCTION DEFINITIONS -------------------------------------------------------
void help_text(void) {
    printf("Input CLI parameters:\n");
    printf("--help               - Print help\n");
    printf("--port NUMBER        - Webserver PORT NUMBER\n");
    printf("--keep-alive SECONDS - Switch on keep-alive by inserting NUMBER of seconds\n");
    printf("--root_dir DIRECTORY - Set webserver root directory, by default is ./ \n");
    printf("--chunked            - Switch on http1.1 chunked mode, by default is off\n");
}


// MAIN ***********************************************************************
int main(int argc, char* argv[])
{
    int used_port     = DEFAULT_PORT;
    int keep_alive    = 0;
    bool chunked_mode = false;
    char root_dir[256] = "./";


    // CLI PARAMETERS PARSING
    if(argc>1) {
        int counter;
        for(counter=0; counter<argc; counter++) {
            if (strcmp(argv[counter], "--help")==0) { help_text(); return errno; };
            if (strcmp(argv[counter], "--port")==0) 
                // JUST IGNORE NON-INTERGER VALUES OR NEXT OR NON-EXISTING PARAMETERS
                if ((strcmp(argv[counter+1], "(null)")!=0) && (atoi(argv[counter+1])>0) && (atoi(argv[counter+1])<=0xffff))                
                    used_port = atoi(argv[counter+1]);
            if (strcmp(argv[counter], "--keep-alive")==0) 
                // JUST IGNORE NON-INTERGER VALUES OR NEXT OR NON-EXISTING PARAMETERS
                if ((strcmp(argv[counter+1], "(null)")!=0) && (atoi(argv[counter+1])>0))                
                    keep_alive = atoi(argv[counter+1]);
            if (strcmp(argv[counter], "--root_dir")==0) 
                // JUST IGNORE NON-EXISTING PARAMETERS
                if ((strcmp(argv[counter+1], "(null)")!=0)) sprintf(root_dir, "%s", argv[counter+1]);                                                      
            if (strcmp(argv[counter], "--chunked")==0) chunked_mode = true;  
        }
    }


    // PRINT ACCEPTED PARAMETERS
    printf("BINARY: %s, USED_PORT: %d, CHUNKED_MODE: %s, ", argv[0], used_port, chunked_mode ? "true" : "false");
    printf("KEEP-ALIVE: %d, ROOT_DIR: %s\n",  keep_alive, root_dir);

    // PRINT ERROR IF OCCURS
    if (errno>0) perror("ERR:");
    return errno;
}