# git commond
* 查看已经配置分支关联信息
```bash
git branch -vv
cat .git/config
```
* 查看远程库详细信息
```bash
git remote -v
git remote show origin
```
* 添加远程库
```bash
git remote add origin https://github.com/teabookDep/pyexcel.git
git push -u origin master
(第一次推送因为远程仓库为空 要加 -u)
```
```bash
git remote rm name  # 删除远程仓库
git remote rename old_name new_name  # 修改仓库名
```
* 利用现有分支创建新分支
```bash
git checkout –b branch4 origin/branch2
```

* 把当前分支中未提交的修改移动到其他分支
```bash
git stash
git checkout branch2
git stash pop
```

* 删除远程分支
```bash
git push origin --delete <branchName>
```
* 查看远程分支
```bash
git branch -r
git ls-remote
```

* 删除远程tag
```bash
git push origin --delete tag <tagname>
```

* 重命名本地分支
```bash
git branch -m devel develop
```

* 看到分支的合并情况
```bash
git log --graph --pretty=oneline --abbrev-commit
```

* 当前目录所有修改的文件 从HEAD中签出并且把它恢复成未修改时的样子.
```bash
git checkout .
```

* 把hello.rb从HEAD中签出.
```bash
git checkout -- hello.rb
```
* 用户配置
```bash
git config --global user.name "teabook"
git config --global user.eamil "teabook@gmail.com"
```

* Git撤销git commit 但是未git push的修改
```bash
???
```


* git如何清除工作区所有还没有add的文件的修改
```bash
git checkout -- filename
git checkout .
```


* 先更新下本地的远程分支
```bash
git fetch origin
```
* 然后可以比对
```bash
git diff 本地分支 origin/xxxx
git diff HEAD FETCH_HEAD
```


* 在使用git时，push到远端后发现commit了多余的文件，或者希望能够回退到以前的版本。
先在本地回退到相应的版本：
```bash
git reset --hard <版本号>
// 注意使用 --hard 参数会抛弃当前工作区的修改
// 使用 --soft 参数的话会回退到之前的版本，但是保留当前工作区的修改，可以重新提交
```

如果此时使用命令：
```bash
git push origin <分支名>
```
会提示本地的版本落后于远端的版本；
为了覆盖掉远端的版本信息，使远端的仓库也回退到相应的版本，需要加上参数--force
```bash
git push origin <分支名> --force

git remote add dkremote https://github.com/teabookDep/docker-spark.git

https://github.com/teabookDep/docker-spark.git


git reset --mixed HEAD 将你当前的改动从缓存区中移除，但是这些改动还留在工作目录中。
另一方面，如果你想完全舍弃你没有提交的改动，你可以使用
git reset --hard HEAD。这是 git reset 最常用的两种用法。

git reset --hard HEAD~1

git clone https://github.com/apache/spark.git
```


* 查看全部log
```bash
git reflog
```
* log
```bash
git log --after="2014-7-1" --before="2014-7-4"
git log –since=2.weeks

git log --after="yesterday"
git blame file_name

git log --since=10.hour
```

* 通常合并分支时，git一般使用”Fast forward”模式，在这种模式下，删除分支后，会丢掉分支信息，现在我们来使用带参数 –no-ff来禁用”Fast forward”模式
```bash
git merge –no-ff -m “注释” dev
```


* 使用命令 git stash list来查看stash 的工作区
```bash
git stash pop,恢复stash内容
```
