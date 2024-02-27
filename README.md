# Python_exercises


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