# morpheus-docs
This is the document repository for [Morpheus Data](https://www.morpheusdata.com "Morpheus Homepage").  All content is automatically published to the [Morpheus Docs Site](https://docs.morpheusdata.com "Morpheus Docs").

The content of these docs is open source.  This means you are free to contribute to them by issuing pull requests from a fork.

## Contributing
The standard flow for contributing to a project such as this is to fork the repo & clone locally, create an upstream remote and sync your local copy before you branch, branch for each separate piece of work, do work including writing good commit messages, push to your origin repo, create a new PR in GitHub, and respond to any code review feedback.

### Step 1: Fork
Firstly you need a local fork of the the project, so go ahead and press the “fork” button in GitHub. This will create a copy of the repository in your own GitHub account and you’ll see a note that it’s been forked underneath the project name:
![alt text](https://github.com/tadamhicks/morpheus-docs/tree/master/images/forked.png "Forked Project")

Now you need a copy locally, so find the “SSH clone URL” in the right hand column and use that to clone locally using a terminal:
```
$ git@github.com:tadamhicks/morpheus-docs.git
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




