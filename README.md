# morpheus-docs
This is the document repository for [Morpheus Data](https://www.morpheusdata.com "Morpheus Homepage").  All content is automatically published to the [Morpheus Docs Site](https://docs.morpheusdata.com "Morpheus Docs").

The content of these docs is open source.  This means you are free to contribute to them by issuing pull requests from a fork.

## Contributing
The standard flow for contributing to a project such as this is to fork the repo & clone locally, create an upstream remote and sync your local copy before you branch, branch for each separate piece of work, do work including writing good commit messages, push to your origin repo, create a new PR in GitHub, and respond to any code review feedback.

### Step 1: Fork
Firstly you need a local fork of the the project, so go ahead and press the “fork” button in GitHub. This will create a copy of the repository in your own GitHub account and you’ll see a note that it’s been forked underneath the project name:
![alt text](/images/forked.png?raw=true "Forked Project")

Now you need a copy locally, so find the “SSH clone URL” in the right hand column and use that to clone locally using a terminal:
```
$ git clone git@github.com:tadamhicks/morpheus-docs.git
```

Change into the new project’s directory:
```
$ cd morpheus-docs
```

Finally, in this stage, you need to set up a new remote that points to the original project so that you can grab any changes and bring them into your local copy. Firstly clock on the link to the original repository – it’s labeled “Forked from” at the top of the GitHub page. This takes you back to the projects main GitHub page, so you can find the “SSH clone URL” and use it to create the new remote, which we’ll call upstream.
```
$ git remote add upstream git@github.com:gomorpheus/morpheus-docs.git
```

You now have two remotes for this project on disk:

    1. origin which points to your GitHub fork of the project. You can read and write to this remote.
    2. upstream which points to the main project’s GitHub repository. You can only read from this remote.

### Step 2: Do some work
This is the fun bit where you get to contribute to the project. It’s usually best to start by fixing a bug that is either annoying you or you’ve found on the project’s issue tracker.
#### BRANCH!
**The number one rule is to put each piece of work on its own branch.** The general rule is that if you are bug fixing, then branch from master and if you are adding a new feature then branch from develop. If the project only has a master branch, the branch from that.

For this example, we’ll assume we’re fixing a bug in morpheus-docs, so we branch from master:
```
$ git checkout master
$ git pull upstream master && git push origin master
$ git checkout -b hotfix/readme-update
```

Firstly we ensure we’re on the master branch. Then the git pull command will sync our local copy with the upstream project and the git push syncs it to our forked GitHub project. Finally we create our new branch. You can name your branch whatever you like, but it helps for it to be meaningful. Including the issue number is usually helpful.

Now you can do your work.

**Ensure that you only fix the thing you’re working on. Do not be tempted to fix some other things that you see along the way, including formatting issues, as your PR will probably be rejected.**

Make sure that you commit in logical blocks. Each commit message should be sane. Read Tim Pope’s [A Note About Git Commit Messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html "A Note About Git Commit Messages").

### Step 3: Create the PR
To create a PR you need to push your branch to the origin remote and then press some buttons on GitHub.

To push a new branch:
```
$ git push -u origin hotfix/readme-update
```

This will create the branch on your GitHub project. The -u flag links this branch with the remote one, so that in the future, you can simply type git push origin.

Swap back to the browser and navigate to your fork of the project (https://github.com/tadamhicks/morpheus-docs in my case) and you’ll see that your new branch is listed at the top with a handy “Compare & pull request” button:
![alt text](/images/pullrequest.png?raw=true "Pull Request")

Go ahead and press the button!

On this page, ensure that the “base fork” points to the correct repository and branch. Then ensure that you provide a good, succinct title for your pull request and explain why you have created it in the description box. Add any relevant issue numbers if you have them.
![alt text](/images/prconfirm.png?raw=true "Pull Request Confirmation")

If you scroll down a bit, you’ll see a diff of your changes. **Double check that it contains what you expect.**

Once you are happy, press the “Create pull request” button and you’re done.

### Step 4: Review by the maintainers
For your work to be integrated into the project, the maintainers will review your work and either request changes or merge it.

