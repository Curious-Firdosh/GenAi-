from fastapi import FastAPI , Depends
from service.products import get_all_products
from model import ProductCreate,UpdateProduct
from db import SessionLocal, engine
from database_model import Base, Product
from sqlalchemy.orm import Session

Base.metadata.create_all(bind = engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except ConnectionRefusedError:
        " Db Not Connected"
    finally:
        db.close()


#! Static Route
@app.get("/")
def root():
    return{
        "message" : "Welcome To Fast Api "
    }
    

@app.get('/products')
def get_all_products(db:Session = Depends(get_db)):
    count = db.query(Product).count()
    products = db.query(Product).all()
    
    return{
       "count" : count,
       "products" : products
    }
 
@app.post('/product')
def get_products(product :ProductCreate , db : Session = Depends(get_db)):
    new_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock
    )
    
    db.add(new_product)
    db.commit()
    
    db.refresh(new_product)
    
    return new_product
  
  
@app.get('/product/{id}')
def get_single_product(id :int , db : Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    db.commit();
    if product:
        return product
    return []


@app.put('/product{id}')
def update_product (id : int , product : UpdateProduct ,  db : Session = Depends(get_db) ):
    db_product = db.query(Product).filter(Product.id == id).first()
    
    if db_product :
        if product.name is not None:
             db_product.name = product.name
        if product.price is not None:
            db_product.price = product.price
        if product.stock >= 0 :
            db_product.stock = product.stock
        if product.description is not None:
             db_product.description = product.description
       
        db.commit();
        return "Product Updated Successfully"
    else :
        return "Product Not Found"

@app.delete("/product/{id}")
def delete_product(id : int , db : Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    else :
        return "Product not Found"
    return {
        "message" : "Delted SuccessFully"
    }

