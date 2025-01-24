-- Insert sample books (idempotent)
IF NOT EXISTS (SELECT 1 FROM BookSelling.Books WHERE isbn = '978-0345391803')
BEGIN
    INSERT INTO BookSelling.Books (title, author, isbn, price, imageUrl) VALUES
    ('The Hitchhiker''s Guide to the Galaxy', 'Douglas Adams', '978-0345391803', 10.99, 'https://m.media-amazon.com/images/I/517E3Y0S3GL._SL500_.jpg');
END;

IF NOT EXISTS (SELECT 1 FROM BookSelling.Books WHERE isbn = '978-0141439518')
BEGIN
   INSERT INTO BookSelling.Books (title, author, isbn, price, imageUrl) VALUES
   ('Pride and Prejudice', 'Jane Austen', '978-0141439518', 9.99, 'https://m.media-amazon.com/images/I/71Q1tPupKjL._SL500_.jpg');
END;

IF NOT EXISTS (SELECT 1 FROM BookSelling.Books WHERE isbn = '978-0439023481')
BEGIN
   INSERT INTO BookSelling.Books (title, author, isbn, price, imageUrl) VALUES
    ('The Hunger Games', 'Suzanne Collins', '978-0439023481', 12.50, 'https://m.media-amazon.com/images/I/71ws63807EL._SL500_.jpg');
END;

-- Insert sample users (idempotent)
IF NOT EXISTS (SELECT 1 FROM BookSelling.Users WHERE username = 'john.doe')
BEGIN
    INSERT INTO BookSelling.Users (username, password, address, contactDetails) VALUES
    ('john.doe', 'password123', '123 Main St', '555-1234');
END;


IF NOT EXISTS (SELECT 1 FROM BookSelling.Users WHERE username = 'jane.smith')
BEGIN
    INSERT INTO BookSelling.Users (username, password, address, contactDetails) VALUES
    ('jane.smith', 'securePass', '456 Oak Ave', '555-5678');
END;


-- Insert sample orders (idempotent)
-- Use a specific orderDate for deterministic results
DECLARE @orderDate1 DATETIME = '2024-01-20T10:00:00';
DECLARE @orderDate2 DATETIME = '2024-01-21T14:30:00';
IF NOT EXISTS (SELECT 1 FROM BookSelling.Orders WHERE userId = 1 AND orderDate = @orderDate1)
BEGIN
    INSERT INTO BookSelling.Orders (userId, orderDate, orderStatus)
    VALUES (1, @orderDate1, 'pending');
END;


IF NOT EXISTS (SELECT 1 FROM BookSelling.Orders WHERE userId = 2 AND orderDate = @orderDate2)
BEGIN
    INSERT INTO BookSelling.Orders (userId, orderDate, orderStatus)
    VALUES (2, @orderDate2, 'shipped');
END;


-- Insert sample order items (idempotent)
IF NOT EXISTS (SELECT 1 FROM BookSelling.OrderItems WHERE orderId = 1 AND bookId = 1)
BEGIN
    INSERT INTO BookSelling.OrderItems (orderId, bookId, quantity) VALUES (1, 1, 1);
END;
IF NOT EXISTS (SELECT 1 FROM BookSelling.OrderItems WHERE orderId = 1 AND bookId = 2)
BEGIN
  INSERT INTO BookSelling.OrderItems (orderId, bookId, quantity) VALUES (1, 2, 1);
END;

IF NOT EXISTS (SELECT 1 FROM BookSelling.OrderItems WHERE orderId = 2 AND bookId = 3)
BEGIN
   INSERT INTO BookSelling.OrderItems (orderId, bookId, quantity) VALUES (2, 3, 2);
END;