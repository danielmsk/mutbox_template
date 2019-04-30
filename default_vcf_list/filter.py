
def get_variant_bootstraptable_column(variant_column_list):
    datajs = ""
    for c1 in variant_column_list:
        if datajs != '': datajs += ','
        datajs += "{field:'"+c1+"',title:'"+c1+"',sortable:true,align:'center',visible:true}"
    return datajs


def convert_variant_list_to_bootstraptable(variant_list):
    datajs = ""

    for v1 in variant_list:
        if datajs != '': datajs += ','

        datajs += "{"
        for c1 in v1.keys():
            datajs += c1+":'"+v1[c1]+"',"
        datajs += "}"
    return datajs

