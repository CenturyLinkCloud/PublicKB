{{{
  "title": "How We Use Github To Build AppFog",
  "date": "1-31-2013",
  "author": "Originally Posted On AppFog",
  "attachments": [],
  "contentIsHTML": false
}}}

Joining [AppFog](http://www.ctl.io/appfog) back in February became my first time working for a company using [Github](https://github.com/) [private repositories](https://github.com/pricing) for source control. My previous gig used [Bitbucket](https://bitbucket.org/) and [Mercurial](https://mercurial.selenic.com/), which we migrated to from self-hosted [SVN](http://subversion.apache.org/), which we migrated to from [SourceGear Vault](http://www.sourcegear.com/vault/), which we migrated to from [Visual Source Safe](https://msdn.microsoft.com/en-us/library/3h0544kx(v=vs.80).aspx)… etc. That’s how things go at a 12-year-old company, I guess. As a startup, AppFog can start off on the right foot and just use Github from the get-go. Yippee!

I have used git and Github for a while in open source projects and know the typical workflow of forking and submitting pull requests. AppFog’s workflow is very similar. Here’s how we approach it.

Setting Up Your Personal Fork

The [AppFog organization](https://github.com/appfog) has a number of projects in it. Everyone in the organization has commit access and can create/destroy/modify any of the repositories. We could just clone the repository down, edit the code, commit and push to master…but there’s a better way.

Our approach is for each developer to create a fork of the project they want to work on.

For example, suppose we have a repository in the AppFog org called af-python-django. I’d head on over to the project page at [https://github.com/appfog/af-python-django](https://github.com/appfog/af-python-django) and click the Fork button near the top of the page.

Once the “hardcore forking action” is over, I now have my own personal fork at https://github.com/thoward/af-python-django. I can clone that to my dev machine:

<pre><code>git clone git@github.com:thoward/af-python-django</code></pre>

One thing you’d notice there is that git clone adds the origin automatically. That’s great and all, but doesn’t do much for me. I need an easy way to pull upstream changes into my personal fork from the main repository. To do that, I’ll hop into that directory and add the upstream remote:

<pre><code>
git remote add upstream git@github.com:appfog/af-python-django
git fetch upstream
</code></pre>

That’s the basic setup.

##Modifying The Code

Now that I’ve got my personal fork configured, I can do whatever I’d like to it without disturbing our pristine shared repository… but to keep things organized and clear, I’m not just going to start tweaking bits and committing to master. Instead, I’ll work entirely on topic branches, regardless of how small or large a change is.

The following steps detail how to create a branch, update the code, push changes to the remote, and bring these changes to the attention of the person responsible for merging pull requests.

First, I’ll bring the master up to date using that upstream remote I created.
<pre><code>
#switch to master
git checkout master</code></pre>


<pre><code>#pull in latest code
git pull upstream master</code></pre>

This will pull all recently-merged changes from the main appfog/af-python-django repository into my personal fork. Next, I’ll create the branch that I’m going to work on. The naming of the branches takes a special structured form.

###Branch Names

We break down the work we do into four distinct types of tasks: bugs, features, chores and hotfixes.

A bug is a normal bug fix of existing functionality.

A feature is new functionality.

A chore is something that adds business value, but doesn’t qualify as a feature (e.g. refactoring).

A hotfix is when we need to fix an immediate problem on a server (if you’re using hotfixes, you’re probably doing something wrong).

The branch name itself consists of the branch type, a brief underscore-separated description, and an optional Github Issue number. They are in the format of: <code>type/a_brief_description_#</code>.

Suppose I wanted to fix a bug where shared users aren’t able to login to the site. After creating the Github Issue, I would name the branch bug/shared_users_cant_login_123 where 123 is the issue number.

###Creating the Topic Branch

To create the branch, run git checkout -b <branch name>, where <branch name> is the type/description/id name we just described. For example, using our hypothetical bug fix task from before, I’d run:

<pre><code>git checkout -b bug/shared_users_cant_login_123</code></pre>

Once I’ve created the branch using the checkout command, follow the normal process of changing code, add/commit, and wrap it up with:

<pre><code>git push origin HEAD</code></pre>

After that, use the GitHub web interface to select the branch from the Current Branch dropdown and issue a Pull Request back to the original project.

So, start to finish, here are the steps to get some work done…

####STEPS TO WORK ON THE BRANCH
1) Checkout master: <code>git checkout master</code>

2) Pull in updates: <code>git fetch upstream</code>

3) Merge updates into master: <code>git merge upstream/master</code>

4) Create the branch: <code>git checkout -b bug/branch_description_123</code>

5) Make the code changes

6) Stage changes for commit: <code>git add <changed filenames></code>

7) Commit changes: <code>git commit -m "This is a descriptive commit message"</code>

8) Push changes to my personal fork: <code>git push origin HEAD</code>

9) From GitHub, select the branch from the Current Branch dropdown and issue a Pull Request

###Pull Request Guidelines

There are some basic guidelines around creating pull-requests.

**JUST SAY NO TO AUTO-MERGE**

Don’t auto-merge the pull request through Github’s interface. Ever.

**EXPLAIN THE PULL REQUEST**

Why is this pull request here? The branch name should be a brief description, but the pull-request itself should have a slightly more detailed description. Leave a nice, clear description about what the branch is for and why. Reference any issues if necessary. Github makes this super easy. You can just type something like #420 and it will auto-link the issue in.

**DON’T COMMIT GEMFILE.LOCK**

This one is Ruby-specific. If you didn’t make changes to Gemfile, don’t commit Gemfile.lock.

**CONFIG FILES**
This one is Rails specific, and is a bit of hyperbole, but relates to our process of using git. If the branch requires the creation of a new config file, say so in the description in big, bold text.

Also do the following:

1) Add the config file to .gitignore. We do not store our configs in source control.

2) Provide an example of your config file suitable for development purposes at config/myconfig.example.yml where myconfig is your config and yml can be any format.

We have a rake task configs:copy that can find those example config files and copy them to the normal names. This is handy when developing locally. On the production servers, the config files are managed separately from source code and are linked into the config directory from another location.

Here’s the <code>configs:copy</code> rake task:

<pre><code>
namespace :configs do
  desc "Copy config/*.example.yml files for development."
  task :copy do
    require 'fileutils'
    examples = Dir["config/*.example.*"]
    examples.each do |example|
      extname = File.extname(example)
      realbase = File.basename(example, ".example#{extname}")
      realpath = File.join("config", "#{realbase}#{extname}")
      unless File.exists?(realpath)
        FileUtils.cp(example, realpath)
        puts "copied #{example} => #{realpath}"
      end
    end
  end
end
</code></pre>

###Merging

Once the pull request is made, it is now the responsibility of the merge master to accept or reject the changes. Being the merge master is a rotating responsibility which involves looking over the pull requests, reviewing the code, and possibly asking the developer to make additional changes, add more unit test, etc.––this is our opportunity to discuss the changes in detail and introduce some standards and process for code quality.

When a pull-request is merged in, we’ll do that onto a special qa branch in the main repository. Here we can get all willy-nilly and try out the code, blow away the changes, or what have you. If everything looks good, then we merge from the change set in the qa branch that’s in a known-good state, finally, into the master branch on the main project. The qa branch is also the target that our continuous integration system watches, which, when updated kicks off our continuous delivery pipeline.

###Conclusion

At AppFog we make it a practice to continually review and improve our workflows when we’re working with GitHub (or any tools for that matter). We are always looking for ways to reduce complexity while still getting the same or even better results.

One of the things we’re currently considering is moving away from personal forks and instead just working with topic branches right in the main project. This should keep things just as organized but reduce the complexity of the process significantly. One radical member of our team suggests never using branches. So far, we smile and nod. He may convince us someday.

We’re also rethinking the merge master role, opting instead to distribute the responsibility for merging code across the team but with the axiom “never merge your own code”, ensuring that code review is baked into the process.

We’ll keep you posted!

**Additional Resources**

* [How Github Uses Github to Build Github](http://zachholman.com/talk/how-github-uses-github-to-build-github/)
* [Github’s Documentation on Pull Requests](https://help.github.com/articles/using-pull-requests/)
* [The Git Book](http://git-scm.com/book/en/v2)
