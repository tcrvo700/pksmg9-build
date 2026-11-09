#!/usr/bin/env python3
"""Builds personals/personal7 (20-byte entries) from the PKHeX Gen7 expansion
table (personal_uu_expansion, 84-byte entries).
Entry layout (20 bytes):
 0-5 base stats (HP Atk Def Spe SpA SpD), 6-7 types, 8 gender, 9 base friendship,
 10 exp growth, 11-16 abilities 1/2/H as u16 LE, 17-18 form stat index u16 LE, 19 form count
"""
import struct, sys
src = open(sys.argv[1], 'rb').read()
S = 0x54
out = bytearray()
for e in range(len(src) // S):
    d = src[e*S:(e+1)*S]
    nb = d[0x53]
    ab = [d[0x18] | (0x100 if nb & 1 else 0),
          d[0x19] | (0x100 if nb & 2 else 0),
          d[0x1A] | (0x100 if nb & 4 else 0)]
    out += d[0:6] + bytes([d[6], d[7], d[0x12], d[0x14], d[0x15]])
    out += b''.join(struct.pack('<H', a) for a in ab)
    out += d[0x1C:0x1E] + bytes([d[0x20]])
open(sys.argv[2], 'wb').write(out)
print(len(src)//S, "entries ->", len(out), "bytes")
