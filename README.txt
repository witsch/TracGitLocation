= Subversion Location =

== Description ==

Adds a Subversion Location link to the contextual navigation under Browse Source. The link points to the Subversion URL for the folder you're viewing. This is very handy for making checkouts and such.

== Installation ==

Follow the normal [http://trac.edgewall.org/wiki/TracPlugins egg installation procedures].

Under the [components] section, enable the plugin:

{{{
[components]
subversionlocation.* = enabled
}}}

Finally, add a section to your project's trac.ini:

{{{
[svn]
repository_url = https://your.repository/location
}}}

Drink, and enjoy.

== Author ==

Subversion Location is written by Erik Rose and based on jhammel's [http://trac-hacks.org/wiki/SvnUrlsPlugin SvnUrlsPlugin]. Thanks, jhammel!

== Version History ==

 1.0.1::
  * The Browse Source tab now highlights properly. Thanks to Jeremie Allard for the original patch.
  * Added egg dependency on Trac, which this of course imports from.
  * Fleshed out other egg metadata a bit.
 1.0::
  Initial release