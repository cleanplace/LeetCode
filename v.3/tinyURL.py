import random
#난수 생성
# class Codec:
#     def __init__(self):
#         self.tiny_urls = {}
#
#     def encode(self, longUrl: str) -> str:
#         num_form = random.randint(1, 1E10)
#
#         while num_form in self.tiny_urls:
#             num_form = random.randint(1, 1E10)
#
#         self.tiny_urls[num_form] = longUrl
#
#         return 'http://tinyurl.com/' + str(num_form)
#
#     def decode(self, S: str) -> str:
#         return self.tiny_urls[int(S[19:])]


#자동 해싱키 생성
# import string
# class Codec:
#
#     alphabet = string.ascii_letters + '0123456789'
#
#     def __init__(self):
#         self.url2code = {}
#         self.code2url = {}
#
#     def encode(self, longUrl):
#         while longUrl not in self.url2code:
#             code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
#             if code not in self.code2url:
#                 self.code2url[code] = longUrl
#                 self.url2code[longUrl] = code
#         return 'http://tinyurl.com/' + self.url2code[longUrl]
#
#     def decode(self, shortUrl):
#         return self.code2url[shortUrl[-6:]]

import hashlib
def get_hash_value(in_str, in_digest_bytes_size=64, in_return_type='digest'):
    """해시값을 구한다
    Parameter:
        in_str: 해싱할문자열,
        in_digest_bytes_size: Digest바이트크기,
        in_return_type: 반환형태(digest or hexdigest or number) """

    assert 1 <= in_digest_bytes_size and in_digest_bytes_size <= 64
    blake  = hashlib.blake2b(in_str.encode('utf-8'), digest_size=in_digest_bytes_size)
    if in_return_type == 'hexdigest': return blake.hexdigest()
    elif in_return_type == 'number': return int(blake.hexdigest(), base=16)

    return blake.digest()

###Hash 함수를 통과 하기전의 원본 데이터를 메세지(message)라고 부르고, 통과된 이후의 데이터를 다이제스트(digest)라고 부름
class Codec:
    def __init__(self):
        self.tiny_urls = {}

    def encode(self, longUrl: str) -> str:
        message = 'JIAN KIM'
        num_form = get_hash_value(in_str=message, in_digest_bytes_size=5, in_return_type='hexdigest')

        self.tiny_urls[num_form] = longUrl

        return 'http://tinyurl.com/' + str(num_form)

    def decode(self, S: str) -> str:
        return self.tiny_urls[S[19:]]


if __name__ == "__main__":

    c = Codec()
    longUrl='https://leetcode.com/problems/design-tinyurl'

    en = c.encode(longUrl)
    de = c.decode(en)

    print(en)
    print(de)