import logging
import sys
import time
import hashlib
import json

from ecdsa import NIST256p
from ecdsa import VerifyingKey

import utils

MINING_DIFFICULTY = 4
MINING_SENDER = 'i am mining sender'
MINING_REWARD = 1.0

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)


class BlockChain(object):
    """Creating Blockchain 
    
    
    
    """

    def __init__(self, blockchain_address=None, port=None):
        self.transaction_pool = []
        self.chain = []
        self.create_block(0, self.hash({}))
        self.blockchain_address = blockchain_address
        self.port = port

    def create_block(self, nonce, previous_hash):
        block = utils.sorted_dict_by_key({
            'timestamp': time.time(),
            'transactions': self.transaction_pool,
            'nonce': nonce,
            'previous_hash': previous_hash
        })
        self.chain.append(block)
        self.transaction_pool = []

        return block

    def hash(self, block):
        sorted_block = json.dumps(block, sort_keys=True)
        return hashlib.sha256(str(sorted_block).encode()).hexdigest()

    def add_transaction(self, sender_blockchain_address,
                        recipient_blockchain_address, value, sender_public_key=None, signature=None):
        
        """取引情報を追加する関数
        
        
        """

        transaction = utils.sorted_dict_by_key({
            'sender_blockchain_address': sender_blockchain_address,
            'recipient_blockchain_address': recipient_blockchain_address,
            'value': value
        })

        if sender_blockchain_address == MINING_SENDER:
            self.transaction_pool.append(transaction)
            return True

        if self.verify_transaction_signture(sender_public_key, signature, transaction):

            #if self.calculate_total_amount(sender_blockchain_address) < float(value):
            #    logger.error({'action': 'add_transaction', 'error': 'no value'})
            #    return False

            self.transaction_pool.append(transaction)
            return True
        return False

    def create_transaction(self,
                           sender_blockchain_address, recipient_blockchain_address,
                           value, sender_public_key, signature):

        is_transacted = self.add_transaction(
            sender_blockchain_address,
            recipient_blockchain_address,
            value,
            sender_public_key,
            signature
        )

        return is_transacted

    def verify_transaction_signture(self, sender_public_key, signature, transaction):
        sha256 = hashlib.sha256()
        sha256.update(str(transaction).encode('utf-8'))
        message = sha256.digest()
        signature_bytes = bytes().fromhex(signature)
        verifying_key = VerifyingKey.from_string(
            bytes().fromhex(sender_public_key), curve=NIST256p
        )
        verified_key = verifying_key.verify(signature_bytes, message)

        return verified_key

    def valid_proof(self, transactions, nonce, previous_hash, difficulty=MINING_DIFFICULTY):
        guess_block = utils.sorted_dict_by_key({
            'transactions': transactions,
            'nonce': nonce,
            'previous_hash': previous_hash
        })

        guess_hash = self.hash(guess_block)
        return guess_hash[:difficulty] == '0' * difficulty

    def proof_of_work(self):
        transactions = self.transaction_pool.copy()
        nonce = 0
        previous_hash = self.hash(self.chain[-1])

        while self.valid_proof(transactions, nonce, previous_hash) is False:
            nonce += 1
        return nonce

    def mining(self):
        nonce = self.proof_of_work()
        self.add_transaction(sender_blockchain_address=MINING_SENDER,
                             recipient_blockchain_address=self.blockchain_address,
                             value=MINING_REWARD)

        previous_hash = self.hash(self.chain[-1])
        self.create_block(nonce, previous_hash)
        logger.info({'action': 'mining', 'status': 'true'})
        return True

    def calculate_total_amount(self, blockchain_address):
        total_amount = 0
        for block in self.chain:
            for transaction in block['transactions']:
                value = float(transaction['value'])
                if blockchain_address == transaction['sender_blockchain_address']:
                    total_amount -= value
                if blockchain_address == transaction['recipient_blockchain_address']:
                    total_amount += value
        return total_amount
