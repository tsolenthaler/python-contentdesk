import service.debug as debug

def filter(products, attribute): 
    #attribute = "openingHoursSpecification"
    productsUpdated = []
    for product in products:
        if attribute in product["values"]:
            productsUpdated.append(product)
    return productsUpdated

def skuList(products, attribute):
    skuList = {}
    for product in products:
        if attribute in product["values"]:
            skuList[product["identifier"]] = {}
            skuList[product["identifier"]] = product["values"][attribute][0]["data"]
        else:
            skuList[product["identifier"]] = {}
    return skuList

def uuidList(products):
    uuidList = []
    for product in products:
        uuidList.append(product["uuid"])
    return uuidList

def main(environment, target, attributes):
    for attribute in attributes:
        print("START Export PRODUCTS for: ", attribute)
        #migration = importMigrationSettings(attribute)
        print("Get all Products")
        products = target.getProducts()
        debug.addToFileExportFull(environment, 'attribute', attribute, 'products', products)
        print("Filter Products")
        productsTranform = filter(products, attribute)
        debug.addToFileExportFull(environment, 'attribute', attribute, 'transform', productsTranform)
        
        productsSku = skuList(productsTranform, attribute)
        debug.addToFileExportFull(environment, 'attribute', attribute, 'sku', productsSku)
        
        productsUuid = uuidList(productsTranform)
        debug.addToFileExportFull(environment, 'attribute', attribute, 'uuid', productsUuid)
        
        # Stop for Export
        #print("Upload Products")
        #productsUpload = migration.uploadProducts(target, productsTranform)
        #print("FINISH PATCH PRODUCTS for: ", attribute)
        
