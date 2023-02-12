""" Genshin Web Event Check-in bot """
from os import environ as _ENV

from .api import Client as _Client, Region as _Region


def main(token=None, ac_id=None, uuid=None, region=None):
    """ The Main Method """
    if not token:
        token = _ENV['MHYTOKEN']
    if not ac_id:
        ac_id = int(_ENV['MHYACID'])
    if not uuid:
        uuid = _ENV['MHYUUID']
    if not region:
        region = _Region(_ENV['REGION'])
    client = _Client(token, ac_id, uuid, region=region)

    if len(client.other_events) > 0:
        for event in client.other_events:
            # pylint: disable=consider-using-f-string
            print("::group::Event \"{name}\"".format(**event))
            print(client.do_event(event))
            print('::endgroup::')

# vim: ft=python3:ts=4:et:
