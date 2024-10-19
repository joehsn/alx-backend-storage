-- A script that creates a trigger that resets the attribute valid_email only when the email has been changed.

DELIMITER ??

CREATE TRIGGER email_validation
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	-- Check if the email has been changed
	IF NEW.email <> OLD.email THEN
	-- Reset valid_email to 0 if email is changed
	SET NEW.valid_email = 0;
	END IF;

END ??

DELIMITER ;
