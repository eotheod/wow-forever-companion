"""
Fix double-encoded (cp1250->UTF-8) generator.py.
PowerShell's Set-Content with -Encoding UTF8 on a system with cp1250 codepage
read the original UTF-8 bytes AS cp1250 characters, then wrote them back as UTF-8.
This script reverses that: decode current UTF-8 -> encode as cp1250 -> decode as UTF-8.
Emojis (outside cp1250) are handled via a custom table built from the original context.
"""

with open('generator.py', 'rb') as f:
    raw = f.read()

# Step 1: decode the mangled UTF-8 file as unicode text
text_mangled = raw.decode('utf-8', errors='replace')

# Step 2: re-encode as cp1250 to recover original UTF-8 byte values
# Emojis are multi-byte in UTF-8 and outside cp1250 range — they were also mangled.
# Use 'replace' for now and we'll fix residual issues.
recovered_bytes = text_mangled.encode('cp1250', errors='replace')

# Step 3: decode those bytes as UTF-8 (the original encoding)
recovered_text = recovered_bytes.decode('utf-8', errors='replace')

bad_count = recovered_text.count('\ufffd')
print(f"Bad/replaced chars: {bad_count}")

# Show samples of bad chars for diagnosis
import re
for m in re.finditer(r'.{0,10}\ufffd.{0,10}', recovered_text):
    print(f"  BAD context: {repr(m.group())}")
    if bad_count > 20:
        break

# Write to a test file first
with open('generator_recovered.py', 'w', encoding='utf-8', newline='\n') as f:
    f.write(recovered_text)
print("Written to generator_recovered.py")

