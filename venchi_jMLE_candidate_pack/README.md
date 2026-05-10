# FarmCorp — Machine Learning Engineer Assessment

### Context
FarmCorp is a manufacturer of agricultural supplies that sells to large commercial farms, family farms and hobbyists alike. 
FarmCorp's IT department have shared data from different areas of the business (sales, marketing, etc) and the management team wants to leverage this data to make smarter, data-driven decisions about sales strategy and customer management.

### Task

As a Machine Learning Engineer, your task is to use the available data to help FarmCorp's sales team **better understand their customers and improve sales performance**. 

Your work is split into two parts.

#### Part 1 — Data Preparation & KPI Engineering
Build a **customer-level analytical dataset** by joining and cleaning the available data sources. Compute at least **4 KPIs or measures** per customer.

Two of them must be:
1. Total revenue generated (purchases × product price)
2. Number of sales interactions in the last 6 months

The other two are up to you — choose metrics you believe are useful for the following analyses.

---

#### Part 2 — Model Implementation: Customer Segmentation

FarmCorp's management believes data can do more than describe the past — it can guide future action. 
FarmCorp's sales director has asked: **"We treat all customers the same, but they clearly aren't. Can you identify distinct customer segments so we can tailor our approach?"**

Using the dataset you built in Part 1:
1. Apply a clustering algorithm to segment customers
2. Determine and justify the number of clusters
3. Describe each segment in business terms (who are they? what do they buy? how loyal are they?)
4. Suggest a **concrete sales action** for each segment (e.g. "Increase face-to-face visits for segment X")
5. Save an accounts_enriched.parquet file containing the original dataset plus the column describing the segment.

### Requirements
In the hope of creating a lasting contribution to FarmCorp that can be trusted, you should consider the following key criteria:
- The submission must be in Python/PySpark (please limit any other language like SQL)
- Use any ML library you prefer
- Document the code and comment your reasoning

### Useful information
- Be aware there are errors in the data because some fields are free text or not mandatory
- Documentation on the data available can be found in `data/README.md`