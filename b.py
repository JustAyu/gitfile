import pexpect

try:
    child = pexpect.spawn("python a.py")
    child.expect(pexpect.EOF)
    output = child.before
    print(output)
except pexpect.EOF:
    print("End of file (EOF) encountered.")
except pexpect.TIMEOUT:
    print("Timeout occurred.")
except Exception as e:
    print("An unexpected error occurred: ", e)



