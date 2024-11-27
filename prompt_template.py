

features= """ 
You are an AI designed to transform client ideas or RFPs into a list of features. Given a client idea or RFP, generate a comprehensive list of features that describe the functionalities and capabilities of the proposed system.
Client Idea/RFP:
{client_idea}

Generated Features:
Just output only the generated features

Example:

Client Idea/RFP:
An online CRM tool that centralizes customer information, streamlines sales processes, and facilitates marketing efforts. It simplifies user interactions through an intuitive interface, incorporates real-time data visualizations, and predictive modeling to anticipate customer needs, with easy integration options for various platforms.

Generated Features :

1. Centralized customer information database
2. Streamlined sales process management
3. Marketing campaign management
4. Intuitive user interface
5. Real-time data visualizations
6. Predictive modeling for customer needs
7. Integration with various platforms
8. Import customer data from CSV files
9. Connect to external databases
10. Integrate with third-party applications
11. Create custom fields for customer data
12. Group customers into segments

"""

user_stories=""" 

You are an AI designed to transform a list of features into detailed user stories with descriptions. Given a list of features, generate user stories that describe the functionalities and benefits of each feature. Each user story should include a title and a description that follows the format: "As a [user role], I want to [goal] so that [reason]."

Input Features:
{features}

Generated User Stories:
Output the generated User Stories in a table format

| **User Story Title** | **User Story Description** |
|----------------------|----------------------------|
| Import customer data from CSV files | As a sales representative, I want to be able to import customer data from CSV files so that I can easily populate the CRM with existing customer information. |
| Connect to external databases | As a CRM administrator, I want to connect the CRM to external databases so that I can automatically sync customer information and keep it up to date. |
| Integrate with third-party applications | As a marketing manager, I want to integrate the CRM with third-party applications like email marketing tools and social media platforms so that I can have a comprehensive view of customer interactions across different channels. |
| Create custom fields | As a CRM administrator, I want to be able to create custom fields for customer data so that I can capture specific information that is relevant to our business. |

"""

backlog=""" 
You are an AI designed to organize features and user stories into a final backlog. Given a list of features and their corresponding user stories, generate a prioritized backlog that outlines the tasks for development. Each backlog item should include a title, description, priority level, and any dependencies.

Input Features and User Stories:
{user_stories}

Generated Backlog:
Output the generated backlog in a table format

Example of Generated Backlog:
| **Backlog Item** | **Description** | **Priority** | **Dependencies** |
|------------------|-----------------|--------------|------------------|
| Import customer data from CSV files | As a sales representative, I want to be able to import customer data from CSV files so that I can easily populate the CRM with existing customer information. | High | None |
| Connect to external databases | As a CRM administrator, I want to connect the CRM to external databases so that I can automatically sync customer information and keep it up to date. | High | None |
| Integrate with third-party applications | As a marketing manager, I want to integrate the CRM with third-party applications like email marketing tools and social media platforms so that I can have a comprehensive view of customer interactions across different channels. | Medium | Connect to external databases |
| Create custom fields | As a CRM administrator, I want to be able to create custom fields for customer data so that I can capture specific information that is relevant to our business. | Medium | None |

"""

api_specification="""
You are an AI designed to create API specifications from a backlog of features and user stories. Given a prioritized backlog, generate detailed API specifications for each feature. Each API specification should include the endpoint, HTTP method, request parameters, response format, and any necessary authentication details.

Input Backlog:
{backlog}

Generated API Specifications:

Example of Generated API Specifications:
1. **Feature: Import customer data from CSV files**
   - **Endpoint:** `/api/customers/import`
   - **Method:** POST
   - **Request Parameters:**
     - `file`: (file) The CSV file containing customer data
   - **Response Format:**
     - `status`: (string) Success or error message
     - `importedRecords`: (integer) Number of records imported
   - **Authentication:** Required (Bearer token)

2. **Feature: Connect to external databases**
   - **Endpoint:** `/api/databases/connect`
   - **Method:** POST
   - **Request Parameters:**
     - `databaseUrl`: (string) URL of the external database
     - `credentials`: (object) Database access credentials
   - **Response Format:**
     - `status`: (string) Success or error message
     - `connectionId`: (string) Unique identifier for the connection
   - **Authentication:** Required (Bearer token) 

"""

technical_architecture="""
You are an AI designed to generate a proposed technical architecture from a backlog of features and user stories. Given a prioritized backlog, create a high-level technical architecture that outlines the system components, their interactions, and the technologies to be used.

Input Backlog:
{backlog}

Generated Technical Architecture:

1. **System Overview:**
   - **Description:** Provide a high-level overview of the system, including its main components and their interactions.

2. **Components:**
   - **Frontend:**
     - **Description:** The user interface of the system.
     - **Technologies:** React.js, Angular, or Vue.js
   - **Backend:**
     - **Description:** The server-side logic and database interactions.
     - **Technologies:** Node.js with Express, Django, or Spring Boot
   - **Database:**
     - **Description:** The storage system for customer data and other information.
     - **Technologies:** PostgreSQL, MySQL, or MongoDB
   - **API Layer:**
     - **Description:** The interface for communication between the frontend and backend.
     - **Technologies:** RESTful APIs, GraphQL
   - **Authentication:**
     - **Description:** The system for user authentication and authorization.
     - **Technologies:** OAuth 2.0, JWT (JSON Web Tokens)
   - **Integration Layer:**
     - **Description:** The system for integrating with third-party applications and external databases.
     - **Technologies:** Apache Camel, MuleSoft
   - **Data Visualization:**
     - **Description:** The system for real-time data visualizations and dashboards.
     - **Technologies:** D3.js, Chart.js, or Tableau
   - **Predictive Modeling:**
     - **Description:** The system for predictive analytics and customer need anticipation.
     - **Technologies:** Python with scikit-learn, TensorFlow, or PyTorch

3. **Interactions:**
   - **Frontend to Backend:**
     - **Description:** How the frontend communicates with the backend.
     - **Technologies:** HTTP/HTTPS, WebSockets
   - **Backend to Database:**
     - **Description:** How the backend interacts with the database.
     - **Technologies:** SQL queries, ORM (Object-Relational Mapping)
   - **API Layer to External Systems:**
     - **Description:** How the API layer integrates with third-party applications and external databases.
     - **Technologies:** RESTful APIs, Webhooks

4. **Security:**
   - **Description:** Measures to ensure the security of the system.
   - **Technologies:** SSL/TLS, Encryption, Firewalls

5. **Scalability:**
   - **Description:** Strategies to ensure the system can handle increased load.
   - **Technologies:** Load Balancers, Microservices Architecture, Kubernetes

6. **Monitoring and Logging:**
   - **Description:** Systems for monitoring performance and logging activities.
   - **Technologies:** Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana) 

"""

wireframes=""" 

You are an AI designed to create wireframes from a backlog of features and user stories. Given a prioritized backlog, generate wireframes that visually represent the user interface for each feature. Each wireframe should include key elements such as buttons, input fields, navigation menus, and any other relevant UI components.

Input Backlog:
{backlog}

Generated Wireframes:

1. **Feature: [Feature Title]**
   - **Wireframe Description:** Describe the main screen or page where this feature will be implemented. Include details about the layout and key UI components.
   - **Key Elements:** List the essential UI components such as buttons, input fields, tables, charts, etc.

2. **Feature: [Feature Title]**
   - **Wireframe Description:** Describe the main screen or page where this feature will be implemented. Include details about the layout and key UI components.
   - **Key Elements:** List the essential UI components such as buttons, input fields, tables, charts, etc.

3. **Feature: [Feature Title]**
   - **Wireframe Description:** Describe the main screen or page where this feature will be implemented. Include details about the layout and key UI components.
   - **Key Elements:** List the essential UI components such as buttons, input fields, tables, charts, etc.

4. **Feature: [Feature Title]**
   - **Wireframe Description:** Describe the main screen or page where this feature will be implemented. Include details about the layout and key UI components.
   - **Key Elements:** List the essential UI components such as buttons, input fields, tables, charts, etc.

5. **Feature: [Feature Title]**
   - **Wireframe Description:** Describe the main screen or page where this feature will be implemented. Include details about the layout and key UI components.
   - **Key Elements:** List the essential UI components such as buttons, input fields, tables, charts, etc.

6. **Feature: [Feature Title]**
   - **Wireframe Description:** Describe the main screen or page where this feature will be implemented. Include details about the layout and key UI components.
   - **Key Elements:** List the essential UI components such as buttons, input fields, tables, charts, etc.

7. **Feature: [Feature Title]**
   - **Wireframe Description:** Describe the main screen or page where this feature will be implemented. Include details about the layout and key UI components.
   - **Key Elements:** List the essential UI components such as buttons, input fields, tables, charts, etc.

8. **Feature: [Feature Title]**
   - **Wireframe Description:** Describe the main screen or page where this feature will be implemented. Include details about the layout and key UI components.
   - **Key Elements:** List the essential UI components such as buttons, input fields, tables, charts, etc.

9. **Feature: [Feature Title]**
   - **Wireframe Description:** Describe the main screen or page where this feature will be implemented. Include details about the layout and key UI components.
   - **Key Elements:** List the essential UI components such as buttons, input fields, tables, charts, etc.

"""

data_model=""" 
You are an AI designed to create a data model from a backlog of features and user stories. Given a prioritized backlog, generate a detailed data model that outlines the database structure, including tables, fields, data types, and relationships.

Input Backlog:
{backlog}

Generated Data Model:

1. **Tables and Fields:**
   - **Table: Customers**
     - **Fields:**
       - `customer_id` (Primary Key, Integer)
       - `first_name` (String)
       - `last_name` (String)
       - `email` (String)
       - `phone_number` (String)
       - `address` (String)
       - `created_at` (Timestamp)
       - `updated_at` (Timestamp)

   - **Table: Interactions**
     - **Fields:**
       - `interaction_id` (Primary Key, Integer)
       - `customer_id` (Foreign Key, Integer)
       - `interaction_type` (String)
       - `interaction_date` (Timestamp)
       - `notes` (Text)

   - **Table: Tags**
     - **Fields:**
       - `tag_id` (Primary Key, Integer)
       - `tag_name` (String)

   - **Table: CustomerTags**
     - **Fields:**
       - `customer_id` (Foreign Key, Integer)
       - `tag_id` (Foreign Key, Integer)

   - **Table: Segments**
     - **Fields:**
       - `segment_id` (Primary Key, Integer)
       - `segment_name` (String)
       - `criteria` (Text)

   - **Table: CustomerSegments**
     - **Fields:**
       - `customer_id` (Foreign Key, Integer)
       - `segment_id` (Foreign Key, Integer)

   - **Table: EngagementMetrics**
     - **Fields:**
       - `metric_id` (Primary Key, Integer)
       - `customer_id` (Foreign Key, Integer)
       - `metric_type` (String)
       - `metric_value` (Float)
       - `recorded_at` (Timestamp)

2. **Relationships:**
   - **Customers to Interactions:** One-to-Many (One customer can have multiple interactions)
   - **Customers to Tags:** Many-to-Many (One customer can have multiple tags and one tag can be assigned to multiple customers)
   - **Customers to Segments:** Many-to-Many (One customer can belong to multiple segments and one segment can include multiple customers)
   - **Customers to EngagementMetrics:** One-to-Many (One customer can have multiple engagement metrics) 

"""