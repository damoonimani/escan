#!/usr/bin/env python
# -*- coding: utf-8 -*-
from web3 import Web3
import time
import json

# provider can be infura, ganache or geth
provider = input('enter http provider url: ')

# 2 addresses to follow 
ads = []

ads.append(input('enter first address: '))
ads.append(input('enter second address: '))

print(ads)

# USDT contract address
usdt = '0xdac17f958d2ee523a2206206994597c13d831ec7'

web3 = Web3(Web3.HTTPProvider(provider))

block_number = 0

#infinite loop for getting each block
while(True):
    # get latest block
    block = web3.eth.get_block('latest')
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
                        # log any transaction from or to addresses
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
    else:
        time.sleep(5)
    
