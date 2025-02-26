/****** Object:  StoredProcedure [dbo].[GetYieldData]    Script Date: 2/12/2024 6:14:21 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[GetYieldData]
	@StartDate DATE,
    @EndDate DATE,
    @Values NVARCHAR(10),
    @BEY BIT = 1 --Type of Yield column - BEY vs Discount yield
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @DiscountColumn NVARCHAR(50) = @Values + '_Discount';
    DECLARE @BEYColumn NVARCHAR(50) = @Values + '_BEY';
    DECLARE @StartDateString NVARCHAR(10) = CONVERT(VARCHAR, @StartDate, 23);
    DECLARE @EndDateString NVARCHAR(10) = CONVERT(VARCHAR, @EndDate, 23);

    IF @BEY = 1
    BEGIN
		EXEC('SELECT [Date], CAST([' + @BEYColumn + '] AS DECIMAL(18, 10)) AS Yield FROM dbo.yielddata WHERE [Date] BETWEEN ''' + @StartDateString + ''' AND ''' + @EndDateString + ''' ORDER BY [Date]');
    END
    ELSE
    BEGIN
        EXEC('SELECT [Date], CAST([' + @DiscountColumn + '] AS DECIMAL(18, 10)) AS Yield FROM dbo.yielddata WHERE [Date] BETWEEN ''' + @StartDateString + ''' AND ''' + @EndDateString + ''' ORDER BY [Date]');
    END
END

--for testing run - EXEC dbo.GetYieldData @Values = '4W', @StartDate = '2022-04-18', @EndDate = '2022-05-19'
