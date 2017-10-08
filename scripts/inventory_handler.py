#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import sqlite3

categories = [
    "スペクトラム・アナライザ",
    "クロスドメイン・アナライザ",
    "光パワーメータ",
    "光スペクトラム・アナライザ",
    "ネットワーク・アナライザ",
    "FFTアナライザ",
]

brands = [
    "ADVANTEST",
    "AGILENT",
    "ANRITSU",
]



def verify(conn):
    c = conn.cursor()
    sql = """
        select * from products_product
    """
    c.execute(sql)
    results = c.fetchall()
    for r in results:
        print(r)


def get_category_id(in_data):
    for index, category in enumerate(categories):
        if in_data == category:
            return index + 1

    return 1


def get_brand_id(in_data):
    for index, brand in enumerate(brands):
        if in_data == brand:
            return index + 1

    return 1


def get_inventory_status(in_data):
    if in_data == "在庫有":
        return "In Stock"
    elif in_data == "在庫無":
        return "Out Of Stock"

    return "Need To Confirm"


def update_category(conn):
    # https://qiita.com/mas9612/items/a881e9f14d20ee1c0703
    sql = """
    insert into products_category 
        (category_text) values (?)
    """

    c = conn.cursor()
    for category in categories:
        c.execute(sql, (category,))


def update_brand(conn):
    # https://qiita.com/mas9612/items/a881e9f14d20ee1c0703
    sql = """
    insert into products_brand 
        (brand_text) values (?)
    """

    c = conn.cursor()
    for brand in brands:
        c.execute(sql, (brand,))


def update_product(conn, df):
    # https://qiita.com/mas9612/items/a881e9f14d20ee1c0703
    sql = """
    insert into products_product 
        (product_text,
         measurable_range,
         option,
         serial_number,
         rank,
         year_of_manufacture,
         price,
         description,
         inventory_status,
         brand_id,
         category_id) values (?,?,?,?,?,?,?,?,?,?,?)
    """

    c = conn.cursor()
    for key, values in df.iterrows():

        product = (
            values[0],  # product_text
            values[3],  # measurable_range
            values[4],  # option
            values[8],  # serial_number
            values[6],  # rank
            values[5],  # year_of_manufacture
            values[7],  # price
            values[11], # description
            get_inventory_status(values[12]), # inventory_status
            get_brand_id(values[1]), # brand_id
            get_category_id(values[2]), # category_id
        )
        c.execute(sql, product)



if __name__ == '__main__':
    excel_file = "../../tomoca_inventory.xlsx"
    database_file = "../project/db.sqlite3"

    df = pd.read_excel(excel_file)
    df = df.replace(np.nan, '-')

    conn = sqlite3.connect(database_file)

    # verify(conn)
    update_category(conn)
    update_brand(conn)
    update_product(conn, df)

    conn.commit()
    conn.close()

