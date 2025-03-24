"""Examples of set and dictionary syntax"""

pids: set[int] = {710000000, 712345678}
pids.add(730120710)

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

"""Edit existing value"""
ice_cream["vanilla"] += 110

"""length of dictionary"""
len(ice_cream)

"""Adding element to dictionary"""
ice_cream["mint"] = 3

"""Access existing value"""
ice_cream["chocolate"]

"""Modify existing value"""
ice_cream["vanilla"] = 10

"""Check if key is in dictionary"""
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("No orders of mint")

"""Removing element from dictionary"""
ice_cream.pop("strawberry")

"""for loops"""
for key in ice_cream:
    print(ice_cream[key])
