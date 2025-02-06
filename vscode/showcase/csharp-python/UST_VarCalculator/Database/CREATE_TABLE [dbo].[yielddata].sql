

/****** Object:  Table [dbo].[yielddata]    Script Date: 2/12/2024 11:35:21 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[yielddata](
	[Date] [date] NOT NULL,
	[4W_Discount] [decimal](18, 10) NOT NULL,
	[4W_BEY] [decimal](18, 10) NOT NULL,
	[8W_Discount] [decimal](18, 10) NOT NULL,
	[8W_BEY] [decimal](18, 10) NOT NULL,
	[13W_Discount] [decimal](18, 10) NOT NULL,
	[13W_BEY] [decimal](18, 10) NOT NULL,
	[26W_Discount] [decimal](18, 10) NOT NULL,
	[26W_BEY] [decimal](18, 10) NOT NULL,
	[52W_Discount] [decimal](18, 10) NOT NULL,
	[52W_BEY] [decimal](18, 10) NOT NULL,
 CONSTRAINT [PK_yielddata2] PRIMARY KEY CLUSTERED 
(
	[Date] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


