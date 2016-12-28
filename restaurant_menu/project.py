from flask import Flask, flash, jsonify, render_template, redirect, request, url_for
app = Flask(__name__)

from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants')
def restaurantList():
    restaurants = session.query(Restaurant).all()
    return render_template(
        'restaurants.html',
        restaurants=restaurants)

@app.route('/restaurant/new', methods=['GET', 'POST'])
def restaurantNew():
    if request.method == 'POST':
        newRestaurant = Restaurant(name = request.form['name'])
        session.add(newRestaurant)
        session.commit()
        flash('Restaurant added')
        return redirect(url_for('restaurantList'))
    else:
        return render_template('new_restaurant.html')

@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def restaurantEdit(restaurant_id):
    editedItem = session.query(Restaurant).filter_by(id = restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        session.add(editedItem)
        session.commit()
        flash('Restaurant edited')
        return redirect(url_for('restaurantList', restaurant_id=restaurant_id))
    else:
        return render_template(
            'edit_restaurant.html',
            restaurant_id = restaurant_id,
            item = editedItem)

@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def restaurantDelete(restaurant_id):
    deletedItem = session.query(Restaurant).filter_by(id = restaurant_id).one()
    if request.method == 'POST':
        session.delete(deletedItem)
        session.commit()
        flash('Restaurant deleted')
        return redirect(url_for('restaurantList'))
    else:
        return render_template('delete_restaurant.html',
                               restaurant_id = restaurant_id,
                               item = deletedItem)

@app.route('/restaurant/<int:restaurant_id>/menu')
@app.route('/restaurant/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    return render_template(
        'menu.html',
        restaurant=restaurant,
        items=items)

@app.route('/restaurant/<int:restaurant_id>/create', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(
            name = request.form['name'],
            price = request.form['price'],
            course = request.form['course'],
            description = request.form['description'],
            restaurant_id = restaurant_id)
        session.add(newItem)
        session.commit()
        flash('Menu item added')
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('new_menu_item.html', restaurant_id = restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['course']:
            editedItem.course = request.form['course']
        if request.form['description']:
            editedItem.description = request.form['description']
        session.add(editedItem)
        session.commit()
        flash('Menu item edited')
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template(
            'edit_menu_item.html',
            restaurant_id = restaurant_id,
            menu_id = menu_id,
            item = editedItem)

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    deletedItem = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        session.delete(deletedItem)
        session.commit()
        flash('Menu item deleted')
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('delete_menu_item.html',
                               restaurant_id = restaurant_id,
                               menu_id = menu_id,
                               item = deletedItem)

if __name__ == '__main__':
    app.secret_key = 'Super secret'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
