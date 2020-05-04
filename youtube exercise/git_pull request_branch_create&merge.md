how to create branch and create a pull request and merge to master?

once you clone repo in your local machine, then
```
git checkout  #make sure you are in master

git branch bname #create branch

git checkout bname #go to branch
```
editing your file
```
git status #what did you modified

git diff #optional, to see the difference with previous file

git add . (or git add -A) # both means add new changes

git commit -m 'comment what you did'

git push
```
then go to bit bucket, create pull request for your reviewer

once your branch code looks good, then
```
git checkout master

git pull # catch all updates

git merge

git push
```
