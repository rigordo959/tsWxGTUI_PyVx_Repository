/***********************************************************************
#
# File    : GeneralCmds.c
#
# Purpose : The general commands source file for the cshell.
#
# Notes   : None
#
# History : Initially from a public domain shell
#
#***********************************************************************/

#include "GeneralCmds.h"

#include <sys/types.h>
#include <sys/stat.h>
#include <signal.h>
#include <utime.h>
#include <errno.h>

GeneralCmds_CMDTABType GeneralCmdtab[] =
{
  {"alias",   "[name [command]]", GeneralCmds_DoAlias,        1, MAXARGS},
  {"cd",      "[dirname]",        GeneralCmds_DoCd,           1, 2},
  {"echo",    "[args] ...",       GeneralCmds_DoEcho,         1, MAXARGS},
  {"exec",    "filename [args]",  GeneralCmds_DoExec,         2, MAXARGS},
  {"exit",    "",                 GeneralCmds_DoExit,         1, 1},
  {"help",    "[command]",        GeneralCmds_DoHelp,         1, 2},
  {"kill",    "[-sig] pid ...",   GeneralCmds_DoKill,         2, MAXARGS},
  {"prompt",  "string",           GeneralCmds_DoPrompt,       2, MAXARGS},
  {"pwd",     "",                 GeneralCmds_DoPwd,          1, 1},
  {"quit",    "",                 GeneralCmds_DoExit,         1, 1},
  {"setenv",  "name value",       GeneralCmds_DoSetenv,       3, 3},
  {".",       "filename",         GeneralCmds_DoSource,       2, 2},
  {"unalias", "name",             GeneralCmds_DoUnalias,      2, 2},
  {"where",   "program",          GeneralCmds_DoWhere,        2, 2},
  {(char *) 0, (char *) 0,        0,                   0, 0}
};

/***********************************************************************
#
# Routine  : GeneralCmds_DoEcho
#
# Purpose  : Echo command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
#***********************************************************************/
void
GeneralCmds_DoEcho(GeneralCmds_TheApplicationTypePtrType aPtr,
                   int argc, const char **argv)
{
  BOOL  first;

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
# Routine  : GeneralCmds_DoHelp
#
# Purpose  : Help command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
#***********************************************************************/
void
GeneralCmds_DoHelp(GeneralCmds_TheApplicationTypePtrType aPtr,
                   int argc, const char **argv)
{
  GeneralCmds_CMDTABTypePtrType cPtr;
  BOOL found;
  int index;

  for (index = 0, found = FALSE;
       (index < GeneralCmds_CommandTableCount);
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
    GeneralCmds_ShowUser(aPtr, aPtr->buffer);
  }
}

/***********************************************************************
#
# Routine  : GeneralCmds_DoPwd
#
# Purpose  : Pwd command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
#***********************************************************************/
void
GeneralCmds_DoPwd(GeneralCmds_TheApplicationTypePtrType aPtr,
                  int argc, const char **argv)
{
  char  buf[PATHLEN];

  if (getcwd(buf, PATHLEN) == NULL) {
    sprintf(aPtr->buffer, "Cannot get current directory\n");
    GeneralCmds_ShowUser(aPtr, aPtr->buffer);
    return;
  }

  printf("  %s\n", buf);
}

/***********************************************************************
#
# Routine  : GeneralCmds_DoCd
#
# Purpose  : Cd command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
#***********************************************************************/
void
GeneralCmds_DoCd(GeneralCmds_TheApplicationTypePtrType aPtr,
                 int argc, const char **argv)
{
  const char *path;

  if (argc > 1)
    path = argv[1];
  else {
    path = getenv("HOME");

    if (path == NULL) {
      GeneralCmds_ShowUser(aPtr, "No HOME environment variable\n");
      return;
    }
  }

  if (chdir(path) < 0)
    perror(path);
}

/***********************************************************************
#
# Routine  : GeneralCmds_DoExit
#
# Purpose  : Exit command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
#***********************************************************************/
void
GeneralCmds_DoExit(GeneralCmds_TheApplicationTypePtrType aPtr,
                   int argc, const char **argv)
{
  exit(0);
}

/***********************************************************************
#
# Routine  : GeneralCmds_DoSetenv
#
# Purpose  : Setenv command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
#***********************************************************************/
void
GeneralCmds_DoSetenv(GeneralCmds_TheApplicationTypePtrType aPtr,
                     int argc, const char **argv)
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
    GeneralCmds_ShowUser(aPtr, "Cannot allocate memory\n");
    return;
  }

  strcpy(str, name);
  strcat(str, "=");
  strcat(str, value);

  putenv(str);
}

/***********************************************************************
#
# Routine  : GeneralCmds_DoUmask
#
# Purpose  : Umask command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
#***********************************************************************/
void
GeneralCmds_DoUmask(GeneralCmds_TheApplicationTypePtrType aPtr,
                    int argc, const char **argv)
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
    GeneralCmds_ShowUser(aPtr, "Bad umask value\n");
    return;
  }

  umask(mask);
}

/***********************************************************************
#
# Routine  : GeneralCmds_DoKill
#
# Purpose  : Kill command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
#***********************************************************************/
void
GeneralCmds_DoKill(GeneralCmds_TheApplicationTypePtrType aPtr,
                   int argc, const char **argv)
{
  const char *cp;
  int   sig;
  int   pid;

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
        GeneralCmds_ShowUser(aPtr, "Unknown signal\n");
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
      GeneralCmds_ShowUser(aPtr, "Non-numeric pid\n");
      return;
    }

    if (kill(pid, sig) < 0)
      perror(*argv);
  }
}

/***********************************************************************
#
# Routine  : GeneralCmds_DoWhere
#
# Purpose  : Where command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
#***********************************************************************/
void
GeneralCmds_DoWhere(GeneralCmds_TheApplicationTypePtrType aPtr,
                    int argc, const char **argv)
{
  const char *program;
  const char *dirName;
  char *path;
  char *endPath;
  char *fullPath;
  BOOL  found;

  found = FALSE;
  program = argv[1];

  if (strchr(program, '/') != NULL) {
        GeneralCmds_ShowUser(aPtr, "Program name cannot include a path\n");
    return;
  }

  path = getenv("PATH");
 
  fullPath = GeneralCmds_GetChunk(aPtr, strlen(path) + strlen(program) + 2);
  path = GeneralCmds_ChunkStrDup(aPtr, path);

  if ((path == NULL) || (fullPath == NULL)) {
    GeneralCmds_ShowUser(aPtr, "Memory allocation failed\n");
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
# Routine  : GeneralCmds_DoUnalias
#
# Purpose  : Unalias command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
#***********************************************************************/
void
GeneralCmds_DoUnalias(GeneralCmds_TheApplicationTypePtrType aPtr,
                      int argc, const char **argv)
{
  GeneralCmds_ALIASType *alias;

  while (--argc > 0) {
    alias = GeneralCmds_FindAlias(aPtr, *++argv);

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
# Routine  : GeneralCmds_DoPrompt
#
# Purpose  : Prompt command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
#***********************************************************************/
void
GeneralCmds_DoPrompt(GeneralCmds_TheApplicationTypePtrType aPtr,
                     int argc, const char **argv)
{
  char *cp;
  char  buf[CMDLEN];

  if (!GeneralCmds_MakeString(aPtr, argc - 1, argv + 1, buf, CMDLEN))
    return;
 
  cp = malloc(strlen(buf) + 2);

  if (cp == NULL) {
    GeneralCmds_ShowUser(aPtr, "4 Out of memory, 0:1\n");
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
# Routine  : GeneralCmds_DoSource
#
# Purpose  : Source command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
#***********************************************************************/
void
GeneralCmds_DoSource(GeneralCmds_TheApplicationTypePtrType aPtr,
                     int argc, const char **argv)
{
  GeneralCmds_ReadFile(aPtr, (char *) argv[1]);
}

/***********************************************************************
#
# Routine  : GeneralCmds_DoExec
#
# Purpose  : Exec command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
#***********************************************************************/
void
GeneralCmds_DoExec(GeneralCmds_TheApplicationTypePtrType aPtr,
                   int argc, const char **argv)
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
# Routine  : GeneralCmds_DoAlias
#
# Purpose  : Alias command.
#
# Parameter: INPUT        aPtr  Application structure pointer
#            INPUT        argc  Argument count
#            INPUT        argv  Vector of pointers to arguments
#
# Returns  : Nothing
#
#***********************************************************************/
void
GeneralCmds_DoAlias(GeneralCmds_TheApplicationTypePtrType aPtr,
                    int argc, const char **argv)
{
  const char *name;
  char *value;
  GeneralCmds_ALIASType *alias;
  int   count;
  char  buf[CMDLEN];

  if (argc < 2) {
    count = aPtr->aliascount;

    for (alias = aPtr->aliastable; count-- > 0; alias++)
      printf("  %s\t%s\n", alias->name, alias->value);
    return;
  }

  name = argv[1];

  if (argc == 2) {
    alias = GeneralCmds_FindAlias(aPtr, name);

    if (alias)
      printf("  %s\n", alias->value);
    else {
      sprintf(aPtr->buffer, "Alias \"%s\" is not defined\n", name);
      GeneralCmds_ShowUser(aPtr, aPtr->buffer);
    }

    return;     
  }

  if (strcmp(name, "alias") == 0) {
    GeneralCmds_ShowUser(aPtr, "Cannot alias \"alias\"\n");
    return;
  }

  if (!GeneralCmds_MakeString(aPtr, argc - 2, argv + 2, buf, CMDLEN))
    return;

  value = malloc(strlen(buf) + 1);

  if (value == NULL) {
    GeneralCmds_ShowUser(aPtr, "No memory for alias value\n");
    return;
  }

  strcpy(value, buf);

  alias = GeneralCmds_FindAlias(aPtr, name);

  if (alias) {
    free(alias->value);
    alias->value = value;
    return;
  }

  if ((aPtr->aliascount % ALIASALLOC) == 0) {
    count = aPtr->aliascount + ALIASALLOC;

    if (aPtr->aliastable)
      alias = (GeneralCmds_ALIASType *) realloc(aPtr->aliastable,
                                sizeof(GeneralCmds_ALIASType *) * count);
    else
      alias = (GeneralCmds_ALIASType *) malloc(sizeof(GeneralCmds_ALIASType *) * count);
 
    if (alias == NULL) {
      free(value);
      GeneralCmds_ShowUser(aPtr, "No memory for alias table\n");
      return;
    }

    aPtr->aliastable = alias;
  }

  alias = &aPtr->aliastable[aPtr->aliascount];

  alias->name = malloc(strlen(name) + 1);

  if (alias->name == NULL) {
    free(value);
    GeneralCmds_ShowUser(aPtr, "No memory for alias name\n");
    return;
  }

  strcpy(alias->name, name);
  alias->value = value;
  aPtr->aliascount++;
}

/* END CODE */
