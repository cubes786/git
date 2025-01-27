IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name=N'BookSelling')
BEGIN
	EXEC('CREATE SCHEMA BookSelling;');
END;

IF NOT EXISTS(SELECT * FROM sys.objects WHERE object_id=OBJECT_ID(N'BookSelling.Books') AND type in (N'U'))
BEGIN
	CREATE TABLE BookSelling.Books(
		id INT PRIMARY KEY IDENTITY(1,1),
		title NVARCHAR(255) NOT NULL,
		author NVARCHAR(255)  NOT NULL,
		isbn NVARCHAR(20),
		price DECIMAL(10,2) NOT NULL,
		imageUrl NVARCHAR(255)
	);
END;

IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'BookSelling.Users') AND type in (N'U'))
BEGIN
  CREATE TABLE BookSelling.Users (
      id INT PRIMARY KEY IDENTITY(1,1),
      username VARCHAR(255) NOT NULL UNIQUE,
      password VARCHAR(255) NOT NULL,
      address VARCHAR(255),
      contactDetails VARCHAR(255)
  );
END;

-- Orders Table (modified to include payment status and transaction details)
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'BookSelling.Orders') AND type in (N'U'))
BEGIN
    CREATE TABLE BookSelling.Orders (
        id INT PRIMARY KEY IDENTITY(1,1),
        userId INT NOT NULL,
        orderDate DATETIME NOT NULL,
        orderStatus VARCHAR(50) NOT NULL,
        paymentStatus VARCHAR(50),  -- New column for payment status (e.g., 'pending', 'paid', 'failed')
        totalAmount DECIMAL(10,2) NOT NULL,  -- Total amount for the order
        FOREIGN KEY (userId) REFERENCES BookSelling.Users(id)
    );
END;

IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'BookSelling.OrderItems') AND type in (N'U'))
BEGIN
    CREATE TABLE BookSelling.OrderItems (
      id INT PRIMARY KEY IDENTITY(1,1),
      orderId INT NOT NULL,
      bookId INT NOT NULL,
      quantity INT NOT NULL,
      FOREIGN KEY (orderId) REFERENCES BookSelling.Orders(id),
      FOREIGN KEY (bookId) REFERENCES BookSelling.Books(id)
    );
END;

-- Payments Table (new table to store detailed payment information)
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'BookSelling.Payments') AND type in (N'U'))
BEGIN
    CREATE TABLE BookSelling.Payments (
        id INT PRIMARY KEY IDENTITY(1,1),
        orderId INT NOT NULL,
        transactionId NVARCHAR(255) NOT NULL,  -- Unique transaction ID from payment provider
        paymentMethod VARCHAR(50) NOT NULL,  -- Payment method (e.g., 'Stripe', 'PayPal')
        paymentDate DATETIME NOT NULL,  -- Date and time of payment
        amount DECIMAL(10,2) NOT NULL,  -- Amount paid
        paymentStatus VARCHAR(50),  -- Status of the payment (e.g., 'successful', 'failed', 'pending')
        FOREIGN KEY (orderId) REFERENCES BookSelling.Orders(id)
    );
END;