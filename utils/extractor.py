"""抽取器，从响应结果中抽取部分数据"""

import json
import jmespath


class JMESPathExtractor(object):
    """
    用JMESPath实现的抽取器，对于json格式数据实现简单方式的抽取。
    """
    def extract(self, query=None, body=None):
        try:
            return jmespath.search(query, json.loads(body))
        except Exception as e:
            raise ValueError("Invalid query: " + query + " : " + str(e))


if __name__ == '__main__':
    from Auto_Ui.utils.client import HTTPClient
    res = HTTPClient(url='http://wthrcdn.etouch.cn/weather_mini?citykey=101010100').send()
    print(res.text)


    j = JMESPathExtractor()
    j_1 = j.extract(query='data.forecast[1].date', body=res.text)
    j_2 = j.extract(query='data.ganmao', body=res.text)
    print(j_1, j_2)
    # 结果：
    # 19日星期六 各项气象条件适宜，无明显降温过程，发生感冒机率较低。
