"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

import time

encode_message = "11111111111111111111111111111"

def helper_dp(message, memo={}):
    if len(message) == 0:
        return 1

    if message[0] == "0":
        return 0

    if message in memo.keys():
        return memo[message]

    result = helper_dp(message[1:], memo)
    if len(message) >= 2 and int(message[:2]) <= 26:
        result += helper_dp(message[2:], memo)
    memo[message] = result
    return result


def num_ways_dp(message):
    return helper_dp(message)


def helper(message):
    if len(message) == 0:
        return 1

    if message[0] == "0":
        return 0

    result = helper(message[1:])
    if len(message) >= 2 and int(message[:2]) <= 26:
        result += helper(message[2:])
    return result


def num_ways(message):
    return helper(message)

start_time = time.time()
print(num_ways(encode_message))
end_time = time.time()

print(end_time - start_time)

start_time = time.time()
print(num_ways_dp(encode_message))
end_time = time.time()

print(end_time - start_time)
