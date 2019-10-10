
from enum import Enum


class RefundReason(Enum):
    AUTHOR_IN_BLACKLIST = "Author is in blacklist"
    SENDER_IN_BLACKLIST = "Sender is in blacklist"
    POST_IS_TOO_NEW = "Post age must be older than 5 minutes"
    POST_IS_TOO_OLD = "Post is too old"
    POST_IS_ALREADY_VOTED = "Post is already voted"


class Database:

    def __init__(self, db_connection):
        self.db_connection = db_connection

    def register_refund(self, sender, incoming_tx_block_height, incoming_tx_id,
                        outgoing_transfer_block_height,
                        outgoing_transfer_tx_id):
        pass

    def register_vote(self, author, permlink, incoming_transfer_block_height,
                      incoming_transfer_tx_id, outgoing_vote_block_height,
                      outgoing_vote_tx_id):
        pass

    def is_already_refunded(self, to, reason, permlink):
        pass

    def is_already_voted(self):
        pass

    def is_author_in_blacklist(self):
        pass

    def is_sender_is_blacklist(self):
        pass

