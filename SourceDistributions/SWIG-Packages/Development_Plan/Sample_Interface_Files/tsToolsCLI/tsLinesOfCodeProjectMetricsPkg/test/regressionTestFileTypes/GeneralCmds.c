/***********************************************************************
# Time-stamp: <07/05/2001  4:21:35 PM rick>
#
# File    : bdsh.c
#
# Purpose : The general commands source file for the BirdDog cshell.
#
# Notes   : None
#
# History : Initially from a public domain shell
#
# Date       Author    Description
#
# 07/05/2001 TeamSTARS Added this file header
#                      Added function headers for all functions.
#                      Changed include bdsh.h to bdcshell.h
#                      Changed all bdsh to bdcsh.
#                      Changed all non-prefixed functions to use
#                        bdcsh_.
#
#***********************************************************************/

#include "bdcshell.h"

#include <sys/types.h>
#include <sys/stat.h>
#include <signal.h>
#include <utime.h>
#include <errno.h>

bdcsh_CMDTABType GeneralCmdtab[] =
{
  {"alias",   "[name [command]]", bdcsh_DoAlias,        1, MAXARGS},
  {"cd",      "[dirname]",	  bdcsh_DoCd,           1, 2},
  {"echo",    "[args] ...",	  bdcsh_DoEcho,         1, MAXARGS},
  {"exec",    "filename [args]",  bdcsh_DoExec,         2, MAXARGS},
  {"exit",    "",		  bdcsh_DoExit,         1, 1},
  {"help",    "[command]",	  bdcsh_DoHelp,         1, 2},
  {"kill",    "[-sig] pid ...",	  bdcsh_DoKill,         2, MAXARGS},
  {"prompt",  "string",		  bdcsh_DoPrompt,       2, MAXARGS},
  {"pwd",     "",		  bdcsh_DoPwd,          1, 1},
  {"quit",    "",		  bdcsh_DoExit,         1, 1},
  {"setenv",  "name value",	  bdcsh_DoSetenv,       3, 3},
  {".",	      "filename",	  bdcsh_DoSource,       2, 2},
  {"unalias", "name",		  bdcsh_DoUnalias,      2, 2},
  {"where",   "program",	  bdcsh_DoWhere,        2, 2},
  {(char *) 0, (char *) 0,	  0,	               0, 0}
};

/***********************************************************************
#
# Routine  : bdcsh_DoEcho
#
# Purpose  : Echo command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
# Author   : TeamSTARS
#
# Notes    : None.
#
#***********************************************************************/
void
bdcsh_DoEcho(bdcsh_TheApplicationTypePtrType aPtr, int argc, const char **argv)
{
  BOOL	first;

  first = TRUE;

  while (argc-- > 1) {
    if (!first)
      fputc(' ', stdout);

    first = FALSE;
    fputs(*++argv, stdout);
  }

  fputc('\n', stdout);
}

/***********************************************************************
#
# Routine  : bdcsh_DoHelp
#
# Purpose  : Help command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
# Author   : TeamSTARS
#
# Notes    : None.
#
#***********************************************************************/
void
bdcsh_DoHelp(bdcsh_TheApplicationTypePtrType aPtr, int argc, const char **argv)
{
  bdcsh_CMDTABTypePtrType cPtr;
  BOOL found;
  int index;

  for (index = 0, found = FALSE;
       (index < bdcsh_CommandTableCount);
       index++) {
    for (cPtr = aPtr->CmdTabPtrArray[index];
	 cPtr->name != (char *) 0;
	 cPtr++) {
      // Should we show it?
      if ((argc == 1) ||
	  ((argc == 2) && (strcmp(argv[1], cPtr->name) == 0))) {
	// Yes
	printf("  %10s\t%s\n", cPtr->name, cPtr->usage);
	found = TRUE;
	// Was a command specified?
	if (argc == 2) {
	  // Yes
	  break;
	}
      }
    }
  }
  // Did we find anything?
  if (!found) {
    // No
    sprintf(aPtr->buffer, "Unknown command: %s\n", argv[1]);
    bdcsh_ShowUser(aPtr, aPtr->buffer);
  }
}

/***********************************************************************
#
# Routine  : bdcsh_DoPwd
#
# Purpose  : Pwd command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
# Author   : TeamSTARS
#
# Notes    : None.
#
#***********************************************************************/
void
bdcsh_DoPwd(bdcsh_TheApplicationTypePtrType aPtr, int argc, const char **argv)
{
  char	buf[PATHLEN];

  if (getcwd(buf, PATHLEN) == NULL) {
    sprintf(aPtr->buffer, "Cannot get current directory\n");
    bdcsh_ShowUser(aPtr, aPtr->buffer);
    return;
  }

  printf("  %s\n", buf);
}

/***********************************************************************
#
# Routine  : bdcsh_DoCd
#
# Purpose  : Cd command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
# Author   : TeamSTARS
#
# Notes    : None.
#
#***********************************************************************/
void
bdcsh_DoCd(bdcsh_TheApplicationTypePtrType aPtr, int argc, const char **argv)
{
  const char *path;

  if (argc > 1)
    path = argv[1];
  else {
    path = getenv("HOME");

    if (path == NULL) {
      bdcsh_ShowUser(aPtr, "No HOME environment variable\n");
      return;
    }
  }

  if (chdir(path) < 0)
    perror(path);
}

/***********************************************************************
#
# Routine  : bdcsh_DoExit
#
# Purpose  : Exit command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
# Author   : TeamSTARS
#
# Notes    : None.
#
#***********************************************************************/
void
bdcsh_DoExit(bdcsh_TheApplicationTypePtrType aPtr, int argc, const char **argv)
{
  exit(0);
}

/***********************************************************************
#
# Routine  : bdcsh_DoSetenv
#
# Purpose  : Setenv command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
# Author   : TeamSTARS
#
# Notes    : None.
#
#***********************************************************************/
void
bdcsh_DoSetenv(bdcsh_TheApplicationTypePtrType aPtr, int argc, const char **argv)
{
  const char *name;
  const char *value;
  char *str;

  name = argv[1];
  value = argv[2];

  /*
   * The value given to putenv must remain around, so we must malloc it.
   * Note: memory is not reclaimed if the same variable is redefined.
   */
  str = malloc(strlen(name) + strlen(value) + 2);

  if (str == NULL) {
    bdcsh_ShowUser(aPtr, "Cannot allocate memory\n");
    return;
  }

  strcpy(str, name);
  strcat(str, "=");
  strcat(str, value);

  putenv(str);
}

/***********************************************************************
#
# Routine  : bdcsh_DoUmask
#
# Purpose  : Umask command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
# Author   : TeamSTARS
#
# Notes    : None.
#
#***********************************************************************/
void
bdcsh_DoUmask(bdcsh_TheApplicationTypePtrType aPtr, int argc, const char **argv)
{
  const char *cp;
  int mask;

  if (argc <= 1) {
    mask = umask(0);
    umask(mask);
    printf("  %03o\n", mask);
    return;
  }

  mask = 0;
  cp = argv[1];

  while (isoctal(*cp))
    mask = mask * 8 + *cp++ - '0';

  if (*cp || (mask & ~0777)) {
    bdcsh_ShowUser(aPtr, "Bad umask value\n");
    return;
  }

  umask(mask);
}

/***********************************************************************
#
# Routine  : bdcsh_DoKill
#
# Purpose  : Kill command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
# Author   : TeamSTARS
#
# Notes    : None.
#
#***********************************************************************/
void
bdcsh_DoKill(bdcsh_TheApplicationTypePtrType aPtr, int argc, const char **argv)
{
  const char *cp;
  int  	sig;
  int  	pid;

  sig = SIGTERM;

  if (argv[1][0] == '-') {
    cp = &argv[1][1];

    if (strcmp(cp, "HUP") == 0)
      sig = SIGHUP;
    else if (strcmp(cp, "INT") == 0)
      sig = SIGINT;
    else if (strcmp(cp, "QUIT") == 0)
      sig = SIGQUIT;
    else if (strcmp(cp, "KILL") == 0)
      sig = SIGKILL;
    else {
      sig = 0;

      while (isdecimal(*cp))
	sig = sig * 10 + *cp++ - '0';

      if (*cp) {
	bdcsh_ShowUser(aPtr, "Unknown signal\n");
	return;
      }
    }

    argc--;
    argv++;
  }

  while (argc-- > 1) {
    cp = *++argv;
    pid = 0;

    while (isdecimal(*cp))
      pid = pid * 10 + *cp++ - '0';

    if (*cp) {
      bdcsh_ShowUser(aPtr, "Non-numeric pid\n");
      return;
    }

    if (kill(pid, sig) < 0)
      perror(*argv);
  }
}

/***********************************************************************
#
# Routine  : bdcsh_DoWhere
#
# Purpose  : Where command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
# Author   : TeamSTARS
#
# Notes    : None.
#
#***********************************************************************/
void
bdcsh_DoWhere(bdcsh_TheApplicationTypePtrType aPtr, int argc, const char **argv)
{
  const char *program;
  const char *dirName;
  char *path;
  char *endPath;
  char *fullPath;
  BOOL	found;

  found = FALSE;
  program = argv[1];

  if (strchr(program, '/') != NULL) {
	bdcsh_ShowUser(aPtr, "Program name cannot include a path\n");
    return;
  }

  path = getenv("PATH");
 
  fullPath = bdcsh_GetChunk(aPtr, strlen(path) + strlen(program) + 2);
  path = bdcsh_ChunkStrDup(aPtr, path);

  if ((path == NULL) || (fullPath == NULL)) {
    bdcsh_ShowUser(aPtr, "Memory allocation failed\n");
    return;
  }

  /*
   * Check out each path to see if the program exists and is
   * executable in that path.
   */
  for (; path; path = endPath) {
    /*
     * Find the end of the next path and NULL terminate
     * it if necessary.
     */
    endPath = strchr(path, ':');

    if (endPath)
      *endPath++ = '\0';

    /*
     * Get the directory name, defaulting it to DOT if
     * it is null.
     */
    dirName = path;

    if (dirName == '\0')
      dirName = ".";

    /*
     * Construct the full path of the program.
     */
    strcpy(fullPath, dirName);
    strcat(fullPath, "/");
    strcat(fullPath, program);

    /*
     * See if the program exists and is executable.
     */
    if (access(fullPath, X_OK) < 0) {
      if (errno != ENOENT)
	printf("  %s: %s\n", fullPath, strerror(errno));
      continue;
    }

    printf("  %s\n", fullPath);
    found = TRUE;
  }

  if (!found)
    printf("  Program \"%s\" not found in PATH\n", program);
}

/***********************************************************************
#
# Routine  : bdcsh_DoUnalias
#
# Purpose  : Unalias command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
# Author   : TeamSTARS
#
# Notes    : None.
#
#***********************************************************************/
void
bdcsh_DoUnalias(bdcsh_TheApplicationTypePtrType aPtr,
	       int argc, const char **argv)
{
  bdcsh_ALIASType *alias;

  while (--argc > 0) {
    alias = bdcsh_FindAlias(aPtr, *++argv);

    if (alias == NULL)
      continue;

    free(alias->name);
    free(alias->value);
    aPtr->aliascount--;
    alias->name = aPtr->aliastable[aPtr->aliascount].name;
    alias->value = aPtr->aliastable[aPtr->aliascount].value;	
  }
}

/***********************************************************************
#
# Routine  : bdcsh_DoPrompt
#
# Purpose  : Prompt command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
# Author   : TeamSTARS
#
# Notes    : None.
#
#***********************************************************************/
void
bdcsh_DoPrompt(bdcsh_TheApplicationTypePtrType aPtr, int argc, const char **argv)
{
  char *cp;
  char	buf[CMDLEN];

  if (!bdcsh_MakeString(aPtr, argc - 1, argv + 1, buf, CMDLEN))
    return;
 
  cp = malloc(strlen(buf) + 2);

  if (cp == NULL) {
    bdcsh_ShowUser(aPtr, "4 Out of memory, 0:1\n");
    return;
  }

  strcpy(cp, buf);
  strcat(cp, " ");

  if (aPtr->prompt)
    free(aPtr->prompt);

  aPtr->prompt = cp;
}

/***********************************************************************
#
# Routine  : bdcsh_DoSource
#
# Purpose  : Source command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
# Author   : TeamSTARS
#
# Notes    : None.
#
#***********************************************************************/
void
bdcsh_DoSource(bdcsh_TheApplicationTypePtrType aPtr, int argc, const char **argv)
{
  bdcsh_ReadFile(aPtr, (char *) argv[1]);
}

/***********************************************************************
#
# Routine  : bdcsh_DoExec
#
# Purpose  : Exec command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
# Author   : TeamSTARS
#
# Notes    : None.
#
#***********************************************************************/
void
bdcsh_DoExec(bdcsh_TheApplicationTypePtrType aPtr, int argc, const char **argv)
{
  const char *name;

  name = argv[1];

  if (access(name, 4)) {
    perror(name);
    return;
  }

  while (--aPtr->sourcecount >= 0) {
    if (aPtr->sourcefiles[aPtr->sourcecount] != stdin)
      fclose(aPtr->sourcefiles[aPtr->sourcecount]);
  }

  argv[argc] = NULL;

  execv(name, (char **) argv + 1);
  exit(1);
}

/***********************************************************************
#
# Routine  : bdcsh_DoAlias
#
# Purpose  : Alias command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
# Author   : TeamSTARS
#
# Notes    : None.
#
#***********************************************************************/
void
bdcsh_DoAlias(bdcsh_TheApplicationTypePtrType aPtr, int argc, const char **argv)
{
  const char *name;
  char *value;
  bdcsh_ALIASType *alias;
  int	count;
  char	buf[CMDLEN];

  if (argc < 2) {
    count = aPtr->aliascount;

    for (alias = aPtr->aliastable; count-- > 0; alias++)
      printf("  %s\t%s\n", alias->name, alias->value);
    return;
  }

  name = argv[1];

  if (argc == 2) {
    alias = bdcsh_FindAlias(aPtr, name);

    if (alias)
      printf("  %s\n", alias->value);
    else {
      sprintf(aPtr->buffer, "Alias \"%s\" is not defined\n", name);
      bdcsh_ShowUser(aPtr, aPtr->buffer);
    }

    return;	
  }

  if (strcmp(name, "alias") == 0) {
    bdcsh_ShowUser(aPtr, "Cannot alias \"alias\"\n");
    return;
  }

  if (!bdcsh_MakeString(aPtr, argc - 2, argv + 2, buf, CMDLEN))
    return;

  value = malloc(strlen(buf) + 1);

  if (value == NULL) {
    bdcsh_ShowUser(aPtr, "No memory for alias value\n");
    return;
  }

  strcpy(value, buf);

  alias = bdcsh_FindAlias(aPtr, name);

  if (alias) {
    free(alias->value);
    alias->value = value;
    return;
  }

  if ((aPtr->aliascount % ALIASALLOC) == 0) {
    count = aPtr->aliascount + ALIASALLOC;

    if (aPtr->aliastable)
      alias = (bdcsh_ALIASType *) realloc(aPtr->aliastable,
				sizeof(bdcsh_ALIASType *) * count);
    else
      alias = (bdcsh_ALIASType *) malloc(sizeof(bdcsh_ALIASType *) * count);
 
    if (alias == NULL) {
      free(value);
      bdcsh_ShowUser(aPtr, "No memory for alias table\n");
      return;
    }

    aPtr->aliastable = alias;
  }

  alias = &aPtr->aliastable[aPtr->aliascount];

  alias->name = malloc(strlen(name) + 1);

  if (alias->name == NULL) {
    free(value);
    bdcsh_ShowUser(aPtr, "No memory for alias name\n");
    return;
  }

  strcpy(alias->name, name);
  alias->value = value;
  aPtr->aliascount++;
}

/* END CODE */
