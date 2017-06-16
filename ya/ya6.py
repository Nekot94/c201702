url = input()
q = input()
pos = url.find("?")
while True:
    pos = url.find(q, pos + 1)
    if url[pos + len(q)] == "=" or pos == -1:
        break
end = url.find("&", pos + 1)
print(url[pos + len(q) + 1:end])