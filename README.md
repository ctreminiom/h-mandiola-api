# h-mandiola-api



### Create consecutive type
curl --request POST \
  --url http://localhost:5000/api/admin/consecutive/type \
  --header 'content-type: application/json' \
  --data '{
	"name": "Activity"
}'


## Get consecutives types
curl --request GET \
  --url http://localhost:5000/api/admin/consecutive/types


## Create consecutive
curl --request POST \
  --url http://localhost:5000/api/admin/consecutive \
  --header 'content-type: application/json' \
  --data '{
	"type": "20",
	"description": "There'\''s the Activity consecutive",
	"has_prefix": "false",
	"prefix": "null",
	"has_range": "true",
	"initial": "1",
	"final": "100",
	"consecutive": "1"
}'


## Get consecutives
curl --request POST \
  --url http://localhost:5000/api/admin/consecutive \
  --header 'content-type: application/json' \
  --data '{
	"type": "20",
	"description": "There'\''s the Activity consecutive",
	"has_prefix": "false",
	"prefix": "null",
	"has_range": "true",
	"initial": "1",
	"final": "100",
	"consecutive": "1"
}'

## Create activuty
curl --request POST \
  --url http://localhost:5000/api/admin/activity \
  --header 'content-type: application/json' \
  --data '{
	"consecutive": "1",
	"name": "Activity #1",
	"description": "Descrption asdasd",
	"image_path": "asdsadsadas"
}'