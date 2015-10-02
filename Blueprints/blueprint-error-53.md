{{{
  "title": "Blueprint Exit code: 53 Error Message",
  "date": "9-2-2015",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}

### Symptom

Blueprint packages that end with an error on each execution with the following error message:

```
[Error] Exit code: 53
```

### Cause

This is caused when an **Execution Mode** mismatch occurs between the package itself and the operating system
the package is being executed on.


### Resolution

Change the `Execution/Mode` setting in the problem `package.manifest` file.

```
<Execution>
  <Mode>Command</Mode>
  <RebootOnSuccess>false</RebootOnSuccess>
  <Command>install.sh</Command>
  <Persistent>false</Persistent>
</Execution>
```

* **Linux** based operating systems but have a mode of **Ssh**
* **Windows** based operating systems but have a mode of **Command** or **PowerShell**


