Alm Lab Website
===============

http://almlab.mit.edu/

Notes on how to add new member content are in the github wiki.

Pushing to this repo automatically updates the website. You can also "run" this by visiting
[http://almlab.mit.edu/make.php](http://almlab.mit.edu/make.php).

How to update
-------------

Updating the website follows this workflow:   

* you edit the webpage on your own computer,
    * navigate to the `web_scripts` folder and run `make` to build a local version of the website
    * look at it in your browser to make sure it looks good, etc.
* git commit those changes
* git push your changes to the repo
* and then, automagically\*, github.com will visit make.php, which will cause athena to run "git pull" and "make"
    * if almlab.mit.edu hasn't updated in a few seconds, then you can visit almlab.mit.edu/make.php and see the error log and troubleshoot from there
    * if you visit almlab.mit.edu and don't see your updates, try force-reloading the page (press Shift while clicking the refresh button)

\*`github.com` is set up to ping `make.php` with Codeship (which you can get to from [here](https://github.com/almlab/www/settings/installations)),
but a [webhook](https://github.com/almlab/www/settings/hooks) can probably do the same thing and would probably be an easier way to do it...
Could be worth investigating.

Accessing the website on Athena
-------------------------------

The website is on Athena, at `/afs/athena.mit.edu/org/a/almlab/`.
(To log in to Athena, `ssh your_kerberos@athena.dialup.mit.edu`)

Members of the `almlab-www` [Moira group](groups.mit.edu/webmoira/) have read and write
permissions (learn more about permissions on Athena [here](https://sipb.mit.edu/doc/afs-and-you/)).

Communicating back and forth to/from Athena and this repo probably involves changing the `git config`
`user.name` to match your GitHub username. You also probably need an [ssh key](https://help.github.com/articles/error-permission-denied-publickey/).
