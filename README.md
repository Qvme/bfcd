## Decoding 🧠F☁️ck with Digital Circuits

just tryin' to decode BF using digital circuits.  
this project doesn't follow any specific design style.

**Project status:** ongoing / unstable 🔧

### Wanna try it out?
write BF code using the table below. for starters, try incrementing cells and outputting the cell content.

| Decimal | Binary (4-bit) | Hex | Description | BF Equivalent | Implemented |
|--------:|:---------------:|:---:|:------------|:-------------:|:-----------:|
| 0 | 0000 | 0x0 | Do nothing | > | ✅ |
| 1 | 0001 | 0x1 | Move pointer right | > | ✅ |
| 2 | 0010 | 0x2 | Move pointer left | < | ✅ |
| 3 | 0011 | 0x3 | Input from buffer | , | ✅ |
| 4 | 0100 | 0x4 | Output to TTY at current location | . | ✅ |
| 5 | 0101 | 0x5 | Increment current cell value | + | ✅ |
| 6 | 0110 | 0x6 | Decrement current cell value | - | ✅ |
| 7 | 0111 | 0x7 | Enter loop (jump if current != 0) | [ | - |
| 8 | 1000 | 0x8 | Terminate loop (jump if current == 0) | ] | - |
| 9 | 1001 | 0x9 | End of line / Reset | EOL | - |

### Issues
- For some reason the RAM pointer has an offset of 2 relative to ROM/counter. I'm debugging it — if you can spot the issue, let me know.

### Software requirements
- logisim-evolution simulator: https://github.com/logisim-evolution/logisim-evolution
