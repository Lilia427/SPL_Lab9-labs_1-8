def align_text(ascii_art, alignment, width):
    lines = ascii_art.split("\n")
    aligned_lines = []

    for line in lines:
        if alignment == "center":
            aligned_line = line.center(width)
        elif alignment == "right":
            aligned_line = line.rjust(width)
        else:
            aligned_line = line.ljust(width)
        aligned_lines.append(aligned_line)

    return "\n".join(aligned_lines)
