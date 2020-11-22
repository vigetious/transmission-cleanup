## Transmission Space Checker

Small script I made in an afternoon to remove all files from the download directory that are not in a transmission client. Stupidly I save a lot of spare files in my directory, so I will run this as a cron job every month to clean up the spare files and folders.

This is designed to be used on the local network. You will need to change your RPC whielist settings in the transmission client config file if you wish to use in remotely.

You will need to create a Python virtual environment and install the ``requests`` library.

#### How to use:

Example usage:

``./python main.py 192.168.1.1:9091 /download/directory/ username password``

- First argument - Transmission download directory.
- Second argument - Transmission username.
- Third argument - Transmission password.
