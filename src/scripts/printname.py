import argparse
import datetime
parser = argparse.ArgumentParser(description="enter your name")
parser.add_argument("--name", type=str, required=True, help="enter ascii string")


args = parser.parse_args()

print(args.name)

if args.name:
    name = args.name
    bfcode = ""
    asmcode = ""
    for idx,chr in enumerate(name):
        ascii_val = int(ord(chr))
        if idx == 0:
            bfcode += "+"*ascii_val
            asmcode += "5"*ascii_val
        
        elif idx>0 and idx<len(name):
            prev_ascii_val = int(ord(name[idx-1]))
            diff = ascii_val - prev_ascii_val
            if diff>0:
                bfcode += "+"* diff
                asmcode += "5"* diff
            else:
                bfcode += "-"* (-diff)
                asmcode += "6" * (-diff)

        bfcode+="."
        asmcode+="4"
    
print(bfcode)
print("\n")
print(asmcode)

print(len(asmcode))

asmcode_length = len(asmcode)
output_length = 256  # 0x100 for a full 256 words
output = [0] * output_length

for idx, char in enumerate(asmcode):
    num = int(char)
    if idx < output_length:
        output[idx] = num


filename = str(datetime.datetime.now()).split(".")[0] + ".txt"

with open(filename,"w") as file:
    file.write("v3.0 hex words addressed\n")
    for i in range(0, output_length, 16):
        hex_address = f"{i:02x}: " + " ".join(f"{output[j]}" for j in range(i, min(i + 16, output_length)))
        file.write(hex_address+"\n")
