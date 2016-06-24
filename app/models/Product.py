from system.core.model import Model
import re
class Product(Model):
    def __init__(self):
        super(Product, self).__init__()

    def retrieve_all_products(self):
        get_all_products_query = 'SELECT * FROM products'
        get_all_products_result = self.db.query_db(get_all_products_query)
        return get_all_products_result

    def retrieve_product(self,id):
        get_product_query = 'SELECT * FROM products WHERE id = :id'
        get_product_data = {'id':id}
        get_product_result = self.db.query_db(get_product_query,get_product_data)
        return get_product_result

    def create_products(self, product_info_dictionary):
        print product_info_dictionary
        
        error_dictionary = {
            'priceError':''
        }
        errorCount = 0
        if not re.findall(r"[-+]?\d*\.\d+|\d+", product_info_dictionary['price']):
            error_dictionary['priceError']+='Price is incorect!\n'
            errorCount+=1

        if errorCount >0:
            return {'result':False, 'errors':error_dictionary}
        else:
            #insert query
            create_product_query = "INSERT INTO products (name, description, price, created_at, updated_at) VALUES (:name,:description, :price, NOW(), NOW())"
            create_product_data = {
                'name': product_info_dictionary['name'],
                'description': product_info_dictionary['description'],
                'price':product_info_dictionary['price']
            }
            self.db.query_db(create_product_query, create_product_data)
            
            return {'result':True, 'errors':None}
    def delete_product(self,id):
        delete_query = 'DELETE from products where id = :id'
        delete_data = {
            'id': id
        }
        self.db.query_db(delete_query,delete_data)
        return None
    def update_product(self,id,product_update_info_dictionary):
        print product_update_info_dictionary
        
        error_dictionary = {
            'priceError':''
        }
        errorCount = 0
        print errorCount
        print 'yo'
        print 'yo'
        print 'yo'
        print 'yo'
        print 'haha'
        print 'haha'
        print 'haha'
        print re.findall(r"[-+]?\d*\.\d+|\d+", product_update_info_dictionary['price'])
        if re.findall(r"[-+]?\d*\.\d+|\d+", product_update_info_dictionary['price']) == None:
            error_dictionary['priceError']+='Price is incorect!\n'
            errorCount+=1
        print errorCount
        if errorCount >0:
            return {'result':False, 'errors':error_dictionary}
        else:
            #insert query
            update_product_query = "UPDATE products SET name = :name, description = :description, price = :price WHERE id = :id"
            update_product_data = {
                'id': id,
                'name': product_update_info_dictionary['name'],
                'description': product_update_info_dictionary['description'],
                'price':product_update_info_dictionary['price']
            }
            self.db.query_db(update_product_query, update_product_data)
            error_dictionary['priceError']+=''
            return {'result':True, 'errors':error_dictionary}