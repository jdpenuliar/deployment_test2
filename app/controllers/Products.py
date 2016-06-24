from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        
        self.load_model('Product')
        self.db = self._app.db
   
    def index(self):
        products = self.models['Product'].retrieve_all_products()
        return self.load_view('/products/index.html', products=products)
    def new(self):
        return self.load_view('/products/new.html')
    def edit(self, id):
        print id
        products = self.models['Product'].retrieve_product(id)
        
        print products
        return self.load_view('/products/edit.html',products=products)
    def show(self, id):
        products = self.models['Product'].retrieve_product(id)
        return self.load_view('/products/show.html',products=products)

    def create(self):
        print request.form['name']
        print request.form['description']
        print request.form['price']
        # product_info_dictionary = {
        #     'name': request.form['name'],
        #     'description': request.form['description'],
        #     'price': request.form['price']
        # }
        result = self.models['Product'].create_products(request.form)
        if result['result'] == True:
            return redirect('/products')
        else:
            #flash messages
            print result['errors']['priceError']
            flash(result['errors']['priceError'],'priceError')
            return redirect('/products/new')
    def destroy(self,id):
        self.models['Product'].delete_product(id)
        return redirect('/products')
    def update(self,id):
        print id
        product_update_info_dictionary = {
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price']
        }
        result = self.models['Product'].update_product(id,product_update_info_dictionary)
        print 'alsdkfja;lsdkfja;sdlfkasdf', result
        if result['result'] == True:
            return redirect('/products')
        else:
            #flash messages
            print result['errors']['priceError']
            flash(result['errors']['priceError'],'priceError')
            return redirect('/products/edit/'+id)