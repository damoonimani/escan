#!/usr/bin/env python
# -*- coding: utf-8 -*-
from web3 import Web3
import json

provider = 'https://mainnet.infura.io/v3/40dd1a9d49e64bb18c3e92902aaf26eb'

ads = ['0xEaad58e77D20B23A3dF57661278a6679FBd279B2', '0x7593BD8AeE555956AbE62BbE440626685C5eaFb9']

usdt = '0xdac17f958d2ee523a2206206994597c13d831ec7'

web3 = Web3(Web3.HTTPProvider(provider))

block_number = 0


print(ads)
print('0xeaad58e77d20b23a3df57661278a6679fbd279b2' in ads)


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
            _contract = tx_receipt['contractAddress']
            if(str(_to) in ads or str(_from) in ads):
                if str(_to) == usdt or str(_from) == usdt or str(_contract) == usdt:
                    tx = web3.eth.get_transaction(transaction_hash)
                    tx_dict = {
                        'to' : _to, 
                        'from' : _from,
                        'contract' : _contract,
                        'usdt_transaction' : True,
                        'value' : tx['value'],
                        'block_hash' : tx['blockHash'],
                        'tx_index' : tx['transactionIndex'],
                        'tx_hash': tx['hash']
                    }
                    print(tx_dict)
                    with open('usdt.txt', 'a') as usdt_file:
                        usdt_file.write(str(tx_dict))
                        usdt_file.write('-------------------')
                else:
                    tx = web3.eth.get_transaction(transaction_hash)
                    tx_dict = {
                        'to' : _to, 
                        'from' : _from,
                        'contract' : _contract,
                        'usdt_transaction' : True,
                        'value' : tx['value'],
                        'block_hash' : tx['blockHash'],
                        'tx_index' : tx['transactionIndex'],
                        'tx_hash': tx['hash']
                    }
                    print(tx_dict)
                    with open("file.txt", 'a') as file:
                        file.write(str(tx_dict))
                        file.write('-------------------')
