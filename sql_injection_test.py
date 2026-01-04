import sqlite3
from flask import request

def get_user_by_id(user_id):
    """Fetch user from database - SQL injection vulnerability"""
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    
    # CRITICAL SECURITY ISSUE: Direct string interpolation
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    
    result = cursor.fetchone()
    conn.close()
    return result

def search_products(search_term):
    """Search products - another SQL injection"""
    conn = sqlite3.connect('app.db')
    
    # CRITICAL: Using string formatting with user input
    sql = "SELECT * FROM products WHERE name LIKE '%" + search_term + "%'"
    cursor = conn.cursor()
    cursor.execute(sql)
    
    products = cursor.fetchall()
    conn.close()
    return products
