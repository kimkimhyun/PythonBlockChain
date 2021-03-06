import logging
import sys
import time

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

class BlockChain(object):

    def __init__(self):
        self.transaction_pool = []
        self.chain = []
        self.create_block(0, 'init hash')

    def create_block(self, nonce, previous_hash):
        block = {
            'timestamp' : time.time(),
            'transactions' : self.transaction_pool,
            'nonce':nonce,
            'previous_hash':previous_hash
        }

        self.chain.append(block)
        self.transaction_pool = []
        return block

def print(chains):
    for i, chain in enumerate(chains):
        print(f'{"="*25} Chain {i} {"="*25}')
        for k, v in chain.items():
            print(f'')

if __name__ == '__main__':
    block_chain = BlockChain()
    print(block_chain.chain)
    block_chain.create_block(5, 'hash 1')
    print(block_chain.chain)
    block_chain.create_block(2, 'hash 2')
    print(block_chain.chain)