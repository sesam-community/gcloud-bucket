from flask import Flask, Response
import os
import logger
from googlecloudstorage import GoogleCloudStorage

app = Flask(__name__)
logger = logger.Logger("gcloud-bucket")

# Google cloud storage requires the environmental variable GOOGLE_APPLICATION_CREDENTIALS for authentication to work
# these credentials should be passed to the GOOGLE_APPLICATION_CREDENTIALS_CONTENT environment variable
# the GOOGLE_APPLICATION_CREDENTIALS_CONTENT value will be written to the file specified in the
# GOOGLE_APPLICATION_CREDENTIALS environment value
# the GOOGLE_APPLICATION_BUCKETNAME environment value is used to contain the name of the bucket to read from
credentials = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_CONTENT")
credentialspath = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
bucketname = os.environ.get("GOOGLE_APPLICATION_BUCKETNAME")


class DataAccess:

    def __get_all_file(self, path):
        google_cloud_storage = GoogleCloudStorage(credentialspath, credentials, bucketname)
        # get xml files from Google cloud storage
        return google_cloud_storage.download(path)

    def get_file(self, path):
        return self.__get_all_file(path)


data_access_layer = DataAccess()


# main entrypoint of service ('/entities')
@app.route("/<path:path>", methods=["GET"])
def get(path):
    return Response(data_access_layer.get_file(path))


if __name__ == '__main__':
    app.run(threaded=True, debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))