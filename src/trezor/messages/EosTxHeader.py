# Automatically generated by pb2py
# fmt: off
import protobuf as p


class EosTxHeader(p.MessageType):

    def __init__(
        self,
        expiration: int = None,
        ref_block_num: int = None,
        ref_block_prefix: int = None,
        max_net_usage_words: int = None,
        max_cpu_usage_ms: int = None,
        delay_sec: int = None,
    ) -> None:
        self.expiration = expiration
        self.ref_block_num = ref_block_num
        self.ref_block_prefix = ref_block_prefix
        self.max_net_usage_words = max_net_usage_words
        self.max_cpu_usage_ms = max_cpu_usage_ms
        self.delay_sec = delay_sec

    @classmethod
    def get_fields(cls):
        return {
            1: ('expiration', p.UVarintType, 0),  # required
            2: ('ref_block_num', p.UVarintType, 0),  # required
            3: ('ref_block_prefix', p.UVarintType, 0),  # required
            4: ('max_net_usage_words', p.UVarintType, 0),  # required
            5: ('max_cpu_usage_ms', p.UVarintType, 0),  # required
            6: ('delay_sec', p.UVarintType, 0),  # required
        }
