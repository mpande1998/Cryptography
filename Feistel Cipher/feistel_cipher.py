import hashlib


class Feistel:
    rounds = 4
    split = 1 / 2

    def __init__(self, key, rounds=rounds):
        self.subkeys = [hashlib.sha1(bytes((i,)) + key).digest() for i in range(rounds)]

    def encipher(self, data):
        split = int(len(data) * self.split)
        d1 = data[:split]
        d2 = data[split:]
        for sk in self.subkeys:
            d1, d2 = self.round(sk, d1, d2)
        return d1 + d2

    def decipher(self, data):
        split = int(len(data) * self.split)
        d1 = data[:split]
        d2 = data[split:]
        for sk in reversed(self.subkeys):
            d2, d1 = self.round(sk, d2, d1)
        return d1 + d2

    def round(self, subkey, d1, d2):
        padparts = ()
        padseed = d2
        for i in range((len(d1) + 19) // 20):
            padseed2 = hashlib.sha1(padseed + subkey).digest()
            padparts += padseed2
            padseed = padseed2
        pad = sum(padparts, b'')

        return d2, bytes(d ^ p for d, p in zip(d1, pad))
