#!/usr/bin/env python
# -*- coding: utf-8 -*-


from web3 import Web3
import json

provider = 'https://mainnet.infura.io/v3/40dd1a9d49e64bb18c3e92902aaf26eb'

web3 = Web3(Web3.HTTPProvider(provider))

block_number = 0

block = web3.eth.get_block(14302518)

if block['number'] > block_number:
    block_number = block['number']

    print('checking' + str(block['number']))

    txs = block['transactions']
    tx_count = len(txs)

    print('transactions count: ' + str(tx_count))
    for transaction_hash in txs:
        tx_receipt = web3.eth.get_transaction_receipt(transaction_hash)
        status = tx_receipt['status']
        if status == 1:
            _to = tx_receipt['to']
            _from = tx_receipt['from']
            print('to: ' + _to) 
            print('from: ' + _from)
