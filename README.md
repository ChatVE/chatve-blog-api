# Blogging API Documentation

Welcome to the documentation for the Blogging API. This API allows you to manage blog posts and comments in a blogging application.

## Endpoints

### GET `/api/posts`

Retrieve a list of all blog posts.

#### Response

- **Status Code:** 200 (OK)
- **Response Format:** JSON

Example Response:
```json
[
    {
        "title": "Tobi",
        "author": {
            "username": "user1"
        },
        "date_posted": "2023-08-20",
        "body": "The man is the best",
        "comment": [
            {
                "name": "John Doe",
                "post": "First Post",
                "comment": "this claim is false",
                "date_posted": "2023-08-20"
            }
        ]
    },
    // ... (more posts)
]
```

## GET `/api/posts/<pk>`

Retrieve details of a specific blog post.

Replace <pk> with the primary key of the desired post.

#### Response
- **Status Code:** 200 (OK)
- **Response Format:** JSON

Example Response:
```json
{
    "title": "Tobi",
    "author": {
        "username": "sample_user"
    },
    "date_posted": "2023-08-20",
    "body": "The man is the best",
    "comment": [
        {
            "name": "Dr. Chidi Ugwu - Atlanta Georgia",
            "post": "tobi",
            "comment": "This claim is true",
            "date_posted": "2023-08-20"
        }
    ]
}
```

## Usage

**Access the API endpoints using the provided URLs:**

- List of all posts: http://localhost:8000/api/posts
- Details of a specific post: http://localhost:8000/api/posts/<pk>

**Author [Tobi TheRevolutionary](https://github.com/Tobitheprof)**

If you face any problems using this API, be sure to reach out to me via [email](mailto:tobiekundayo07@gmail.com)


