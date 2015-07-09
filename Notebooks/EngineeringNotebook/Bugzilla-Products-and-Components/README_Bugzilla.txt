#-----------------------------------------------------------
#"Time-stamp: <05/17/2015  8:13:54 AM rsg>
#-----------------------------------------------------------

================ File: $README-Bugzilla.txt =================

   +----+----+  TeamSTARS "tsWxGTUI_PyVx" Toolkit
   | ts | Wx |      with Python-based
   +----+----+         Command Line Interface (CLI)
   | G T U I |      and "wxPython"-style, "Curses"-based
   +---------+         Graphical-Text User Interface (GUI)
 
   Get that cross-platform, pixel-mode "wxPython" feeling
   on character-mode color (xterm-family) & non-color
   (vt100-family) terminals.

   You can find this and other plain-text files in the
   Toolkit subdirectory named "./Documents/tsDocGUI/
          Bugzilla Product and Component Recommendation".

===================== TABLE OF CONTENTS ====================

1. Installing Bugzilla

2. Configuring Bugzilla Database

   2.1 Bugzilla Database
   2.2 TeamSTARS "tsWxGTUI_PyVx" Toolkit Products
   2.3 TeamSTARS "tsWxGTUI_PyVx" Toolkit Components

==================== INSTALLING BUGZILLA ===================

1. Installing Bugzilla

   See Bugzilla topic in:

       "./Documents/$GETTING_STARTED.txt"

=============== CONFIGURING BUGZILLA DATABASE ==============

2. Configuring Bugzilla Database

   2.1 Bugzilla Database

       Bugzilla supports the following administrator database
       configuration and software troubleshooter bug reports
       and bug tracking:

       a) Parameters --- Set core parameters of the install-
          ation. That's the place where you specify the URL to
          access this installation, determine how users authen-
          ticate, choose which bug fields to display, select
          the mail transfer agent to send email notifications,
          choose which group of users can use charts and share
          queries, and much more.

       b) Default Preferences --- Set the default user prefer-
          ences. These are the values which will be used by
          default for all users. Users will be able to edit
          their own preferences from the Preferences.

       c) Sanity Check --- Run sanity checks to locate problems
          in your database. This may take several tens of min-
          utes depending on the size of your installation. You
          can also automate this check by running sanitycheck.pl
          from a cron job. A notification will be sent per email
          to the specified user if errors are detected.

       d) Users --- Create new user accounts or edit existing
          ones. You can also add and remove users from groups
          (also known as "user privileges").

       e) Classifications --- If your installation has to
          manage many products at once, it's a good idea to
          group these products into distinct categories. This
          lets users find information more easily when doing
          searches or when filing new bugs.

       f) Products --- Edit all aspects of products, includ-
          ing group restrictions which let you define who can
          access bugs being in these products. You can also
          edit some specific attributes of products such as
          components, versions and milestones directly.

          NOTE:

              The TeamSTARS "tsWxGTUI_PyVx" Toolkit auth-
              or(s) use the Product and Component names
              and descriptions detailed in:

                  "./Documents/tsDocGUI/
                     Bugzilla-Products-and-Components"

              f1) "Bugzilla-Products.doc" --- File created
                  by copying Bugzilla names and descriptions
                  from Product and Component screens into a
                  Microsoft Word document.

              f2) "Bugzilla-Products.txt" --- File created
                  by converting file f1 Tables to Tab separ-
                  ated text and saving as plain text.

              f3) "Bugzilla-Products.xls" --- File created
                  by opening file f2 with Microsoft Excel
		  1997-2003; creating additional worksheets;
		  cutting component sections from original
		  worksheet; pasting each cut section on to
		  the appropriate component worksheet; and
                  saving as Microsoft Excel xlsx worksheet.

              f4) "Bugzilla-Products.xlss" --- File created
                  by opening file f3 with Microsoft Excel
		  2007-2013; and saving asMicrosoft Excel
		  2007-2013 spreadsheet.

              f5) "Bugzilla-Products.ods" --- File created
                  by opening file f4 with LibraOffice 4.4
                  Calc; and saving as LibraOffice 4.4 Calc
		  ODS spreadsheet.

       g) Flags --- A flag is a custom 4-states attribute of
          bugs and/or attachments. These states are: granted,
          denied, requested and undefined. You can set as many
          flags as desired per bug, and define which users are
          allowed to edit them.

       h) Custom Fields --- Bugzilla lets you define fields
          which are not implemented by default, based on your
          local and specific requirements. These fields can
          then be used as any other field, meaning that you
          can set them in bugs and run any search involving
          them.

          Before creating new fields, keep in mind that too
          many fields may make the user interface more complex
          and harder to use. Be sure you have investigated
          other ways to satisfy your needs before doing this.

       i) Field Values --- Define legal values for fields
          whose values must belong to some given list. This
          is also the place where you define legal values
          for some types of custom fields.

       j) Bug Status Workflow --- Customize your workflow
          and choose initial bug statuses available on bug
          creation and allowed bug status transitions when
          editing existing bugs.

       k) Groups --- Define groups which will be used in the
          installation. They can either be used to define new
          user privileges or to restrict the access to some bugs.

       l) Keywords --- Set keywords to be used with bugs. Key-
          words are an easy way to "tag" bugs to let you find
          them more easily later.

       m) Whining --- Set queries which will be run at some
          specified date and time, and get the result of these
          queries directly per email. This is a good way to
          create reminders and to keep track of the ac

   2.2 TeamSTARS "tsWxGTUI_PyVx" Toolkit Products

       Individual source code and document directories are
       the only products to be registered with Bugzilla.

       The TeamSTARS "tsWxGTUI_PyVx" Toolkit software consists
       of the following:

       a) Numerous Python source code libraries, packages and
          any lower-level subdirectories.

          Products (Directories)

              ["Technical-Preview-0.0.0"]
                |
                +-- ["Developer-Sandbox"]
                |     |
                |     +-- ["tsWxGTUI_PyVx"]
                |           |
                |           +-- ["Documents"]
                |           |
                |           +-- ["Python-2x"]
                |           |
                |           +-- ["Python-3x"]
                |                 |
                |                 +-- ["tsWxGTUI_Py3x"]
                |                       |
                |                       +-- ["tsDemoArchive"]
                |                       +-- ["tsLibCLI"]
                |                       +-- ["tsLibGUI"]
                |                       +-- ["tsTestsLibCLI"]
                |                       +-- ["tsTestsLibGUI"]
                |                       +-- ["tsTestsToolsCLI"]
                |                       +-- ["tsTestsToolsGUI"]
                |                       +-- ["tsTestsToolsLibCLI"]
                |                       +-- ["tsTestsToolsLibGUI"]
                |                       +-- ["tsToolsCLI"]
                |                       +-- ["tsToolsGUI"]
                |                       +-- ["tsToolsLibCLI"]
                |                       +-- ["tsToolsLibGUI"]
                |                       +-- ["tsUtilities"]
                |
                +-- ["Site-Package"]
                      |
                      +-- ["tsWxGTUI_PyVx"]
                            |
                            +-- ["Documents"]
                            +-- ["ManPages"]
                            +-- ["Notebooks"]
                            |
                            +-- ["Python-2x"]
                            |
                            +-- ["Python-3x"]
                                  |
                                  +-- ["tsWxGTUI_Py3x"]
                                        |
                                        +-- ["Documents"]
                                        +-- ["tsDemoArchive"]
                                        |     |
                                        |     +-- ["tsTestsLibCLI"]
                                        |     +-- ["tsTestsLibGUI"]
                                        |     +-- ["tsTestsToolsCLI"]
                                        |     +-- ["tsTestsToolsGUI"]
                                        |     +-- ["tsTestsToolsLibCLI"]
                                        |     +-- ["tsTestsToolsLibGUI"]
                                        |
                                        +-- ["tsLibCLI"]
                                        +-- ["tsLibGUI"]
                                        +-- ["tsToolsCLI"]
                                        +-- ["tsToolsGUI"]
                                        +-- ["tsToolsLibCLI"]
                                        +-- ["tsToolsLibGUI"]
                                        +-- ["tsUtilities"]

          Components (Files)

       b) Numerous plain text and application-specific docu-
          ments with multiple fonts and graphic images.

       c) Numerous bug filings, comments and status changes:

          unconfirmed ->

          confirmed ->

          in-progress -> 

          resolved (fixed, duplicate,
                    wontfix, worksforme,
                    invalid) ->

          verified.

   2.3 TeamSTARS "tsWxGTUI_PyVx" Toolkit Components

       Individual source code and document files are the only
       components to be registered with Bugzilla.

       The TeamSTARS "tsWxGTUI_PyVx" Toolkit software consists
       of the following:

       a) Numerous Python modules with one or more classes,
          methods, functions, data declarations, shell
          scripts and distribution build scripts.

   2.3 Bugzilla Troubleshooter Bug Filing and Searching

       Bugzilla supports the following software trouble-
       shooter bug filing and bug tracking:

======================= End-Of-File ========================
