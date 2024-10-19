-- A script that creates a trigger that decreases the quantity of an item after adding a new order.

DELIMITER ??

CREATE TRIGGER quantity_reduce
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	-- Update the quantity of the item in the items table
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;

END ??
DELIMITER ;
