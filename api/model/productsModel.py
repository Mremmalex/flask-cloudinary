cursor, mydb

query = """  CREATE TABLE IF NOT EXISTS `products`
( productID INT AUTO_INCREMENT, 
productName VARCHAR(200),
productImage VARCHAR(255),
 productDesc TEXT, 
productPrice INT, 
PRIMARY KEY (productID)) """

cursor.execute(query)
mydb.commit()


class Products:

    def __init__(self):
        self.db = cursor

    def newProduct(self, productName, productImg, productDesc, productPrice):
        query = "INSERT INTO products (productName,productImage,productDesc, productPrice) VALUES(%s, %s, %s, %s)"
        val = (productName, productImg, productDesc, productPrice)
        cursor.execute(query, val)
        mydb.commit()

    def getAllProducts(self):
        cursor.execute("SELECT * FROM products")
        result = cursor.fetchall()
        return result


productTable = Products()
