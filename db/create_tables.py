def create_tables(conn):
    cursor = conn.cursor()
    
    tabel_query = '''CREATE TABLE IF NOT EXISTS PropertySales (
        UniqueID INT PRIMARY KEY,
        ParcelID VARCHAR(20),
        LandUse VARCHAR(50),
        PropertyAddress VARCHAR(255),
        SaleDate DATE,
        SalePrice DECIMAL(15, 2),
        LegalReference VARCHAR(50),
        SoldAsVacant BOOLEAN,
        OwnerName VARCHAR(100),
        OwnerAddress VARCHAR(255),
        Acreage DECIMAL(10, 2),
        TaxDistrict VARCHAR(100),
        LandValue DECIMAL(15, 2),
        BuildingValue DECIMAL(15, 2),
        TotalValue DECIMAL(15, 2),
        YearBuilt INT,
        Bedrooms INT,
        FullBath INT,
        HalfBath INT
    );
    
    '''
    cursor.execute(tabel_query)
    
   
    conn.commit()
