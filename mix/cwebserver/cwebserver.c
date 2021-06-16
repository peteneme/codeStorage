#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

#define DEFAULT_PORT "80"
#define STRING_LEN    10

int main(int argc,char* argv[])
{
    int counter;
    char used_port_string[STRING_LEN] = DEFAULT_PORT;
    char arg_value[STRING_LEN];
    int used_port = atoi(DEFAULT_PORT);

    //printf("Program Name Is: %s\n", argv[0]);
    if(argc>1)
    {
        for(counter=0; counter<argc; counter++)
        {
            sprintf(arg_value, "%s", argv[counter]);

            if (strcmp(arg_value, "--port")==0) 
            {
                counter++;
                char tmp_port[STRING_LEN];
                sprintf(tmp_port, "%s", argv[counter]);
                // JUST IGNORE NON-INTERGER VALUES
                if ((strcmp(tmp_port, "(null)")!=0) && (atoi(tmp_port)>0) && (atoi(tmp_port)<=0xffff))
                { 
                    sprintf(used_port_string, "%s", argv[counter]);
                    used_port = atoi(used_port_string);
                }    
            };

            
        }
        
    }

    printf("USED_PORT: %d\n", used_port);


    // PRINT ERROR IF OCCURS
    if (errno>0) perror("ERR:");
    return 0;
}