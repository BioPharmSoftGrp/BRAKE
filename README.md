# BRAKE - Biopharm R pAcKge Explorer

## Desired Functionality

### Create User Account - Public

- Create account – public
- Usual process for login, username and password
- Do we need a terms of use? If so does someone have a generic one
- Request ownership of a package added by an admin ( V2 )
- Reset password (V2)
- List of packages they own
- Profile update (eg email address)

### User Account – Private
- List of functionalities for a user once they create an account and
  are logged it
- Request ownership of a package added by an admin ( V2 )
- Reset password (V2)
- Edit package details of packages they own
- Add others as co-owners so they can also edit package details (V2)

### Add a new package - Public
Anyone can add a new package
- Added by someone with an account 
  - They are listed as the “owner” if that package so they can come
    back and edit, update modify ect
- Added by someone without an account
  - By default the admins of BRAKE own it and can modify as we get
    request, but make every effort to have the package developers take
    ownership so they can modify
- Admins of BRAKE can always edit/modify package
- Before a package is displayed for the public it is first reviewed by
  someone
- Once it is reviewed it appears on the public page
- List of packages they own
- Profile update (eg email address)
- Subscribe to update about particular package (V2)
- Get notified of new packages (V2)

### Main Website (Public)
- List all packages in the database
- Search packages by name or keyword 
- Search by category
- Search by Author (V2)

### Package Details
This section lists the information and details about what we will
collect for each package.

Information listed on CRAN: Description, Version, R Depends,
Published, Author, Maintainer, URL, CRAN Link, GitHub Link, other links
(used for things like GitLab), reference materials (allowed to be
links), Vignettes, screen shots, list to training (eg on our YouTube
channel) , link to shiny app version (see
https://gsdesign.shinyapps.io/prod/ for example)

### Other information
- Package category: How would the owner classify: Trial design, trial
  simulation, trial monitoring, visualization, tools.
- Packages can choose more than one category.
- Do we need other categories, such as: safety monitoring?
- Do we need a sub-category such as Trial Design -> Dose finding,
  Trial Design -> Platform trials, randomized trials?

## Setup Dev Environment

To setup a development environment for BRAKE:

0. Install django
   
   ```
   $ pip install django
   ```
   
1. Initialize the sqlite3 database
   
   ```
   $ ./cd BRAKEProject
   $ python manage.py makemigrations
   $ python manage.py migrate
   ```
   
   This will a create `db.sqlite3` file in the
   [BRAKEProject](BRAKEProject) folder.
   
2. Create a `.local_settings.py` file with the following contents:
   
   ```python
   # Development Settings
   # IMPORTANT: Remove when merging into master.
   
   DEBUG = True
   ALLOWED_HOSTS = ['127.0.0.1']
   ```
   
   This file is sourced by
   [settings.py](BRAKEProject/BRAKE/settings.py), and will let django
   allow your browser's connection.

