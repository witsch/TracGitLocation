= Git Location Plugin =

== Description ==

Adds the Git Location to the contextual navigation under Browse Source.  Even though with Git this info is static, i.e. it doesn't change depending on which folder is browsed in Trac, it still comes in handy for making checkouts and such.

[[Image(screenshot.png)]]

== Installation ==

Follow the normal [http://trac.edgewall.org/wiki/TracPlugins egg installation procedures].

Under the `[components]` section, enable the plugin:
{{{
[components]
gitlocation.* = enabled
}}}

Finally, add a section to your project's trac.ini:
{{{
[git]
repository_url = git@foo.com:foobar
}}}

== Source ==

You can browser the source from [http://github.com/witsch/TracGitLocation/ github] using Git, or check it out via:
{{{
$ git clone git://github.com/witsch/TracGitLocation.git
}}}

== Credits ==

Git Location is a shameless rip-off of Erik Rose' [http://trac-hacks.org/wiki/SubversionLocationPlugin Subversion Location plugin] and therefore also based on jhammel's [http://trac-hacks.org/wiki/SvnUrlsPlugin SvnUrlsPlugin]. Thanks, Erik & jhammel!

== Version History ==

 1.0::
  Initial release