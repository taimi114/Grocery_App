from sql_connection import get_sql_connection

def get_all_products(connection):

    cursor = connection.cursor()
    query=("SELECT products.products_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
           "FROM products INNER JOIN uom ON products.uom_id=uom.uom_id;")

    cursor.execute(query)
    response=[]
    for (products_id, name, uom_id, price_per_unit,uom_name) in cursor:
        response.append(
            {
            'products_id':products_id,
            'name':name,
            'uom_id':uom_id,
            'price_per_unit':price_per_unit,
             'uom_name':uom_name
            }
        )


    return response
def insert_new_products(connection,products):
    cursor=connection.cursor()
    query=("INSERT INTO products"
           "(name,uom_id,price_per_unit)"
           "values (%s,%s,%s)")
    data=(products['products_name'],products['uom_id'],products['price_per_unit'])
    cursor.execute(query,data)
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid
def delete_products(connection,products_id):
    cursor=connection.cursor()
    query=("DELETE FROM  products WHERE products_id="+str(products_id)
           )

    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid


if __name__=='__main__':
    connection=get_sql_connection()




    '''print(insert_new_products(connection, {

        'products_name':'cabbage',
        'uom_id':'1',
        'price_per_unit':'10'
    }))''' # It will be used for inserting values in  database

    #print(delete_products(connection,14))
