= Git Location =

== Description ==

Adds a Git Location link to the contextual navigation under Browse Source. The link points to the Git URL for the folder you're viewing. This is very handy for making checkouts and such.

== Installation ==

Follow the normal [http://trac.edgewall.org/wiki/TracPlugins egg installation procedures].

Under the [components] section, enable the plugin:

{{{
[components]
gitlocation.* = enabled
}}}

Finally, add a section to your project's trac.ini:

{{{
[git]
repository_url = https://your.repository/location
}}}

Drink, and enjoy.

== Author ==

Git Location is a shameless rip-off of Erik Rose' Subversion Location plugin and therefore also based on jhammel's [http://trac-hacks.org/wiki/SvnUrlsPlugin SvnUrlsPlugin]. Thanks, Erik & jhammel!

== Version History ==

 1.0::
  Initial release