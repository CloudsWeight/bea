# BEA and Fed API Data Classes
BEA and New York Fed data grabbing classes to learn Data Analysis concepts.

![image](https://github.com/user-attachments/assets/cca5a524-c8f5-436e-8c7d-8ac7e9892704)

# Fed API 
- fxs() = function to get swap data, takes 3 args, start date, end date, country
- plot() - creates a plot using date_time, interest_rate, and country data
- get() - a simple get function for returning JSON from the API endpoints
- lists() = translates fxs data into list for x and y axis data with the country counterpart (only tested on fxs data)
Fed API

Agency Mortgage-Backend Securites Operations
/api/fxs/{operationType}/search.{format}
/api/ambs/{operation}/results/{include}/lastTwoWeeks.{format}
/api/ambs/{operation}/results/{include}/last/{number}.{format}
/api/ambs/{operation}/results/{include}/search.{format}

CB Liquidity Swaps
/api/fxs/{operationType}/latest.{format}
/api/fxs/{operationType}/last/{number}.{format}'
/api/fxs/{operationType}/search.{format}
/api/fxs/{operationType}/search.{format}

Guide Sheets
/api/guidesheets/{guideSheettypes}/latest.json
/api/guidesheets/{guidesheetType}/previous.{format}

![image](https://github.com/user-attachments/assets/b3437e4f-eec7-4361-a76d-ea0fcd310094)
