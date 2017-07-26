## 课前准备心得
### 总体心境变化：
作为文科生，编程是一个我一直很感兴趣但是不敢入手的领域。小学时曾经参加过市里的BASIC编程比赛，但是早就已经忘得精光，现在每天在excel的苦海里鏖战，但是效率之低令我无比沮丧。
接触到阳志平老师的文章之后，开始尝试着学习使用github，看过几个介绍视频之后，被Issue+pull request+branch的精妙设计所折服，加之阳志平老师不遗余力地讲解为何选择编程作为他的五大元科学，对编程的兴趣如烈火熊熊升起。恰巧发现开智有编程课，就毫不犹豫地预报名了。
在学习Learn Python The hard way的过程中，从一开始的懵懂，到刻意模仿作者程序，但又不停犯下简单错误，再到Google上到处翻阅资料了解bug出在何处，在不断的打怪升级之中，4天之内，自己就已经能够独立撰写一些简单的小程序了，让我倍感兴奋。
很期待接下来几个月的python课程，期待能够在几个月后脱胎换骨，把目前工作中的事情进行高度自动化，提升效率，更期待能够通过掌握程序员思维，更好地杠杆自己的成长。

### 学习过程复盘：
整体上，学习比较顺利，没有遇到特别大的困难
在学习中相对吃力的是：
1. Argv：在操作层面，自己很理解argv的使用方法，但是在意义层面，不太明白这个函数的用处。  =》 通过反复实操，理解了Argv可以通过一次操作，赋值多个变量。
2. 反向实操的过程中，发现自己原本以为很清楚的语法，完全写不出来    =》强逼自己一句一句写出来，然后test，再去与原文对比，在一次次的细节矫正之中，将语法和细节默化了；
3. 在模仿练习34制作自己的小游戏时，因为没有将代码写完，导致出现了多个未封闭的函数，导致报错，查询了许多网站都没有得到正解，最后在询问程序员朋友后，终于得到解决。
教训： 没有遵循书中的经验，每写一段就试着运行一次，确保没有问题之后再向下推进。
分析： 因为编写小游戏过程中，运用的都是def和raw_input函数，有很多重复性的内容，导致不耐烦。
改变： 小步快走、画小圈是保持持续稳步上升的好办法，每一步都坚定走“最小产品”+敏捷迭代的方法来推进。

### 如何学好：
1. 模仿 模仿 模仿：学习编程就像学习一门新的语言一样，孩子学习语言的方法只能是模仿嘴巴的动作，不断发声，不断根据外界反映校正，而不是扔给孩子一本语法书，“你照着学吧。”
2. 犯错 犯错 犯错：依然是学习语言的隐喻，小朋友一遍一遍学舌，比如终于说对“爸爸”之后，全家人的兴奋会给到ta一个正面激励，没说对就没有这个激励。所以多犯错，就能了解到知识的边界。

## 进阶任务：
### 心流：
心流状态多产生于 周末、家中、听音乐时
为了创建良好的，利于心流产生的环境，我需要做的事：
- 保持工作区域整洁、精简，避免杂物干扰注意力；
- 把手机放在另一个房间，以便高度专注地学习2小时；
- 将所需品（如 水、水果）等放在工作区域周边，随时可得
- 使用降噪耳机，隔绝外界噪音

### 教6个月前的自己使用Git：
其实我也不懂Git是什么。。。我尝试自学一下再教自己：

1. 利用官方文档和Wikipedia，了解SSH是什么，怎么用：https://help.github.com/articles/connecting-to-github-with-ssh/
* SSH最小定义：Secure Shell (SSH) is a cryptographic network protocol for operating network services securely over an unsecured network.[1] The best known example application is for remote login to computer systems by users.

* SSH的Github解释：Using the SSH protocol, you can connect and authenticate to remote servers and services. With SSH keys, you can connect to GitHub without supplying your username or password at each visit.

* 根据指引，新建SSH，连接SSH到github账户，修改密码增加安全性。

2. Git 是啥？  查阅官方术语词典：
Git is an open source program for tracking changes in text files. It was written by the author of the Linux operating system, and is the core technology that GitHub, the social and user interface, is built on top of.
明确了Git是一种分布式版本管理方法之后，在Github中搜索 “Git terminal edit”，紧跟问题。

3. 找到官方手册关于在本地运行Git的部分： 
https://help.github.com/articles/set-up-git/#setting-up-git

  1.安装Git：在google上找到git下载安装


  2. Git add/ commit/ push:  添加/ 修改/ 推送到云端
    Push file from local repository to on-line repository
    * https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/
      0. open terminal
      1. git init
      2. git add
      3. git commit -m "First commit"
      4. git remote add origin #remote repository site
      5. git remote -v
      6. git push -u origin master
 
  3. Git PULL: 在云端编辑完成后，利用git pull将修改的内容拉取到本地仓库。
      Fetch from and integrate with another repository or a local branch. Incorporates changes from a remote repository into the current branch. In its default mode, git pull is shorthand for git fetch followed by git merge FETCH_HEAD.
      * https://git-scm.com/docs/git-pull    * git pull [options] [<repository> [<refspec>…​]]
      * <repository> should be the name of a remote repository as passed to git-fetch[1]. <refspec> can name an arbitrary remote ref (for example, the name of a tag) or even a collection of refs with corresponding remote-tracking branches (e.g., refs/heads/*:refs/remotes/origin/*), but usually it is the name of a branch in the remote repository.
     
  4. Git Merge: 将Branch与master进行合并。
  具体用法研究中
  
  ...........................................
