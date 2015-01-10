# CenturyLink Cloud CLI and Python SDK

This repository contains a *Python SDK* and a command line interface *CLI* (based on the SDK) to interact with the *[CenturyLink Cloud](http://www.centurylinkcloud.com)* API.  At present this aligns most closely to [V1](https://t3n.zendesk.com/categories/20012068-API-v1-0) of the CenturyLink Cloud API though efforts are in process to merge [V2](https://t3n.zendesk.com/categories/20067994-API-v2-0-Beta-) API as it nears full release.

## Contents

* [Installing](#installing)
* [Python APIV1 SDK Programming Guide](README_PYTHON_APIV2_SDK.md)
* [Python APIV2 SDK Programming Guide](README_PYTHON_APIV1_SDK.md)
* [SDK API Reference](http://centurylinkcloud.github.io/clc-python-sdk/doc/clc.html)
* [CLI](README_CLI.md)


## Installing

### Via Python's pip
Cross-platform installation is available via pypi.  Requires *Python 2.7* - this is not currently compatible with Python 3.
If you have pip already installed the following command will get you running:
```
> pip install clc-sdk
```

This should automatically install the following dependencies used by the CLI: prettytable, clint, argparse, requests

If you do not have pip (the Python package manager) installed a quickstart install of this prereq on Linux/Mac is:
```
> curl https://bootstrap.pypa.io/get-pip.py | sudo python
```

### Windows pre-package executable
The CLI is available as a prepackaged single-file Windows executable and the most recent compiled version is always available [here](https://github.com/CenturyLinkCloud/clc-python-sdk/raw/master/src/dist/clc-cli.exe).
Note also that all examples below will need to be modified since the Windows command line executable is *clc-cli* (to eliminate conflict with the a 
standard installed PS commandlet.


