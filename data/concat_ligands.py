import numpy as np

ligands = ['0072', '0104', '0161', '0195', '0305', '0354', '0387', '0434', '0678', '0689', '0691', '0692', '0734', '0748',
               '0749','0752','0755','0759','0769','0770','0774','0786','0805','0820','0828','0830','0831','0874',
               '0946','0991','1077','1093','1249','1308','1311','1334','1336','1348','1351','1374','1375','1380',
               '1382','1384','1385','1386','1392','1402','1412','1418','1420','1425','1458','1478','1493']


site2_ligands = ['0072', '0104', '0161', '0195', '0305', '0354', '0387', '0434', '0678', '0692', '0748',
                 '0749','0759','0770','0830','0831','0874', '0946','1077','1093','1249', '1382','1386',
                 '1392','1418','1420']

site11_ligands = ['0689', '0691','0734','0752','0755','0769','0774','0786','0805','0820','0828','0991',
                  '1308','1311','1334','1336','1348','1351','1374','1375','1380','1384','1385',
                  '1402', '1412', '1425','1458','1478','1493']

full_lines = []
num_atoms = 0
for ligand in site11_ligands:
    file = open('xyz/'+ligand+'.xyz','r')
    lines = file.readlines()
    num_atoms += int(lines[0])
    full_lines.extend(lines[2:])
file = open('xyz/site11_ligands.xyz','w')
file.write(str(num_atoms))
file.write('\n\n')
file.writelines(full_lines)
