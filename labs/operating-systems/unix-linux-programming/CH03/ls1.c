/** ls1.c
 **   purpose  list contents of directory or directories
 **   action   if no args, use .  else list files in args
 **/
#include <dirent.h>
#include <stdio.h>
#include <sys/types.h>

void do_ls(char[]);

void main(int ac, char *av[]) {
  if (ac == 1)
      do_ls(".");
  else
      while (--ac) {
          printf("%s:\n", *++av);
          do_ls(*av);
      }
}

void do_ls(char dirname[])
/*
 *	list files in directory called dirname
 */
{
  DIR *dir_ptr;           /* the directory */
  struct dirent *direntp; /* each entry	 */

  if ((dir_ptr = opendir(dirname)) == NULL)
    fprintf(stderr, "ls1: cannot open %s\n", dirname);
  else {
    while ((direntp = readdir(dir_ptr)) != NULL)
      printf("%s\n", direntp->d_name);
    closedir(dir_ptr);
  }
}
