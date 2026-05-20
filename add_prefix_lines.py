s="line1\nline2\nline3"
prefix=">> "
print("\n".join(prefix+i for i in s.splitlines()))