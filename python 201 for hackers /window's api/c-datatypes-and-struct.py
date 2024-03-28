#https://docs.python.org/3/library/ctypes.html

from ctypes import * 

b0 = c_bool(0)
b1 = c_bool(1)


print(b0)
print(type(b0))
print(b0.value)


print("\n------------------------------------------------------------")


print(b1)
print(type(b1))
print(b1.value)

print("\n------------------------------------------------------------")



i0 = c_uint(-1)
print(i0.value)


print("\n------------------------------------------------------------")


c0 = c_char_p(b"test")
print(c0.value)
print(c0)


print("\n------------------------------------------------------------")


c0 = c_char_p(b"test2")
print(c0)
print(c0.value)


print("\n------------------------------------------------------------")



p0 = create_string_buffer(5)
print(p0)
print(p0.raw)
print(p0.value)

p0.value = b"a"
print(p0.raw)
print(p0)

#https://docs.python.org/3/library/ctypes.html
print("\n------------------------------------------------------------")

i = c_int(42)
pi = pointer(i)


print(i)
print(pi)
print(pi.contents)

print("\n------------------------------------------------------------")

print(p0.value)
print(p0)
print(hex(addressof(p0)))

pt = byref(p0)
print(pt)

print(cast(pt, c_char_p).value)

print(cast(pt, POINTER(c_int)).contents)

print(ord('a'))

print("\n------------------------------------------------------------")



class PERSON(Structure):
    _fields_ = [("name", c_char_p),
                ("age", c_int)]

bob = PERSON(b"bob",30)
print(bob.name)
print(bob.age)

alice = PERSON(b"alice",20)
print(alice.name)
print(alice.age)


print("\n------------------------------------------------------------")

person_array_t = PERSON * 4
print(person_array_t)


print("\n------------------------------------------------------------")

person_array = person_array_t()

person_array[0] = PERSON(b"bob",30)
person_array[1] = PERSON(b"alice",20)
person_array[2] = PERSON(b"mallory",50)
person_array[3] = PERSON(b"Gaurav",21)

for person in person_array:
    print(person)
    print(person.name )
    print(person.age)
    print("\n")






'''
This code demonstrates various features of the `ctypes` module in Python to interact with C-style data types. Here's a breakdown of each section and its output:

**1. Boolean Values:**

```python
b0 = c_bool(0)
b1 = c_bool(1)

print(b0)  # Output: False
print(type(b0))  # Output: <class 'ctypes._CData'>
print(b0.value)  # Output: False

print("\n------------------------------------------------------------")

print(b1)  # Output: True
print(type(b1))  # Output: <class 'ctypes._CData'>
print(b1.value)  # Output: True
```

- `c_bool` represents a boolean value.
- `0` and `1` are converted to `False` and `True`, respectively.

**2. Unsigned Integer:**

```python
i0 = c_uint(-1)
print(i0.value)  # Output: 4294967295 (maximum unsigned 32-bit integer)
```

- `c_uint` represents an unsigned integer.
- `-1` is interpreted as the maximum value due to unsigned nature.

**3. Character Array:**

```python
c0 = c_char_p(b"test")
print(c0.value)  # Output: test
print(c0)        # Output: <function pointer at 0x7f7b5970a1d8> (implementation detail)

print("\n------------------------------------------------------------")

c0 = c_char_p(b"test2")
print(c0)  # Output: <function pointer at 0x7f7b5970a1d8> (implementation detail)
print(c0.value)  # Output: test2
```

- `c_char_p` represents a pointer to a character array (C-style string).
- Printing `c0` shows the memory address (implementation detail).
- `c0.value` decodes the bytes as a string.

**4. String Buffer:**

```python
p0 = create_string_buffer(5)
print(p0)  # Output: <function pointer at 0x7f7b5970a1d8> (implementation detail)
print(p0.raw)  # Output: b'\x00\x00\x00\x00\x00' (initial buffer)
print(p0.value)  # Output: '' (empty string)

p0.value = b"a"
print(p0.raw)  # Output: b'a\x00\x00\x00' (updated buffer)
print(p0)  # Output: <function pointer at 0x7f7b5970a1d8> (implementation detail)
```

- `create_string_buffer` creates a string buffer with a specified size.
- `p0.raw` accesses the raw bytes in the buffer.
- `p0.value` decodes the bytes as a string.

**5. Pointers and Casting:**

```python
i = c_int(42)
pi = pointer(i)

print(i)  # Output: 42
print(pi)  # Output: <function pointer at 0x7f7b5970a1d8> (implementation detail)
print(pi.contents)  # Output: 42 (value pointed to by pi)
```

- `pointer` creates a pointer to an existing variable.
- `pi.contents` accesses the value pointed to by the pointer.

**6. Memory Address and Type Casting:**

```python
print(p0.value)  # Output: a
print(p0)  # Output: <function pointer at 0x7f7b5970a1d8> (implementation detail)
print(hex(addressof(p0)))  # Output: 0x7f7b5970a1d8 (memory address of p0)

pt = byref(p0)
print(pt)  # Output: <memory address at 0x7f7b5970a1d8> (memory address of p0)

print(cast(pt, c_char_p).value)  # Output: a (cast pt to c_char_p and decode)

print(cast(pt
'''