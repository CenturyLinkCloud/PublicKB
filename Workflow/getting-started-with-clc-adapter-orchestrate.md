{{{
  "title": "Getting Started with the CLC Orchestrate Adapter",
  "date": "07-15-2015",
  "author": "Benjamin Harristhal",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

We developed the Orchestrate Adapter to allow developers to take advantage of Orchestrate as their Database Service and yet continue to leverage the power of Spring Data within their services and solution.

The Orchestrate Adapter implements the standard Spring Data interfaces so that using the Orchestrate Adapter is exactly like using any other Spring Data Adapter.  This also allows for an easy change from a backend your project might be using now, like Mongo, to use Orchestrate by simply updating your Spring configuration.

The Adapter provides the basic find, find all, and other out of the box queries you would expect to have.  The adapter also supports the ability to define your own custom queries as needed.  

We also added some additional features that can be utilized via annotations in your service implementations.  One of the most popular features we added was the ability to encrypt/decrypt data at the attribute level by simply applying the @Encrypted annotation to the variable declaration.

You don’t need to be an expert in Spring Data to start using the Orchestrate Adapter either.  If you’re using Spring Boot then it’s just a couple of annotations and you are plugging into Orchestrate.  If you are using Spring Core then there are just a couple of additional annotations (or configuration lines – depending on your style) to add.

Please see the [README](https://github.com/CenturyLinkCloud/clc-adapter-orchestrate) for more information on using this adapter in your code.
