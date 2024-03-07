# Assignment: Git

## Rebase, Squash - Normal Merge

### Normal merge 

All the commits from the feature branch are merged onto the main branch (the branch, one wants the merge to be applied to). It carries over all the commit history from the feature branch to the main branch.

```
feature branch:
         -C4-C5-
        /       \
C1-C2-C3         -C6
main-branch:
```
The above highlights the feature branch (C4-C5) merging with the main branch in commit 6 (C6).  

One should use a merge when one wants to update a branch, which has been shared with others.

### Squash merge 

In squash merge, all the commits from the feature branch are made into a single commit, that is merged onto the main branch. The main branch will have one commit that represents all the commits that were made. In a `git squash merge`, the merge does not carry over the commit history of the feature branch to the main branch. 

```
feature branch:
            - C4 - C5
           /   \  /
C1 - C2 - C3    C6
main-branch:
```
The above highlights the feature branch (C4-C5) merges with the main branch in a single commit (C6) with no history.

One should use this squash merge when one wants to merge with the master branch and one does not require the history of all the commits.

### Rebase merge
In rebase, all the comits from the feature branch are added individally onto the base branch. All the hashes in the commit will be recaultated. It basically go back intime and redos these commits with a new hash that represents the commit made. This helps to get ride of any dummy commits. It may lead to merge conflicts if someone tries already cloned your branch and then tries to merge to your rebased branch. This is due to the changed hashes.

```
C1 - C2 - C3 - C4 - C5
branch:
```

One should use this on a branch that one would like to update. One should make sure that this branch has not been shared or cloned.

## what are forks, why are they used ?

Forks are a operation that copys a repository where changes can be made without affecting the original respository. In forks there exsits a connection between the original respository and the forked repository. Forks are used so that one does not make changes to the original repository, which could break the project or not comply with the rules. This will become tedious and hard for the coder to go back and revert these changes in a big project.

## git rebase -i
The `i` stands for interactive. It looks at the root commit and one by one applies the following commits.The diffrence between a interactive rebase and normal rebase is that, a normal rebase does this automatically where as in rebase interactive - one is able to edit each commit. One is able to edit an old commit message, delete a old commit, combine multiple commits (sqaush them), reorder commits, make fixes to old commits, reopen commits for editing. 

One should only use this technique when the branch has not been shared with anyone, in order to prevent future merge conflicts.
