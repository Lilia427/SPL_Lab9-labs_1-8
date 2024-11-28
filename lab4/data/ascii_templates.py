def get_ascii_template(char, symbol):
    templates = {
        "A": [
            f"  {symbol}  ",
            f" {symbol} {symbol} ",
            f"{symbol}{symbol}{symbol}{symbol}{symbol}",
            f"{symbol}   {symbol}",
            f"{symbol}   {symbol}"
        ],
        "B": [
            f"{symbol}{symbol}{symbol} ",
            f"{symbol}   {symbol}",
            f"{symbol}{symbol}{symbol} ",
            f"{symbol}   {symbol}",
            f"{symbol}{symbol}{symbol} "
        ],
        "C": [
            f" {symbol}{symbol}{symbol}",
            f"{symbol}   ",
            f"{symbol}   ",
            f"{symbol}   ",
            f" {symbol}{symbol}{symbol}"
        ],
        "D": [
            f"{symbol}{symbol}{symbol} ",
            f"{symbol}   {symbol}",
            f"{symbol}   {symbol}",
            f"{symbol}   {symbol}",
            f"{symbol}{symbol}{symbol} "
        ],
        "E": [
            f"{symbol}{symbol}{symbol}{symbol}{symbol}",
            f"{symbol}    ",
            f"{symbol}{symbol}{symbol} ",
            f"{symbol}    ",
            f"{symbol}{symbol}{symbol}{symbol}{symbol}"
        ],
        "F": [
            f"{symbol}{symbol}{symbol}{symbol}{symbol}",
            f"{symbol}    ",
            f"{symbol}{symbol}{symbol} ",
            f"{symbol}    ",
            f"{symbol}    "
        ],
        "G": [
            f" {symbol}{symbol}{symbol}{symbol}",
            f"{symbol}    ",
            f"{symbol}  {symbol}{symbol}{symbol}",
            f"{symbol}   {symbol}",
            f" {symbol}{symbol}{symbol}{symbol}"
        ],
        "H": [
            f"{symbol}   {symbol}",
            f"{symbol}   {symbol}",
            f"{symbol}{symbol}{symbol}{symbol}{symbol}",
            f"{symbol}   {symbol}",
            f"{symbol}   {symbol}"
        ],
        "I": [
            f"{symbol}{symbol}{symbol}",
            f" {symbol} ",
            f" {symbol} ",
            f" {symbol} ",
            f"{symbol}{symbol}{symbol}"
        ],
        "J": [
            f"  {symbol}{symbol}{symbol}",
            f"    {symbol}",
            f"    {symbol}",
            f"{symbol}   {symbol}",
            f" {symbol}{symbol}{symbol} "
        ],
        "K": [
            f"{symbol}   {symbol}",
            f"{symbol}  {symbol} ",
            f"{symbol}{symbol}   ",
            f"{symbol}  {symbol} ",
            f"{symbol}   {symbol}"
        ],
        "L": [
            f"{symbol}    ",
            f"{symbol}    ",
            f"{symbol}    ",
            f"{symbol}    ",
            f"{symbol}{symbol}{symbol}{symbol}{symbol}"
        ],
        "M": [
            f"{symbol}   {symbol}",
            f"{symbol}{symbol} {symbol}{symbol}",
            f"{symbol} {symbol} {symbol}",
            f"{symbol}   {symbol}",
            f"{symbol}   {symbol}"
        ],
        "N": [
            f"{symbol}   {symbol}",
            f"{symbol}{symbol}  {symbol}",
            f"{symbol} {symbol} {symbol}",
            f"{symbol}  {symbol}{symbol}",
            f"{symbol}   {symbol}"
        ],
        "O": [
            f" {symbol}{symbol}{symbol} ",
            f"{symbol}   {symbol}",
            f"{symbol}   {symbol}",
            f"{symbol}   {symbol}",
            f" {symbol}{symbol}{symbol} "
        ],
        "P": [
            f"{symbol}{symbol}{symbol} ",
            f"{symbol}   {symbol}",
            f"{symbol}{symbol}{symbol} ",
            f"{symbol}    ",
            f"{symbol}    "
        ],
        "Q": [
            f" {symbol}{symbol}{symbol} ",
            f"{symbol}   {symbol}",
            f"{symbol} {symbol} {symbol}",
            f" {symbol}{symbol}{symbol} ",
            f"     {symbol}"
        ],
        "R": [
            f"{symbol}{symbol}{symbol} ",
            f"{symbol}   {symbol}",
            f"{symbol}{symbol}{symbol} ",
            f"{symbol}  {symbol} ",
            f"{symbol}   {symbol}"
        ],
        "S": [
            f" {symbol}{symbol}{symbol}{symbol}",
            f"{symbol}    ",
            f" {symbol}{symbol}{symbol}",
            f"    {symbol}",
            f"{symbol}{symbol}{symbol}{symbol} "
        ],
        "T": [
            f"{symbol}{symbol}{symbol}{symbol}{symbol}",
            f"   {symbol}   ",
            f"   {symbol}   ",
            f"   {symbol}   ",
            f"   {symbol}   "
        ],
        "U": [
            f"{symbol}   {symbol}",
            f"{symbol}   {symbol}",
            f"{symbol}   {symbol}",
            f"{symbol}   {symbol}",
            f" {symbol}{symbol}{symbol} "
        ],
        "V": [
            f"{symbol}   {symbol}",
            f"{symbol}   {symbol}",
            f" {symbol} {symbol} ",
            f" {symbol} {symbol} ",
            f"  {symbol}   "
        ],
        "W": [
            f"{symbol}   {symbol}",
            f"{symbol}   {symbol}",
            f"{symbol} {symbol} {symbol}",
            f"{symbol}{symbol} {symbol}{symbol}",
            f"{symbol}   {symbol}"
        ],
        "X": [
            f"{symbol}   {symbol}",
            f" {symbol} {symbol} ",
            f"  {symbol}   ",
            f" {symbol} {symbol} ",
            f"{symbol}   {symbol}"
        ],
        "Y": [
            f"{symbol}   {symbol}",
            f" {symbol} {symbol} ",
            f"  {symbol}   ",
            f"  {symbol}   ",
            f"  {symbol}   "
        ],
        "Z": [
            f"{symbol}{symbol}{symbol}{symbol}{symbol}",
            f"    {symbol}   ",
            f"   {symbol}   ",
            f"  {symbol}    ",
            f"{symbol}{symbol}{symbol}{symbol}{symbol}"
        ],
    }
    return templates.get(char.upper(), [f"{symbol}"])

def build_template_art(text, symbol):
    lines = [""] * 5  

    for char in text:
        char_template = get_ascii_template(char, symbol)
        for i in range(5):
            lines[i] += char_template[i] + "  "  

    return "\n".join(lines)

if __name__ == "__main__":
    text = "HELLO"
    symbol = "#"
    ascii_art = build_template_art(text, symbol)
    print(ascii_art)
