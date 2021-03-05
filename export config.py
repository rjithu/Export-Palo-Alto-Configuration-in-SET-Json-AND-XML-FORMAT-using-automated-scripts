import pexpect
import sys
import time

fw_user = "admin"
fw_pass = "admin"
fw_ip = "10.x.x.x"
prompt = "> $"
hash = "# $"
fw = pexpect.spawn("sshpass -p{} ssh -o StrictHostKeyChecking=no {}@{}".format(fw_pass, fw_user, fw_ip))
fw.logfile = open("config.log", "a")
fw.expect(prompt)
fw.sendline("set cli pager off")
fw.expect(prompt)
fw.sendline("show clock")
fw.sendline("set cli config-output-format set")
fw.expect(prompt)
fw.sendline("configure")
fw.expect(hash)
fw.sendline("show")
fw.expect(hash)
fw.sendline("exit")
fw.expect(prompt)
fw.sendline("set cli config-output-format default")
fw.sendline("exit")