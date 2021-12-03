# Background

I was looking for a way to view multiple Twitch chats in a single window or session, and most of the tools out there were ... not very good! The main solution seemed to be to "pop out" each chat window as provided by Twitch's site and smash it into a single view, somehow--which tended not to work especially well, and even if it did, it was not a look suitable for including in a stream overlay. But I did discover [this learning repository for data science projects in Python](https://github.com/LearnDataSci/articles), from which I have forked just the one tool that proved relevant:

+ [How to Stream Text Data from Twitch with Sockets in Python](https://learndatasci.com/tutorials/how-stream-text-data-twitch-sockets-python/) [[<b>repo</b>](../../tree/master/How%20to%20Stream%20Text%20Data%20from%20Twitch%20with%20Sockets%20in%20Python)]

With a few minor modifications, that were apparently planned for the LearnDataSci project but never implemented, I extended the script to join and log multiple channels at once.

This fork of the repository thus isn't so much for Python data scientists, as for Twitch streamers looking to assemble a single chat log from the conversations in several collaborating channels! You can still visit the old exercises in the commit history, but the source repository is probably a better place for that!

# Setup

You'll need a Python runtime environment. [Python.org](https://www.python.org/downloads/) should have what you need!

Then, edit `chat_logger.py`.

* In the `nickname` variable, replace the example with your Twitch user name.
* In the `token` variable, replace "gibberish" with the gibberish supplied when you authenticate at [Twitchapps.com](https://twitchapps.com/tmi/).
* In the `channels`, replace the #channel1,2 bit with a comma-delimited list of quoted channel names led by hash signs. E.g. `['#kaliranya','#commanderroot','#serycodes']`

# Usage

To run the script,

> py .\chat_logger.py

in a terminal session in the repo directory is all you need. It will output a `chat.log` file that you can then add in e.g. OBS Studio as a Text source, reading from file, in "chatlog" mode with word wrap turned on, and you'll see chatter from all the added channels start to flow in!

To stop, halt the session with a Ctrl+C or Ctrl+Pause, whatever works to send a system interrupt in your environment. You'll want to delete or empty out chat.log before your next stream, or it'll carry over the chatter from the previous session.

# Help!

The script works. It gets the chats! It does the thing!
But it looks quite jank!
I would love to have this produce a nice overlay chat box like you'd find on StreamElements or Tipeeestream, but thus far that is beyond my capabilities.
Please! Smart coder people out there! Fork this and make it better!

Yours,
[Dame-Armiger Kali Ranya](https://twitch.tv/kaliranya)
