"""
This file is part of Ludolph: Skeleton plugin
Copyright (C) 2015 Erigones, s. r. o.

See the LICENSE file for copying permission.
"""
import time

from ludolph_skeleton import __version__
from ludolph.command import CommandError, command
from ludolph.plugins.plugin import LudolphPlugin


class HelloWorld(LudolphPlugin):
    """
    Ludolph: Skeleton, Hello World plugin commands.

    Sample plugin with 3 commands. Each showing how you can use Ludolph decorators in your plugins.
    """
    __version__ = __version__

    # noinspection PyUnusedLocal
    @command
    def hello_world(self, msg):
        """
        Hello World greeting.

        Usage: hello-world
        """
        return 'Hi, I am the Hello World plugin reply!'

    # noinspection PyUnusedLocal
    @command(stream_output=True)
    def hello_repeat(self, msg, *args):
        """
        Hello World plugin parameters repeater with streaming output.
        Repeat all parameters passed to command, each in separate reply message.
        First parameter is required.

        Usage: hello-repeat [param1] [param2] [param3] [paramN]
        """
        if not args:
            raise CommandError('You gave me nothing to repeat :(')

        for arg in args:
            yield 'I have received parameter: "%s"' % arg
            time.sleep(0.3)

    # noinspection PyUnusedLocal
    @command(admin_required=True)
    def hello_admin(self, msg):
        """
        Hello Admin greeting (admin only).

        Usage: hello-admin
        """
        return 'Hi, I am the Hello Admin plugin reply!'
