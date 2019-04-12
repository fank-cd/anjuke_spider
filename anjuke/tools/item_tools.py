# coding:utf-8
import re


def get_nums(value):
    match_re = re.match(r".*?(\d+).*", value)
    if match_re:
        nums = match_re.groups(1)
    else:
        nums = 0
    return nums


def remove_n(value):
    value = value.strip().replace("\n", "").strip()
    return value

