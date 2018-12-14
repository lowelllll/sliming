import json
import requests

def get_content(url):
    """
    인스타그램의 게시글을 통해 비디오 링크를 가져옴
    TODO :: 향후 s3를 도입해 사진 링크도 가져와 자동으로 등록하게끔 함.
    :return:
    """
    res = requests.get(url+'?__a=1')
    data = json.loads(res.text)

    if data['graphql']['shortcode_media'].get('edge_sidecar_to_children'):
        items = data['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']
        video = [item['node'].get('video_url') for item in items if item['node'].get('video_url')][0]
    else:
        video = data['graphql']['shortcode_media'].get('video_url')
    return video

