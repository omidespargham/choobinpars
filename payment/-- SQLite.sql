-- SQLite
-- SELECT DISTINCT accounts_user.id from accounts_user INNER JOIN products_product ON accounts_user.id = products_product.user_id

-- SELECT DISTINCT accounts_user.id from products_product INNER JOIN accounts_user ON accounts_user.id = products_product.user_id

SELECT products_repair.name from products_repair INNER JOIN products_category on products_repair.category_id = products_category.id where products_category.name = 'miz'