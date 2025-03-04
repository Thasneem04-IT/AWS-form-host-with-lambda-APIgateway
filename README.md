# **AWS API Gateway Form Submission with DynamoDB**  

This project demonstrates how to use **AWS API Gateway**, **Lambda**, and **DynamoDB** to handle form submissions from a static website hosted on **Amazon S3**.  

## **Project Overview**  
- A simple **HTML form** allows users to submit their name and email.  
- The form data is sent to an **AWS API Gateway endpoint**, which triggers a **Lambda function**.  
- The **Lambda function** processes the request and stores the data in **DynamoDB**.  

---

## **Architecture**  
1. **Frontend**: Static web page (HTML, CSS, JavaScript) hosted on an **S3 bucket**.  
2. **API Gateway**: Receives HTTP requests and forwards them to Lambda.  
3. **Lambda Function**: Processes form data and stores it in DynamoDB.  
4. **DynamoDB**: Stores submitted form data persistently.  

---

## **Setup and Deployment**  

### **Step 1: Host the Frontend on S3**  
1. Go to the **AWS S3 Console** → Create a new bucket.  
2. Enable **static website hosting**.  
3. Upload `index.html`, `styles.css`, and `script.js`.  
4. Make the files **public** and copy the S3 website URL.  

---

### **Step 2: Create DynamoDB Table**  
1. Go to **AWS DynamoDB Console**.  
2. Click **Create Table**.  
3. Table name: `gateway_table`.  
4. Partition Key: `id` (String).  
5. Click **Create Table**.  

---

### **Step 3: Create a Lambda Function**  
1. Go to **AWS Lambda Console**.  
2. Click **Create Function** → **Author from scratch**.  
3. Function name: `submitFormFunction`.  
4. Runtime: **Python 3.9+**.  
5. Under **Permissions**, attach the **AmazonDynamoDBFullAccess** policy.  
6. Upload `lambda_function.py` code.  
7. Click **Deploy**.  

---

### **Step 4: Create API Gateway**  
1. Go to **AWS API Gateway Console**.  
2. Click **Create API** → Choose **HTTP API**.  
3. Set a **POST method** for the route `/submit-form`.  
4. Integrate it with the **Lambda function** (`submitFormFunction`).  
5. Deploy the API and note the **Invoke URL**.  

---

### **Step 5: Connect API Gateway to Frontend**  
1. Replace the API URL in `script.js`:  

   ```javascript
   const response = await fetch("https://your-api-id.execute-api.region.amazonaws.com/prod/submit-form", {
   ```

2. Re-upload `script.js` to the S3 bucket.  

---

## **Testing the Application**  
1. Open the **S3 website URL** in a browser.  
2. Enter name and email, then click **Submit**.  
3. Check **DynamoDB** to confirm the data is stored.  

---
