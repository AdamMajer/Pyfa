## Pyfa for Debian

You can grab your latest .deb release for Pyfa, the EVE fitting assistant.

The latest releases are available under [releases](https://github.com/AdamMajer/Pyfa/releases)

On Debian systems, you can verify the integrity of the changes file by,

    gpg --verify --keyring /usr/share/keyrings/debian-maintainers.gpg pyfa.changes

or if you are not using Debian, get the key from official Debian keyring server and verify,

    gpg --keyserver keyring.debian.org --recv-keys AC8DFBD0
    gpg --verify pyfa.changes

Then compare the SHA256 sum of the .deb file with the one in the .changes file.

### Are you going to upload Pyfa to Debian?

No. Pyfa changes with Eve, not with Debian update cycles. It is best Pyfa remains outside of Debian.
