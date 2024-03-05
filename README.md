# API

## Accounts
### Signup

POST http://43.201.183.161/accounts/signup/

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

POST http://43.201.183.161/accounts/signin/

- Request Body

```json
{
    "username": "seconduser",
    "password": "seconduser"
}
```

### Signout
POST http://43.201.183.161/accounts/signout/

- Request Header

```
Authorization Token b8be3ea67513bd21203af5e3cd147e6dada27b06
```


## Posts
### List Posts
GET http://43.201.183.161/posts/


### Create Post
POST http://43.201.183.161/posts/
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
GET http://43.201.183.161/posts/pk(int)/


### Update Post
PUT http://43.201.183.161/posts/pk(int)/
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
PATCH http://43.201.183.161/posts/pk(int)/
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
DELETE http://43.201.183.161/posts/pk(int)/
- Request Headers

```
Authorization Token b8be3ea67513bd21203af5e3cd147e6dada27b06
```

## Comments
### List Comments
GET http://43.201.183.161/comments/posts/post_id(int)/

### Create Comment
POST http://43.201.183.161/comments/posts/post_id(int)/
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
PUT http://43.201.183.161/comments/pk(int)/
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
PATCH http://43.201.183.161/comments/pk(int)/
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
DELETE http://43.201.183.161/comments/pk(int)/
- Request Headers

```
Authorization Token b8be3ea67513bd21203af5e3cd147e6dada27b06
```

## Tags
### List Posts by Tag
GET http://43.201.183.161/tags/pk(str)/posts/


### List Comments by Tag
GET http://43.201.183.161/tags/pk(str)/posts/


<br>
<br>

# 추가로 고민할 부분

1. 태그 생성 및 삭제 로직 재고
2. 쿼리 최적화
3. django app 분리 기준
4. SerializerMethodField()와 @property
5. DRF TokenAuthentication → JWT
6. 로직을 어떻게 분리하고 어디에서 담당할 것인가