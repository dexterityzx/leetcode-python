def convert(s, numRows):
    if numRows <= 1:
        return s
    container = ["" for _ in range(numRows)]
    container_idx = 0
    direction = 1;
    for char in s:
        # print 'direction:'+ str(direction)
        # print 'container_idx:'+ str(container_idx)
        container[container_idx] += char
        if container_idx+direction == numRows or container_idx+direction == -1:
            direction*=-1
        container_idx += direction
    return_string = ""
    for _str in container:
        return_string += _str
    return return_string
print convert("PAYPALISHIRING",1)