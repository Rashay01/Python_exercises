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
C1 - C2 - C3  -  C6
main-branch:
```
The above highlights the feature branch (C4-C5) which merges with the main branch, in a single commit (C6) with no history (C4 and C5).

One should use this squash merge when one wants to merge with the master branch and one does not require the history of all the commits.

### Rebase merge
In rebase merge, all the comits from the feature branch are added individually onto the base branch. All the hashes in the commit will be recalculated. It basically goes back in time and redoes these commits with a new hash which represents the commit made. This helps to get rid of any dummy commits. This may lead to merge conflicts, if the branch was already cloned/forked and an attempt is made to merge to the rebased branch. This occurs due to the changed hashes.

```
C1 - C2 - C3 - C4 - C5
branch:
```

One should use rebase merge on a branch one would like to update. One should ensure that this branch has not already been shared or cloned.

## what are forks, why are they used ?

A Fork is an operations that copies an existing repository where changes may be made without affecting the original respository. In forks there exsits a connection between the original respository and the forked repository (cpoied repository). Forks prevent changes to the original repository. Changes could break the project or not comply with the rules of the original repository. If one is able to change the oringinal repository  it will become tedious and difficult to go back and reverse these changes. It can be a new repository that has a connection to the existing repository. 

## git rebase -i
The `i` stands for interactive. `git rebase -i` takes the the root commit and thereafter sequentially applies all the commits that follow.The diffrence between a interactive rebase and a normal rebase is that, the normal rebase automatically redoes all the commits whereas in rebase interactive - one is able to edit each individual commit. Git interactive rebase allows one to change individual commits, squash commits together, delete commits or reorder the commits. This allows one to clean up their Git commit history, to make it linear and meaningfuf. This may make it easier to understand the history of the respository. 

One should only use this technique when the branch has not been shared, in order to prevent future merge conflicts.