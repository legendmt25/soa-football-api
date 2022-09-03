from enum import Enum


class TransactionStatus(Enum):
    PENDING = "PENDING"
    RESOLVED = "RESOLVED"
    CANCELED = "CANCELED"