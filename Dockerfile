FROM registry.cn-hangzhou.aliyuncs.com/xyd-2020/ubuntu
RUN apt install net-tools
EXPOSE 8000
COPY ./itauto /www
COPY ./start.sh /www/start.sh
ENTRYPOINT ["/www/start.sh"]
