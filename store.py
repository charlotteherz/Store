from bottle import run, template, static_file, get, post, delete, request
import json
import pymysql

connection = pymysql.connect(host = "localhost",
                             user = "root",
                             password = "francesca2",
                             db="store",
                             charset="utf8",
                             cursorclass = pymysql.cursors.DictCursor)

cursor = connection.cursor()

@get("/admin")
def admin_portal():
    return template("pages/admin.html")

@post("/category")
def create_category():
    try:
        with connection.cursor() as cursor:
            name = request.POST.get("name")
            sql = "INSERT INTO category VALUES (0,'{}')".format(name)
            cursor.execute(sql)
            connection.commit()
            result = cursor.fetchall()
            return json.dumps({'STATUS':'SUCCESS','MSG':result,'CODE':201})

    except Exception as e:
        print (repr(e))
        return json.dumps({'STATUS':'ERROR','MSG':'INTERNAL ERROR'})

@post("/product")
def add_edit_product():
    try:
        with connection.cursor() as cursor:
            title = request.POST.get("title")
            price = request.POST.get("price")
            img_url = request.POST.get("img_url")
            category = request.POST.get("category")
            sql = "INSERT INTO product VALUES ('{0}','{1}','{2}','{3}',{4},'{5}',0)".format(category,price,title,img_url)
            cursor.execute(sql)
            connection.commit()
            result = cursor.fetchall()
            return json.dumps({'STATUS': 'SUCCESS', 'MSG':result, 'CODE': 200})

    except Exception as e:
        print repr(e)
        return json.dumps({'STATUS': 'ERROR', 'MSG': 'INTERNAL ERROR','CODE':500})

@delete("/category/<id>")
def delete_category(id):
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM category WHERE id = {}".format(id)
            cursor.execute(sql)
            connection.commit()
            return json.dumps({'STATUS': 'SUCCESS', 'CODE': 201})
    except Exception:
        return json.dumps({'STATUS': 'ERROR', 'MSG': 'Internal error', 'CODE': 500})

@delete("/product/<id>")
def delete_product(id):
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM product WHERE id = {}".format(id)
            cursor.execute(sql)
            connection.commit()
            return json.dumps({'STATUS': 'SUCCESS', 'CODE': 201})

    except Exception:
        return json.dumps({'STATUS': 'ERROR', 'MSG': 'Internal error', 'CODE': 500})

@get("/categories")
def list_category():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM category"
            cursor.execute(sql)
            result = cursor.fetchall()

            return json.dumps({'STATUS': 'SUCCESS', 'CATEGORIES': result, 'CODE': 200})

    except Exception:
        return json.dumps({'STATUS': 'ERROR', 'MSG': 'Internal error', 'CODE': 500})

@get("/products")
def list_products():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM product;"
            cursor.execute(sql)
            result = cursor.fetchall()

            return json.dumps({'STATUS': 'SUCCESS', 'PRODUCTS': result, 'CODE': 200})

    except Exception:
        return json.dumps({'STATUS': 'ERROR', 'MSG': 'Internal error', 'CODE': 500})

@get("/product/<id>")
def get_product(id):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM product WHERE id = '{}'".format(id)
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({'STATUS': 'SUCCESS', 'PRODUCTS': result, 'CODE': 200})

    except Exception as e:
        print (repr(e))
        return json.dumps({'STATUS': 'ERROR', 'MSG': 'Internal error', 'CODE': 500})

@get("/category/<id>/products")
def list_products_by_category(id):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM product WHERE category = '{}'".format(id)
            cursor.execute(sql)
            result = cursor.fetchall()

            return json.dumps({'STATUS': 'SUCCESS', 'PRODUCTS': result, 'CODE': 200})

    except Exception:
        return json.dumps({'STATUS': 'ERROR', 'MSG': 'Internal error', 'CODE': 500})

@get("/")
def index():
    return template("index.html")


@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')

def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()