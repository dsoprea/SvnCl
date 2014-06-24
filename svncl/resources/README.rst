------------
Introduction
------------

A tool to generate a changelog from the commits occurring after the last tag. 
This is intended to simplify creating tag commit-messages. Messages are 
generated starting from the oldest.

I'm no more a fan of SVN than the next, modern developer, but it still exists.
If I have to use it, I'm going to make it as painless as possible.


------------
Installation
------------

Install via PyPI::

    $ sudo pip install svncl


-----
Usage
-----

To generate a changelog::

    $ svncl . https://svnserver.com/tags/project
    - Setup fix.
    - Removed obsolete references to collections package.
    - Updates are now stored in S3.
    - Added parallel S3 downloading.

This represents the four commits that have occurred since the last tag/release.

To do a release and simply pipe the output of *svncl* into the commit-message::

    $ svncl . https://svnserver.com/tags/project1 | \
        svn cp -F - \
            https://svnserver.com/trunk/project1 \
            https://svnserver.com/tags/project1/project1-1.4.4 

    Committed revision 767.

    $ svn log -l 1 https://svnserver.com/tags/project1
    ------------------------------------------------------------------------
    r767 | dustin | 2014-06-24 03:11:36 -0400 (Tue, 24 Jun 2014) | 13 lines

    - Setup fix.
    - Removed obsolete references to collections package.
    - Updates are now stored in S3.
    - Added parallel S3 downloading.
