import subprocess


command = "python a.py"


# Create a subprocess with the command
proc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = proc.communicate()


if output:
    splited_output = (output.decode()).split(" ")
    print(splited_output)
    if 'phone' in splited_output:
        if 'number' in splited_output:
            if 'token:' in splited_output:
                ask_number = input("Please Give the mobile number : ")
                proc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, error = proc.communicate(f"{ask_number}\n".encode())
                splited_output = (output.decode()).split(" ")
                splited_error = (error.decode()).split(" ")
                if output:
                    print(splited_output)
                else:
                    print(splited_error)

                if '(y/N):' in splited_output:
                    if 'correct?' in splited_output:
                        ask_number = input("Giving Yes! ")
                        proc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        output, error = proc.communicate(f"y\n".encode())
                        splited_output = (output.decode()).split(" ")
                        splited_error = (error.decode()).split(" ")
                        if output:
                            print(splited_output)
                        else:
                            print(splited_error)


elif error:
    print(error.decode())