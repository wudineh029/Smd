import pandas as pd

# Function to format resistor value
def format_value(value):
    if value == 0:
        return "0 Ω (jumper)"
    elif value >= 1_000_000:
        return f"{value/1_000_000:.3g} MΩ"
    elif value >= 1000:
        return f"{value/1000:.3g} kΩ"
    else:
        return f"{value} Ω"

# --- 3-digit codes ---
codes_3, values_3 = [], []
for i in range(1000):  # 000–999
    code = f"{i:03d}"
    if code == "000":
        val_str = "0 Ω (jumper)"
    else:
        sig = int(code[:2])
        mult = int(code[2])
        value = sig * (10 ** mult)
        val_str = format_value(value)
    codes_3.append(code)
    values_3.append(val_str)

# --- 4-digit codes ---
codes_4, values_4 = [], []
for i in range(10000):  # 0000–9999
    code = f"{i:04d}"
    if code == "0000":
        val_str = "0 Ω (jumper)"
    else:
        sig = int(code[:3])
        mult = int(code[3])
        value = sig * (10 ** mult)
        val_str = format_value(value)
    codes_4.append(code)
    values_4.append(val_str)

# --- R codes (decimal notation) ---
codes_r, values_r = [], []
# Common ranges like 0R1 to 9R9, 10R to 99R9
for ohms in [0.1, 0.22, 0.33, 0.47, 0.68, 1, 2.2, 3.3, 4.7, 6.8, 10, 22, 47, 100]:
    if ohms < 10:
        code = str(ohms).replace(".", "R")
    else:
        code = str(ohms).replace(".", "R")
    codes_r.append(code)
    values_r.append(format_value(ohms))

# Build DataFrames
df3 = pd.DataFrame({"Code (3-digit)": codes_3, "Value": values_3})
df4 = pd.DataFrame({"Code (4-digit)": codes_4, "Value": values_4})
dfr = pd.DataFrame({"Code (R type)": codes_r, "Value": values_r})

# Save to Excel
with pd.ExcelWriter("SMD_Resistor_Codes_Full.xlsx") as writer:
    df3.to_excel(writer, sheet_name="3-digit Codes", index=False)
    df4.to_excel(writer, sheet_name="4-digit Codes", index=False)
    dfr.to_excel(writer, sheet_name="R Codes", index=False)

print("✅ Full SMD Resistor Code Chart saved as 'SMD_Resistor_Codes_Full.xlsx'")
