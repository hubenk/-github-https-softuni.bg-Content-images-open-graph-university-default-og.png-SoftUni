from collections import deque


def math_operations(*args, **kwargs):
    rotate_keys = deque(kwargs.keys())
    nums = [x for x in args]

    while nums:
        if nums[0] == 0:
            nums.pop(0)
        else:
            if rotate_keys[0] == "a":
                kwargs[rotate_keys[0]] += nums.pop(0)
            elif rotate_keys[0] == "s":
                kwargs[rotate_keys[0]] -= nums.pop(0)
            elif rotate_keys[0] == "d":
                kwargs[rotate_keys[0]] /= nums.pop(0)
            elif rotate_keys[0] == "m":
                kwargs[rotate_keys[0]] *= nums.pop(0)

        rotate_keys.rotate(-1)
    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
