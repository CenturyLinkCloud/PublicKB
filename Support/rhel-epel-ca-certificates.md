{{{
  "title": "RHEL 6, CA Certificates, and yum check-update",
  "date": "01-12-2017",
  "author": "Type-y McTyper",
  "attachments": [],
  "contentIsHTML": false
}}}


On RHEL 6, we've seen issues where `yum check-update` returns some errors, which might include something that looks like the following:

> https://mirrors.kernel.org/fedora-epel/6/x86_64/repodata/repomd.xml: [Errno -1] repomd.xml does not match metalink for epel
> Trying other mirror.


To correct the error, you can try to update 'ca-certificates' with the 'epel' repo disabled:

```sh
yum --disablerepo=epel update ca-certificates
```

And the go ahead and try `yum check-update` again.

