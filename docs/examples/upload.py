#!/usr/bin/env python3

# Any copyright is dedicated to the Public Domain.
# http://creativecommons.org/publicdomain/zero/1.0/

from volapi import Room


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Provide a room ID", file=sys.stderr)
        sys.exit(1)

    def callback(current, total):
        print("Uploaded {} of {} bytes or {:.2%}".
              format(current, total, float(current) / total))

    r = Room(sys.argv[1])
    r.userChangeNick("DumbUpload")
    r.uploadFile(__file__, cb=callback)
