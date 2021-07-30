# Immo Eliza deployment exercise

## Description

```
{
  "data": {
    "area": int,
    "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
    "rooms-number": int,
    "zip-code": int,
    "facades-number": Optional[int],
    "building-state": Optional[
      "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"
    ]
  }
}

```

## Usage

send your HTTP post equest over [here](https://app-deployment-example.herokuapp.com/)

## Development

**Github**

```
git clone https://github.com/hakanErgin/immo_eliza_deployment.git
```

**Docker**

to create image

```
docker build -t immo_eliza_deployment .
```

the create container

```
docker run -d -v $PWD/:/app -p 5000:5000 immo_eliza_deployment
```

`-d` for detached

`-v $PWD/:/app` for creating volume

## Deployment

**Heroku**

to deploy

```
heroku container:push web --app app-deployment-example
```

to release

```
heroku container:release web --app app-deployment-example
```
