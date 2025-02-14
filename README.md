# 加速 HuggingFace 下载

> 默认使用**ModelScope**  
> 默认下载到脚本执行目录  
> 默认重试**10**次  

```
--repo              仓库名称
--local-dir         本地路径
--use_model_scope   是否使用ModelScope
--num-retries       重试次数
```

## 模型

```
python model.py --repo="Monor/Qwen1.5-0.5B-h-world" --local-dir="/Users/huangxinping/Desktop"
```

## 数据集

```
python dataset.py --repo='Monor/hwtcm' --use_model_scope=False --num-retries=100
```

注意事项：  
对于ModelScope，并非HuggingFace的任意模型或数据集都可以下载。如报错如下，则请手动检查：

modelscope.hub.errors.RequestError: Url = https://www.modelscope.cn/api/v1/datasets/fka/awesome-chatgpt-prompts, Request id=8c1d2564-e24a-49f3-b6b0-1d2c358a9d20 Code = 10020101002 Message = 不存在的数据集, Please specify correct dataset_name and namespace.