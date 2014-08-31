#!/usr/bin/python
# FamaMonetae decodes data stored as Bitcoin addresses in a Bitcoin
# transaction.
# Copyright (C) 2014  William Breathitt Gray
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/>.

import sys
from bitcoin import base58
from bitcoinrpc.authproxy import AuthServiceProxy

def hearRumor(txid, service_url, rumor_file):
    access = AuthServiceProxy(service_url)

    whispers = hearWhispers(txid, access)

    fp = open(rumor_file, "wb")
    for whisper in whispers:
        fp.write(whisper)
    
    fp.close()


def hearWhispers(txid, access):
    rawtx = access.getrawtransaction(txid)
    decodedtx = access.decoderawtransaction(rawtx)

    vouts = decodedtx['vout']

    whispers = []
    for vout in vouts:
        address = vout['scriptPubKey']['addresses'][0]
        whisper = base58.decode(address)[1:-4]
        whispers.append(whisper)

    return whispers
