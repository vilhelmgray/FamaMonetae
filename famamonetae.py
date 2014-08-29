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

username = 'user'
password = 'pass'
server = '127.0.0.1'
port = '8332'

access = AuthServiceProxy('http://'+username+':'+password+'@'+server+':'+port)

txid = sys.argv[1]
rawtx = access.getrawtransaction(txid)
decodedtx = access.decoderawtransaction(rawtx)

vouts = decodedtx['vout']

fp = open("rumor.dat", "wb")

for vout in vouts:
    address = vout['scriptPubKey']['addresses'][0]
    data = base58.decode(address)[1:-4]
    fp.write(data)

fp.close()
