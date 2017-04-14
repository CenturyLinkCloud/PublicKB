{{{
  "title": "SafeHaven: Unlock Administrator Account",
  "date": "5-18-2016",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview:
Multiple incorrect login attempts through the SafeHaven console may lock out the administrator account. The following procedure can be used to unlock the account.

### Walkthrough:
1. SSH into CMS using the root account.

2. Kill the manager service by issuing the command: `killall -9 manager`. Verify that it is not running by either issuing it again or using `ps aux | grep manager`.

3. Move to the CMS directory with the following command: `cd /var/cms`

4. Open the "users" file in your preferred text editor: `vi users` (or `nano users`. Alternatively, Step 3 can be skipped and the file directly opened via path `vi /var/cms/users`).

5. The users file content should be similar to the following output:
   `Administrator   $5$jrawcgrsmfcrjjvw$vRopiZp2bzQ6NeTGMdMWIKcdxN9VTIymHi5joFELRQ8
4   ADMIN   WAVE    WAVE`

6. During normal operations, the users file should contain a "0". If it contains a "4" as above, the administrator account is locked. To unlocked it, edit the **4** value to **0** and save the file.

7. Restart the manager service by logging in through the console. You will be prompted to restart CMS services, if they are not running. This is best practice for starting CMS services. However, if for some reason you are unable to do so, you can run `/etc/rc.local`.

8. After you are prompted for the service start, you should be able to login successfully. If not, please contact the SafeHaven support team via customer care (help@ctl.io).
