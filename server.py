#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import bottle
import gevent
import gevent.monkey

gevent.monkey.patch_all()

# Should be import after "gevent.monkey.patch_all()"
import bottle_jsonrpc


@bottle.route('/')
def index():
    return bottle.static_file('example.html', os.getcwd())


jsonrpc = bottle_jsonrpc.register('/rpc')


@jsonrpc
def add(a, b):
    return a + b


@jsonrpc
def sort(lst):
    return sorted(lst)


@jsonrpc
def power(base, power):
    print "receive: {}".format(base, power)
    time.sleep(5)
    gevent.sleep(0)
    print "respond: {}".format(base ** power)
    gevent.sleep(0)
    return base ** power


@jsonrpc
def echo(msg):
    print "receive: {}".format(msg)
    time.sleep(2)
    gevent.sleep(0)
    print "respond: {}".format(msg)
    gevent.sleep(0)
    return msg


bottle.debug(False)

if __name__ == '__main__':
    # Standalone web server
    bottle.run(reloader=True, server="gevent")
else:
    # Running under WSGI (probably apache)
    application = bottle.default_app()
