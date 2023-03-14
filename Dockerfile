# 基于的基础镜像
FROM python:3.8.16

# 设置工作目录为 /demo/
WORKDIR /nsf-flask-trade/

# 将依赖文件拷贝到工作目录
COPY requirements.txt /nsf-flask-trade/

# 执行pip指令，安装这个应用所需要的依赖
RUN pip install -r requirements.txt

# 拷贝当前目录的所有内容拷贝到工作目录下
COPY . /nsf-flask-trade/

# 允许外界访问5000端口
EXPOSE 8000

# 设置容器进程为python app.py ，启动
ENTRYPOINT [ "python", "app.py" ]
