# M2K
Yet another midi to keystroke thing


## Notes
`rtmidi` installation is broken under Windows, setting [python38 in it's setup.py works](https://github.com/patrickkidd/pyrtmidi/blob/master/setup.py#L52)

`rtmidi` requires atleast `alsa-lib-devel` and `libstdc++-devel` on Fedora 32, or maybe nothing with the `rtmidi` package installed?
