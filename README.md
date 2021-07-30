# Immo Eliza deployment exercise

## Description

```
{
  "data": {
    "area": int,
    "subtype": ['MIXED_USE_BUILDING', 'HOUSE', 'MANSION', 'APARTMENT', 'VILLA',
       'FLAT_STUDIO', 'EXCEPTIONAL_PROPERTY', 'PENTHOUSE', 'GROUND_FLOOR',
       'TOWN_HOUSE', 'DUPLEX', 'APARTMENT_BLOCK', 'FARMHOUSE', 'BUNGALOW',
       'COUNTRY_COTTAGE', 'SERVICE_FLAT', 'TRIPLEX', 'OTHER_PROPERTY',
       'CHALET', 'LOFT', 'KOT', 'MANOR_HOUSE', 'PAVILION', 'CASTLE'],
    "room_number": int,
    "location": int,
    "facade_count": int,
    "building_condition" : ['GOOD', 'TO_BE_DONE_UP', 'AS_NEW', 'TO_RESTORE', 'JUST_RENOVATED',
       'TO_RENOVATE']
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
