https://github.com/zixiiu/Digital_Life_Server  

这个项目里面的语音合成，我单独做成api了

# 运行项目：

## 1. 安装[python3.9.8](https://www.python.org/ftp/python/3.9.8/)  

## 2. 装依赖  

> 注意：如果你有多个python，请将pip换为该版本pip所在路径，例如:"C:\Users\fanbo\AppData\Local\Programs\Python\Python39\Scripts\pip.exe"

```shell
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple 
pip config set install.trusted-host mirrors.aliyun.com
```

```shell
pip install torch torchvision torchaudio
```  

下面这一步，如果出现个别冲突错误，不用管  

```shell
pip install -r requirements_out_of_pytorch.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

```shell
pip install sentry_sdk flask flask_cors
```

## 3. 下载模型  

此处下载tts文件夹  
https://pan.baidu.com/s/1EnHDPADNdhDl71x_DHeElg?pwd=75gr  

里面有两个文件夹，models_unused可选，models必须下载  

将下载的json、pth文件全部移动到项目的models文件夹，注意只需要文件，不需要外层文件夹  

## 4.测试  

直接运行getaudio.py，10秒后查看项目文件夹下的output.wav  
如果没有生成：检查输出里面的错误信息、python版本，并且检查库和模型文件，必要时安装c++构建工具并重新生成内核  
可选：

```shell
cd "TTS/vits/monotonic_align"
mkdir monotonic_align
python setup.py build_ext --inplace
cp monotonic_align/*.pyd .
```

如果output.wav里面是杂音，卸载python并重新按照1、2来安装库  

## 5.使用api  

> /getaudio

api在普通电脑上5秒内响应，2h2g轻量服务器上10秒内响应  
模型编号有这些：  

```
0:("models/paimon6k.json", "models/paimon6k_390k.pth"),
1:("models/CyberYunfei3k.json", "models/yunfei3k_69k.pth")
2:("models/ayaka.json", "models/ayaka_167k.pth")
3:("models/ningguang.json", "models/ningguang_179k.pth")
4:("models/nahida.json", "models/nahida_129k.pth")
5:("models/noelle.json", "models/noelle_337k.pth")
6:("models/yunfeimix.json", "models/yunfeimix_122k.pth")
7:("models/yunfeineo.json", "models/yunfeineo_25k.pth")
8:("models/zhongli.json", "models/zhongli_44k.pth")
9:("models/catmix.json" , "models/catmix_107k.pth")
```  

示例：  
https://127.0.0.1:5001/getaudio?text=%E4%BD%A0%E5%A5%BD%E5%95%8A
 
参数：

| 参数名 | 类型 | 是否必须 | 描述 |
| :----: | :----: | :----: | :----: |
| text | string | 是 | 文本 |
| name | string | 否 | 模型编号，0至9 |

返回：  
type:json  

| 参数名 | 类型 | 是否必须 | 描述 |
| :----: | :----: | :----: | :----: |
| code | intger | 否 | 错误代码 |
| url | string | 否 | 文件链接 |
| msg | string | 否 | 状态描述 |
