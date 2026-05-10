# FarmCorp Data Documentation

This document outlines the data supplied by FarmCorp's IT department. 

## accounts.parquet
This is a record of the customers of FarmCorp extracted from the CRM system. 

| Column  | Type  | Description  |
|---|---|---|
| account_id | string | An ID to identify the customer.  |
| hct | int | The size of the customer's farm. |
| staff | int | The number of people the customer employs. |
| turnover_m_usd | int| The total annual revenue of the customer in millions of USD. |
| brand_loyalty | int | A sales rep estimate of the customer's brand loyalty out of ten. |

## interactions.parquet
This is a record of the interactions FarmCorp's sales reps have had with customers. This data is extracted from the CRM system.

| Column  | Type  | Description  |
|---|---|---|
| interaction_id  | string  | An ID to identify the interaction.  |
| channel  | string  | How the interaction occured (e.g. over the phone, face to face, or over a web call).  |
| duration_mins | int  | The duration of the call in minutes. |
| response  | string  | A record of how the customer responded to the interaction as perceived by the sales rep (positive, negative or mixed).  |
| topic  | string  | What the subject of the interaction was. |
| date  | date  | The date of the interaction.  |
| account_id  | string | The customer that the interaction was with. |
| product_id  | string  |  The product that the interaction was about. |

## products.txt
This is a record of the products offered by FarmCorp and is extracted from the order system. 

| Column  | Type  | Description  |
|---|---|---|
| product_id  | string  | An ID to identify the product.  |
| maturity  | string  | How long the product has been on the market (new or established).  |
| price | int  | The price in USD. |
| category  | string | The type of product. |
| patent_id | int | Which patent the product is related to. |

## sales.parquet
This table is a log of the sales of products to accounts and is extracted from the order system. 

| Column  | Type  | Description  |
|---|---|---|
| sale_id | string  | An ID to identify the sale. |
| date | date | The date of the sale. |
| account_id | string | The account_id of the customer that purchased the product.  |
| product_id | string | The product_id of the product that was purchased.  |
