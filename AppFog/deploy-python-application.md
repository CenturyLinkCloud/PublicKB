{{{
  "title": "Deploying a Python Application",
  "date": "03-07-2016",
  "author": "Derek Jansen",
  "attachments": [
  {
    "file_name": "Python Django Sample",
    "url": "../attachments/af-python-django-sample.zip",
    "type": "application/zip"
  }],
  "related-products" : [],
  "contentIsHTML": false
}}}

<strong>The AppFog service will be retired as of June 29, 2018. Beginning on this date, the AppFog Platform-as-a-Service will no longer be available, including all source code, env vars, and database information.</strong>

### Audience
Application Developers

#### Overview
AppFog includes the Cloud Foundry [Python buildpack](https://github.com/cloudfoundry/python-buildpack) by default. This enables the deployment of [Python](https://www.python.org/) applications using any one of multiple runtime versions. To learn more, please read the Cloud Foundry Python buildpack [README](https://github.com/cloudfoundry/python-buildpack/blob/master/README.md).

This article is going to focus on deploying a sample Python application. It uses the popular [Django](https://www.djangoproject.com/) framework for creating web applications in Python.

### Pre-Requisites
#### Installing Python
To develop using Python you must have the its [runtime interpreter](https://wiki.python.org/moin/BeginnersGuide/Download) installed. You should choose a version supported in the buildpack's [releases page](https://github.com/cloudfoundry/python-buildpack/releases).

You will also need [Pip](https://pip.pypa.io/en/stable/installing/) installed in your development environment.

#### Downloading Simple Example Application
The sample app used in this article is attached at the bottom of this article.

#### Running the Sample App Locally
After downloading the sample app locally you must install the required Python modules.
```
$ unzip af-python-django-sample.zip
$ cd django_sample
$ pip install -r requirements.txt
```

Once all of the dependent libraries are downloaded and installed, you will need to make **manage.py** executable and apply migrations. Then you can start the app.
```
$ chmod +x manage.py
$ ./manage.py migrate
$ ./manage.py runserver
```

This will start the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### Deploying to AppFog
#### Vendor your dependencies and create *Procfile*.
```
$ mkdir vendor
$ pip install -d vendor -r requirements.txt
$ echo 'web: ./manage.py collectstatic --noinput && \
./manage.py migrate && \
gunicorn django_sample.wsgi' > Procfile
```

#### It is recommended to create *.cfignore* to exclude files/directories you would not want pushed to production.
```
$ echo -e '*.pyc\n*.dbsqlite3\n*.[oa]\n*.swp\nbackups/' > .cfignore
```
Alternatively, you can simply create a shortcut if you already have **.gitignore**.
```
$ ln -s .gitignore .cfignore
```

#### You should also specify the version of Python you want to use in *runtime.txt*.
```
$ echo 'python-2.7.11' > runtime.txt
```

#### Now you can push your app to the platform.
You are ready to deploy the app using the [Cloud Foundry CLI](login-using-cf-cli.md). Once it is running, copy the value from `urls` and go to that address in a browser. You should see a page that says 'Hello'.
* The example below returns django-sample.useast.appfog.ctl.io as the URL. Your app's address will depend on its region and either its name or the route you provide.

```
$ cf push django-sample
Using manifest file /home/derek/code/django_sample/manifest.yml

Updating app django-sample in org Derek / space Dev as Derek...
OK

Uploading django-sample...
Uploading app files from: /home/derek/code/django_sample
Uploading 41.9K, 19 files
Done uploading               
OK

Stopping app django-sample in org Derek / space Dev as Derek...
OK

Starting app django-sample in org Derek / space Dev as Derek...
-----> Downloaded app package (6.8M)
-----> Downloaded app buildpack cache (35M)
-------> Buildpack version 1.5.4
-----> Installing dependencies with pip
       Ignoring indexes: https://pypi.python.org/simple
-----> Preparing static assets
       Running collectstatic...
       61 static files copied to '/home/vcap/app/staticfiles'.

-----> Uploading droplet (42M)

1 of 1 instances running

App started


OK

App django-sample was started using this command `python manage.py collectstatic --noinput && python manage.py migrate && gunicorn django_sample.wsgi`

Showing health and status for app django-sample in org Derek / space Dev as Derek...
OK

requested state: started
instances: 1/1
usage: 512M x 1 instances
urls: django-sample.useast.appfog.ctl.io
last uploaded: Mon Mar 7 22:50:37 UTC 2016
stack: cflinuxfs2
buildpack: python 1.5.4

     state     since                    cpu    memory           disk           details   
#0   running   2016-03-07 04:51:14 PM   0.0%   103.1M of 512M   161.8M of 1G
```

### Python Version Support

The Python buildpack [releases page](https://github.com/cloudfoundry/python-buildpack/releases) outlines the supported versions. We recommend using the most recent one for applications deployed to AppFog.
