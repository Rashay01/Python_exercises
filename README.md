# Python_exercises

[Map to links](https://whimsical.com/python-data-types-classification-Q967VqqPXDmUW5QPjXgdK2)


# set up Git Notes

- click on code  and copy Https url
- delete file url and type cmd
- type git clone (url)
- Type this in the terminal to set up github
    - git config --global user.name "Github username"
    - git config --global user.email "Github email"


# Fails to clone repository
If it fails to clone: [link](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
In Gitbash: 
- ssh-keygen -t ed25519 -C "your_email@example.com"
- .> Enter file in which to save the key (/c/Users/YOU/.ssh/id_ALGORITHM):[Press enter]
- .> Enter passphrase (empty for no passphrase): [Type a passphrase]
- .> Enter same passphrase again: [Type passphrase again]

In setting on github website: 
- add a ssh key 

Repsoity one wants to clone:
- Now copy SSH link on the respository 

now in cmd in location:
- type git clone (url)

Alternative:
In gitbash:
- `cd` navigate to folder location
-  type `git clone` (enter url of repository)


Git Commands:

git init
git add .
git commit -m "This is my first project with git"
git add .
git commit -m "Created double function"
git log
git add .
git commit -m "Cool file with awesome msg"
git log
git checkout c7f9f09860
git checkout -
git log
git checkout 4b8be
git checkout c7f9
git checkout -
git checkout master

git log --help
git log -Sdouble -p


### git log -Smap -p
### git log -2 (top 2 commits)
### git log --graph (graph commits)

# Checkout to the master branch (old)
# Merge with dev branch (new) git merge dev

# Merge Conflict
# 1. Resolve
# 2. Stage
# 3. Commit