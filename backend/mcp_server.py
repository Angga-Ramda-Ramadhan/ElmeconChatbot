from fastmcp import FastMCP
from mcp_conn import connection_db_mcp
from model import query_elm


mcp = FastMCP("MCP Server")


@mcp.tool
def get_info_products(products: list[str]):
    
    conn = connection_db_mcp()

    argument = []
    value = []


    for item in products:
        argument.append('p.name ILIKE %s')
        value.append(f'%{item}%')

    


    cursor = conn.cursor()

    # query = f"""

    # SELECT p.nama, p.stocks, pp.price_class, pp.price
    # FROM products_tb p
    # JOIN products_price_tb pp ON p.id = pp.product_id
    # WHERE ({' OR '.join(argument)}) AND pp.price_class=%s

    # """

    query_elm1 = f"""

    SELECT p.value,p.name,p.em_skaab_klasifikasi,bb2.name as brand,
    sum(ms.qtyonhand-ms.reservedqty) as Stock,

    (select mp.pricestd
    from m_product p2
    left join m_productprice mp on p2.m_product_id=mp.m_product_id
    left join m_pricelist_version mv on mp.m_pricelist_version_id=mv.m_pricelist_version_id
    left join m_pricelist pp on mv.m_pricelist_id=pp.m_pricelist_id
    left join m_brand bb on p2.m_brand_id=bb.m_brand_id
    where p2.ad_client_id='8F03B5235ACB427CAF5EB65F2B0FD3ED'
    and p2.isactive='Y'
    and pp.m_pricelist_id='F1F0CB5679B44071ADBBDB28F734AF94'
    and mv.isactive='Y'
    and p2.value=p.value) as harga_end_user


    from m_product p
    left join m_storage_detail ms on p.m_product_id=ms.m_product_id
    left join m_locator ml on ms.m_locator_id=ml.m_locator_id
    left join m_warehouse mw on ml.m_warehouse_id=mw.m_warehouse_id
    left join m_brand bb2 on p.m_brand_id=bb2.m_brand_id
    where p.ad_client_id='8F03B5235ACB427CAF5EB65F2B0FD3ED'
    and mw.name='Warehouse Jakarta'
    and p.isactive='Y' 
    AND ({' OR '.join(argument)})
    group by p.value,p.name,p.em_skaab_klasifikasi,bb2.name


    """

    # value.append(price_class)
    print('ini value', value)
    cursor.execute(query_elm1, tuple(value))

    results = cursor.fetchall()

    if results:

        list_data = [{
            'nama_product':result[1],
            'stock':result[4],
            'harga end user':result[5]
        } for result in results]

        print('list data', list_data)

        return list_data
    
    else:
        return 'Tidak ditemukan product yang relevan dengan request user'
    

if __name__ == "__main__":
    mcp.run(transport="http", host='127.0.0.1', port=9000)