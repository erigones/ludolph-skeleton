"""
This file is part of Ludolph: Hello World plugin
Copyright (C) 2015 Erigones, s. r. o.

See the LICENSE file for copying permission.
"""
import time

# noinspection PyPep8Naming
from hello_world import __version__
from ludolph.command import command, parameter_required, admin_required
from ludolph.plugins.plugin import LudolphPlugin


class Base(LudolphPlugin):
    """
    Ludolph: Hello world plugin commands.

    Sample plugin with 3 commands. Each showing how you can use Ludolph decorators in your plugins.
    """
    # noinspection PyUnusedLocal
    @command
    def hello_world(self, msg):
        """
        Hello World greeting.

        Usage: hello-world
        """
        return 'Hi, I am the Hello World plugin reply!'

    # noinspection PyUnusedLocal
    @parameter_required(1)
    @command(stream_output=True)
    def hello_repeat(self, msg, *args):
        """
        Hello World plugin parameters repeater with streaming output.
        Repeat all parameters passed to command, each in separate reply message.
        First parameter is required.

        Usage: hello-repeat <param1> [param2] [param3] [paramN]
        """
        for arg in args:
            yield 'I have received parameter: "%s"' % arg
            time.sleep(0.3)

    # noinspection PyUnusedLocal
    @admin_required
    @command
    def hello_version(self, msg):
        """
        Show version of Ludolph: Hello World plugin (admin only).

        Usage: hello-version
        """
        return 'Ludolph: Hello World plugin version: ' + __version__
