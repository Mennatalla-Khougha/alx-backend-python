#!/usr/bin/env python3
from utils import access_nested_map


n_map_1  = {"a": 1}
p_1 = ("a", )
res_1 = access_nested_map(n_map_1, p_1)
print(res_1)

n_map_2  = {"a": {"b": 2}}
p_2 = ("a", )
res_2 = access_nested_map(n_map_2, p_2)
print(res_2)

n_map_3  = {"a":{"b": 2}}
p_3 = ("a", "b")
res_3 = access_nested_map(n_map_3, p_3)
print(res_3)