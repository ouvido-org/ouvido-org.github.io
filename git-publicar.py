import subprocess as cmd
cmd.run('git add -A', check=True, shell=True)
cmd.run('git commit -m "message"', check=True, shell=True)
cmd.run("git push", check=True, shell=True)
print("Success")
  
