# mongodb+srv://<username>:<password>@cluster-yu.ixch7.gcp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
# DB = xy_db  Collections = user

from flask import Flask #,request # Response
from flask_restful import  Api,Resource,reqparse,abort


app = Flask(__name__)
api = Api(app)

videos = {}
Video_post_args = reqparse.RequestParser()
Video_post_args.add_argument("name",type=str,help="Name of the video",required=True)
Video_post_args.add_argument("views",type=int,help="Views of the video",required=True)
Video_post_args.add_argument("likes",type=int,help="Likes of the video",required=True)


names = {'tim':{'age':19,'gender':'male'},
        'jiner':{'age':29,'gender':'male'},
        'bill':{'age':69,'gender':'male'}}

# dqyw
def  abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404,message='Video id is not valid....')

class Hello(Resource):
    def get(self,name):
        # return {'name':name,'age':age}
        return names[name]


    def post(self):
        return {'data':'Posted'}
    
class Video(Resource):
    def get(self,video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return video_id
    
    def post(self,video_id):
        args = Video_post_args.parse_args()
        # print(request.form)
        videos[video_id] = args
        return videos[video_id],201

    def delete(self,video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '',204

api.add_resource(Video,'/video/<int:video_id>')

api.add_resource(Hello,'/hehe/<string:name>')

# api.add_resource(Hello,'/hehe/<string:name>/<int:age>')


if __name__ == '__main__':
    app.run(debug=True)
