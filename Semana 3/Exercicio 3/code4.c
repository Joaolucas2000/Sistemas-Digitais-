#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int spawn(char* program, char** arg_list){
    pid_t child_pid;
    child_pid = fork();
    if(child_pid != 0)
        
        return child_pid;
    else{
        execvp(program, arg_list);        
fprintf(stderr, an error occurred in execvpn);
        abort();
    }
}
int main(){
   /*The argument list to pass to the ls command.*/
    char* arg_list[] = {
       ls, /*argv[0], the name of the program*/
       -l,
       /,
       
    };    
    /*Spawn a child process running the ls command.
    Ignore the returned child process ID.
    */
    spawn(ls, arg_list);
    printf(done with main programn);

    return 0;
} 
