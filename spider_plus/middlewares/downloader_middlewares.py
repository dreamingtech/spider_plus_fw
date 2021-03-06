# coding=utf-8
# 下载器中间件

class DownloaderMiddleware(object):
    '''完成对下载器中间件的封装'''

    def process_request(self, request):
        '''
        实现对request的处理
        :param request: 请求对象
        :return: 请求对象
        '''
        # print("下载器中间件：process_request方法")
        return request

    def process_response(self, response):
        '''
        实现对response的处理
        :param response: 响应对象
        :return: 响应对象
        '''
        # print("下载器中间件：process_response方法")
        return response