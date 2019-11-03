CREATE DATABASE IF NOT EXISTS stocks;
USE stocks;
CREATE TABLE IF NOT EXISTS stocks (
	             id VARCHAR(15) PRIMARY KEY,
        	     symbol VARCHAR(6),
                     date DATE,
                     open REAL,
                     high REAL,
                     low REAL,
                     close REAL,
                     adjusted_close REAL,
                     volume BIGINT,
                     dividend_amount REAL,
                     split_coefficient REAL
		    );
