#Amit
import pymongo

# Create connection to mongodb
connection = pymongo.Connection("mongodb://localhost",safe=True)

#switch db
db = connection.school

#get students collection
students = db.students.find()

#iterate through students
for item in students :
    curr_score = -1
    scores_array = item["scores"]
    new_scores_array = []
    for value in scores_array:
        print "value", value
        if value["type"] == "homework":
            if curr_score == -1 :
                curr_score = value["score"]
            else:
                if curr_score < value["score"]:
                    curr_score = value["score"]
        else:
            new_scores_array.append(value)

    new_scores_array.append({"type": "homework","score":curr_score})
    db.students.update({"_id": item["_id"]},{"$set": {"scores": new_scores_array}})
