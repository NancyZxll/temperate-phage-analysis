list_f = open('file_list_choose')
f_out = open('file_list_complete','w')
for line in list_f:
    file_name = line.strip('\n')
    f_out.write(file_name)
    f_out.write('\t')
    # get host name from file name
    if file_name.startswith('NC_') or file_name.startswith('AF') or file_name.startswith('AY') or file_name.startswith('BX5718') or file_name.startswith('HG917'):
        f_host = open('ncbi_host.txt')
        for ncbi in f_host:
            ncbi = ncbi.strip('\n')
            if ncbi.split('\t')[0]==file_name:
                host_name = ncbi.split('\t')[1]
        f_host.close()
    elif file_name.startswith('SRR') or file_name.startswith('DRR') or file_name.startswith('ERR'):
        host_name = '_'.join(file_name.split('_')[1:-4])
    else:
        host_name = file_name.split('_')[0]
    # modify file name
    host_name = host_name.replace('_',' ')
    f = open('not_find_list.txt')
    for temp in f:
        temp = temp.strip('\n')
        if host_name == temp.split('\t')[0]:
            host_name = temp.split('\t')[1]
            break
    f.close()
    # get complete taxonomy
    check = 0
    f = open('host_list_add.txt')
    for temp in f:
        temp = temp.strip('\n').rstrip('\t')
        if host_name == temp.split('\t')[0]:
            f_out.write('\t'.join(temp.split('\t')[0:]))
            check = 1
            break
    if check == 0:
        print(host_name)
    f_out.write('\n')

f_out.close()
list_f.close()

