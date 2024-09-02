from db.db_connections import create_connection
from db.create_tables import create_tables
from data.load_data import load_data
from db.insert_data import insert_covid_data, insert_vaccination_data
from db.queries import run_queries
# from visualizations.plot_data import plot_vaccination_rate

def main():
    conn = create_connection()
    
    # Create tables
    create_tables(conn)
    
    # Load and insert data
    data = load_data('data/Nashville Housing Data for Data Cleaning (1).csv')
    
    insert_covid_data(conn, data)
    insert_vaccination_data(conn, vaccination_data)
    table_name = 'PropertySales'
    
    # Run queries and visualize
    # # Standardize date format
    #### Step 1
    # query = '''
    #     SELECT saledate, CAST(saledate as DATE) as formated_date
    #     FROM PropertySales 
    #     order by saledate
    # '''


    # # change table to create new one to update date column
    #### Step 2
    # query = '''
    #      ALTER TABLE PropertySales
    #      ADD COLUMN convertedsaledate DATE
    # '''
    # # update date column to new formated column
    # query = '''
    #      UPDATE PropertySales
    #     set convertedsaledate = CAST(saledate as DATE)
    # '''
    # And then retrieve data from table with first query


    # # Populate property address data
    # # if one parcelid have address and another did not have, populate them (duplicate parcelid)
    # query = '''
    #     SELECT a.parcelid, a.propertyaddress AS address_a, b.parcelid, b.propertyaddress AS address_b, 
    #            COALESCE(a.propertyaddress, b.propertyaddress) AS combined_address
    #     FROM PropertySales AS a
    #     JOIN PropertySales AS b
    #     ON a.parcelid = b.parcelid
    #     AND a.uniqueid <> b.uniqueid
    #     WHERE a.propertyaddress IS NULL OR b.propertyaddress = 'NaN'
        
    #     ORDER BY a.parcelid
    # '''

    # # update table with populated column
    # query = '''
    #     UPDATE PropertySales AS a
    #     SET propertyaddress = COALESCE(a.propertyaddress, b.propertyaddress)
    #     FROM PropertySales AS b
    #     WHERE a.parcelid = b.parcelid
    #     AND a.uniqueid <> b.uniqueid
    #     AND (a.propertyaddress IS NULL OR b.propertyaddress = 'NaN')
    # '''


    # # Breaking out address into individual columns(Address, City, State)
    # query = '''
    #    SELECT
    #     TRIM(SPLIT_PART(propertyaddress, ',', 1)) AS ADDRESS,
    #     TRIM(SPLIT_PART(propertyaddress, ',', 2)) AS CITY,
    #     TRIM(SPLIT_PART(propertyaddress, ',', 3)) AS STATE
    #     FROM
    #         PropertySales;
    # '''
    # query = '''
    #      ALTER TABLE PropertySales
    #      ADD COLUMN ADDRESS VARCHAR(255)
    # '''
    # query = '''
    #      ALTER TABLE PropertySales
    #      ADD COLUMN CITY VARCHAR(255)
    # '''
    # # update date column to new formated column
    # query = '''
    #      UPDATE PropertySales
    #     set ADDRESS = TRIM(SPLIT_PART(propertyaddress, ',', 1)) 
    # '''

    # query = '''
    #      UPDATE PropertySales
    #     set CITY = TRIM(SPLIT_PART(propertyaddress, ',', 2)) 
    # '''

    # # knowing distinct values of a column
    # query = '''
    #     SELECT Distinct(soldasvacant), Count(soldasvacant)
    #     FROM PropertySales
    #     Group BY soldasvacant
    #     order by soldasvacant
    # '''


    # # change Y and N to Yes and No in 'Sold as vacant' and update main colum
    # query = '''
    #     SELECT
    #     CASE 
    #     WHEN soldasvacant = 'False' THEN 'NO'
    #     WHEN soldasvacant = 'True' THEN 'YES'
    #     ELSE 'UNKNOWN'
    #     END AS modified_soldasvacant
    #     FROM PropertySales
    # '''

    # # update soldasvacant column to new modified_soldasvacant column
    # # step 1: should change column type to varchar
    # query = '''
    #     ALTER TABLE PropertySales 
    #     ADD COLUMN modified_soldasvacant VARCHAR;
    # '''

    # # Step2: assign modified value to soldasvacant column
    # query = '''
    #     UPDATE PropertySales
    #     SET modified_soldasvacant = CASE 
    #         WHEN soldasvacant = 'true' THEN 'YES'   
    #         WHEN soldasvacant = 'false' THEN 'NO'   
    #         ELSE 'UNKNOWN'                        
    #     END
    # '''

    # # Show duplicates
    # query = ''' WITH ROWNumCTE AS (
    #     SELECT * , ROW_NUMBER() OVER (
    #         Partition by parcelid,
    #                      propertyaddress,
    #                      saleprice,
    #                      saledate,
    #                      legalreference
    #         order by uniqueid
    #         )
    #         row_num
    #     FROM PropertySales
    #     --order by parcelid
    # ) 

    #     SELECT * FROM ROWNumCTE
    #     WHERE row_num > 1
    #     order by propertyaddress
                         
    # '''

    # # remove duplicates
    # query = '''
    # DELETE FROM PropertySales
    # WHERE uniqueid IN (
    #     SELECT uniqueid
    #     FROM (
    #         SELECT uniqueid,
    #                ROW_NUMBER() OVER (
    #                    PARTITION BY parcelid,
    #                                 propertyaddress,
    #                                 saleprice,
    #                                 saledate,
    #                                 legalreference
    #                    ORDER BY uniqueid
    #                ) AS row_num
    #         FROM PropertySales
    #     ) AS subquery
    #     WHERE row_num > 1
    # );
    # '''

    # # remove unecessary columns
    # query = '''
    #     ALTER TABLE PropertySales
    #     DROP COLUMN parcelid
    # '''
    db_data = run_queries(query, conn)
    if not db_data.empty:
        # Proceed with data processing or visualization
        print(db_data.head())
    else:
        print("No data retrieved.")
    
    # plot_vaccination_rate(db_data)
    

if __name__ == "__main__":
    main()
