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

IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'BookSelling.Orders') AND type in (N'U'))
BEGIN
    CREATE TABLE BookSelling.Orders (
        id INT PRIMARY KEY IDENTITY(1,1),
        userId INT NOT NULL,
        orderDate DATETIME NOT NULL,
        orderStatus VARCHAR(50) NOT NULL,
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