# API

## Accounts
### Signup

POST /accounts/signup/

- Request Body

```json
{
    "username": "first_user",
    "email": "first_user@example.com",
    "password": "first_user1234",
    "password_check": "first_user1234"
}
```

### Signin

POST /accounts/signin/

- Request Body

```json
{
    "username": "seconduser",
    "password": "seconduser"
}
```

### Signout
POST /accounts/signout/

- Request Header

```
Authorization Token b8be3ea67513bd21203af5e3cd147e6dada27b06
```


## Posts
### List Posts
GET /posts/


### Create Post
POST /posts/
- Request Header
```
Authorization Token b8be3ea67513bd21203af5e3cd147e6dada27b06
```

- Request Body
```json
{
    "title": "sixth title",
    "description": "sixth description",
    "tags": ["tag1", "tag2"]
}
```

### Retrieve Post
GET /posts/pk(int)/


### Update Post
PUT /posts/pk(int)/
- Request Header
```
Authorization Token b8be3ea67513bd21203af5e3cd147e6dada27b06
```

- Request Body
```json
{
    "title": "sixth title",
    "description": "sixth description - changed",
    "tags": ["tag1", "tag2"]
}
```

### Partial Update Post
PATCH /posts/pk(int)/
- Request Header
```
Authorization Token b8be3ea67513bd21203af5e3cd147e6dada27b06
```

- Request Body
```json
{
    "description": "sixth description - changed twice"
}
```

### Delete Post
DELETE /posts/pk(int)/
- Request Headers

```
Authorization Token b8be3ea67513bd21203af5e3cd147e6dada27b06
```

## Comments
### List Comments
GET /comments/posts/post_id(int)/

### Create Comment
POST /comments/posts/post_id(int)/
- Request Headers

```
Authorization Token b8be3ea67513bd21203af5e3cd147e6dada27b06
```

- Request Body
```json
{
    "content": "third comment",
    "tags": ["태그"]
}
```

### Update Comment
PUT /comments/pk(int)/
- Request Headers

```
Authorization Token b8be3ea67513bd21203af5e3cd147e6dada27b06
```

- Request Body
```json
{
    "content": "third comment - changed",
    "tags": ["태그"]
}
```

### Partial Update Comment
PATCH /comments/pk(int)/
- Request Headers

```
Authorization Token b8be3ea67513bd21203af5e3cd147e6dada27b06
```

- Request Body
```json
{
    "content": "third comment - changed twice"
}
```

### Delete Comment
DELETE /comments/pk(int)/
- Request Headers

```
Authorization Token b8be3ea67513bd21203af5e3cd147e6dada27b06
```

## Tags
### List Posts by Tag
GET /tags/pk(str)/posts/


### List Comments by Tag
GET /tags/pk(str)/posts/
