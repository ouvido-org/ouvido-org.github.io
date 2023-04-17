import subprocess as cmd
import os

os.system('sigal build /Users/shandi/Documents/GitHub/ouvido')
cmd.run('git add -A', check=True, shell=True)
cmd.run('git commit -m "commit"', check=True, shell=True)
cmd.run("git push", check=True, shell=True)
print("Success")
  
