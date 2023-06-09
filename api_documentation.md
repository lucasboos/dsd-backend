# API Documentation

## User API

Base URL: `/api/v1/user`

### Get All Users

Retrieve all user information.

#### Request

- Method: `GET`
- URL: `/api/v1/user`

#### Response

- Status: 200 OK
- Body:

```json
[
  {
    "id": 1,
    "nome": "John Doe",
    "login": "johndoe",
    "cep": "12345-678",
    "numero": 10,
    "complemento": "Apartment 123",
    "telefone": "1234567890"
  },
  {
    "id": 2,
    "nome": "John Doe2",
    "login": "johndoe2",
    "cep": "12345-678",
    "numero": 10,
    "complemento": "Apartment 123",
    "telefone": "1234567890"
  }
]
```

### Get All Complete User Information

Retrieve all complete user information.

#### Request

- Method: `GET`
- URL: `/api/v1/user/complete`

#### Response

- Status: 200 OK
- Body:

```json
[
	{
		"nome": "John Doe1",
		"login": "johndoe1",
		"cep": 12647528,
		"numero": "10",
		"complemento": "Apartment 123",
		"telefone": "987654321",
		"logradouro": "Rua Fictícia",
		"ibge": 165767,
		"bairro": "Bairro Fictício",
		"ddd": "00",
		"uf": "UF",
		"ddd": 99
	},
	{
		"nome": "John Doe2",
		"login": "johndoe2",
		"cep": 12647528,
		"numero": "10",
		"complemento": "Apartment 123",
		"telefone": "987654321",
		"logradouro": "Rua Fictícia",
		"ibge": 165767,
		"bairro": "Bairro Fictício",
		"ddd": "00",
		"uf": "UF",
		"ddd": 99
	}
]
```

### Get User by ID

Retrieve user information by ID.

#### Request

- Method: `GET`
- URL: `/api/v1/user/<id>`

#### Response

- Status: 200 OK
- Body:

```json
{
  "id": 1,
  "nome": "John Doe",
  "login": "johndoe",
  "cep": "12345-678",
  "numero": 10,
  "complemento": "Apartment 123",
  "telefone": "1234567890"
}
```

### Create User

Create a new user.

#### Request

- Method: `POST`
- URL: `/api/v1/user/`
- Body:

```json
{
  "nome": "John Doe",
  "login": "johndoe",
  "cep": "12345-678",
  "numero": 10,
  "complemento": "House",
  "telefone": "1234567890"
}
```

#### Response

- Status: 200 OK
- Body:

```json
{
  "message": "User created successfully"
}
```

### Delete User by ID

Delete user information by ID.

#### Request

- Method: `DELETE`
- URL: `/api/v1/user/<id>`

#### Response

- Status: 200 OK
- Body:

```json
{
  "messagem": "Successfully deleted user"
}
```

## CEP API

Base URL: `/api/v1/cep`

### Get City by IBGE

Retrieve city information by IBGE code.

#### Request

- Method: `GET`
- URL: `/api/v1/cep/cidade/<ibge>`

#### Response

- Status: 200 OK
- Body:

```json
{
  "ibge": "1234567",
  "cidade": "São Paulo",
  "uf": "SP",
  "ddd": "11"
}
```

### Get CEP by IBGE and ZIP Code

Retrieve address information by IBGE code and ZIP code.

#### Request

- Method: `GET`
- URL: `/api/v1/cep/<ibge>/<cep>`

#### Response

- Status: 200 OK
- Body:

```json
{
  "cep": "12345-678",
  "logradouro": "Rua Example",
  "ibge": "1234567",
  "bairro": "Example Neighborhood",
  "cidade": "São Paulo",
  "uf": "SP",
  "ddd": "11"
}
```

### Create CEP

Create a new address.

#### Request

- Method: `POST`
- URL: `/api/v1/cep/`

#### Response

- Status: 200 OK
- Body:

```json
{
  "cep": "12345-678",
  "logradouro": "Rua Example",
  "ibge": "1234567",
  "bairro": "Example Neighborhood",
  "cidade": "São Paulo",
  "uf": "SP",
  "ddd": "11"
}
```

### Update City

Update city information by IBGE code.

#### Request

- Method: `PUT`
- URL: `/api/v1/cep/<ibge>`

#### Response

- Status: 200 OK
- Body:

```json
{
  "message": "City updated successfully"
}
```

### Delete City

Delete city information by IBGE code.

#### Request

- Method: `DELETE`
- URL: `/api/v1/cep/<ibge>`

#### Response

- Status: 200 OK
- Body:

```json
{
  "message": "City deleted successfully"
}
```