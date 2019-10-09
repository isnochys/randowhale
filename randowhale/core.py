from lightsteem.client import Client
from lightsteem.helpers.amount import Amount
from lightsteem.datastructures import Operation
import time

from datetime import datetime, timedelta


class TransferListener:

    def __init__(self, account=None, posting_key=None, active_key=None,
                 nodes=None):

        # default node is api.steemit.com
        if not nodes:
            nodes = ["https://api.steemit.com", ]

        self.account = account
        self.vote_client = Client(keys=[posting_key, ], nodes=nodes)
        self.refund_client = Client(keys=[active_key, ], nodes=nodes)

    def get_incoming_transfers(self):
        stop_at = datetime.now() - timedelta(hours=24)
        acc = self.vote_client.account(self.account)
        transfers = []
        for _, transaction in acc.history(
                filter=["transfer"],
                only_operation_data=False,
                stop_at=stop_at,
        ):
            op = transaction["op"][1]
            if op["to"] != self.account:
                continue
            transfers.append(transaction)

        return transfers

    def poll_transfers(self):
        while True:
            try:
                for transfer in self.get_incoming_transfers():
                    print(transfer)
            except Exception as error:
                print(error)
            time.sleep(3)