def get_switch_name(name):
        lenn=len(name)
        for index in range(lenn):
            if name[index]!='0':
                if name[index]!=':':
                        break
        return 'Switch-'+name[index:lenn]
