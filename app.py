from flask import Flask, render_template
import json

"""
A example for creating a Table that is sortable by its header
"""

app = Flask(__name__)
data = [{
  "name": "SQL",
  "commits": "2000",
  "uneven": "window function"
},
 {
  "name": "Python",
  "commits": "1",
  "uneven": "Pandas"
}, {
  "name": "HTML",
  "commits": "555",
  "uneven": "HTTP"
}]
# other column settings -> http://bootstrap-table.wenzhixin.net.cn/documentation/#column-options
columns = [
  {
    "field": "name", # which is the field's name of data key 
    "title": "name", # display as the table header's name
    "sortable": True,
  },
  {
    "field": "commits",
    "title": "commits",
    "sortable": True,
  },
  {
    "field": "uneven",
    "title": "uneven",
    "sortable": True,
  }
]

#jdata=json.dumps(data)

@app.route('/')
def index():
    return render_template("table.html",
      data=data,
      columns=columns,
      title='Flask Bootstrap Table')


if __name__ == '__main__':
	#print jdata
  app.run(debug=True)