A Slack bot to let people know when coffee is ready!

Based off [this article](https://blog.cloudstitch.com/how-i-hacked-amazon-s-5-wifi-button-to-track-baby-data-794214b0bdd8) with modified code lifted from a now defunct [Nelson Cash](https://nelsoncash.com/) blog.

This code requires scapy, which is kind of a bear to install on a mac. Check [this install guide](http://scapy.readthedocs.io/en/latest/installation.html#platform-specific-instructions) out if you get stuck.

To start, create a copy of `constants-example.py`, rename to `constants.py` and fill in your Slack API token, the  ID for the channel you'd like the notice posted in, and the MAC address of the dash button.

Note: since this script requires packet sniffing, you'll need to run it as `sudo`.
