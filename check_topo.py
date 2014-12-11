def check_topo(data_old,data_new,result_topo_deleted):
    num_of_old_links=len(data_old['edgeProperties'])
    num_of_new_links=len(data_new['edgeProperties'])
    for link_index_old in range(num_of_old_links):
        switch_id_old=data_old['edgeProperties'][link_index_old]['edge']['headNodeConnector']['node']['id']       

        flag=0

        for link_index_new in range(num_of_new_links):
            if switch_id_old==data_new['edgeProperties'][link_index_new]['edge']['headNodeConnector']['node']['id']:
                port_id_old=data_old['edgeProperties'][link_index_new]['edge']['headNodeConnector']['id']
                if port_id_old==data_old['edgeProperties'][[link_index_new]]['edge']['headNodeConnector']['id']:
                    switch_id_old_2=data_old['edgeProperties'][link_index_old]]['edge']['tailNodeConnector']['node']['id']
                    if switch_id_old_2==data_new['edgeProperties'][link_index_new]['edge']['tailNodeConnector']['node']['id']:
                        port_id_old_2=data_old['edgeProperties'][link_index_new]['edge']['headNodeConnector']['id']
                        if port_id_old_2==data_old['edgeProperties'][[link_index_new]]['edge']['headNodeConnector']['id']:
                        flag=1
                        break
        if flag==0:

            {'headNodeConnector':[],'hn port':[],'tailNodeConnector':[],'tn port':[]}
            
            result_topo_deleted['headNodeConnector'].append((switch_id_old))
            result_topo_deleted['hn port'].append((switch_id_old))
            result_topo_deleted['tailNodeConnector'].append((switch_id_old_2))
            result_topo_deleted['tn port'].append((port_id_old_2))
            
            print 'Link Removed',' Switch ',switch_id_old,' port ',switch_id_old,' --- ',' Switch ',switch_id_old_2,' port ',port_id_old_2
    return result_topo_deleted


