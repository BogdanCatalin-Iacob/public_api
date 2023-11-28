# Public API

## Description
This app displays the date, time, and a random message on home page.
On api/random page will display a random number between 0 and a user set limit, and a user text.
This app is live on [Pythonanywhere](MisterBogdan.pythonanywhere.com) for 3 months, ending in Feb 2024.

## Project Creation

This project was developed using a [VS Code](https://code.visualstudio.com/). The code was committed to [Git](https://git-scm.com) and pushed to [GitHub](https://github.com) using the terminal.

The project was started by navigating to [GitHub](https://github.com) and creating a new repository by clicking `New` button. Under 'Repository name' I input 'public_api' and then clicked 'Create repository'.

I opened VS Code and initialized directory 'public_api': 
```
git init
git add README.md
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/BogdanCatalin-Iacob/public_api.git
git push -u origin main
```
The following commands were used throughout the project:
* `git status` - This command was used to see the modified files before adding them to staging area
* `git add` - This command was used to add files to the staging area before commiting.
* `git commit` -m *commit message explaining teh updates* - This command was used to commit changes to the local repository.
* `git push` - This command was used to push all commited changes to the GitHub repository.

## Technologies
-   Python
-   Flask