第一步：首先把数据分成多个部分，比如说10个部分。然后每个部分都给一个Mapper A和Reducer A，因此总共有10个Mapper A和Reducer A。每个Mapper A和Reducer A会创建一个basket文档，这样我们就有10个basket文档。
第二步：把每个basket文件分给一个Mapper B处理，总共就有10个Mapper B，所有Mapper B的输出都汇集到一个Reducer B上面，因为Reducer B的作用是给所有Mapper B的输出查重去掉重复部分。Reducer B输出一个完整的frequent itemset candidate文档
第三步：把第一步的10个basket文档分给10个Mapper C，MapperC负责算每个basket里面所有candidate的support。然后10个MapperC的输出都给到ReducerC，ReducerC将会把每个candidate的support求和，输出最终frequent itemset以及对应的support。

需要调整的参数有
1. Mapper B的support
2. ReducerC的threshold（等于Mapper B的support乘以总共basket的个数，这个例子里为10）

注意事项：Reducer B输出的文档名字要为 4.txt 。并且存放到Mapper C的目录里，因为Mapper C需要这个文档作为字典去算每一个candidate的support。


数据清洗结果：
链接：https://pan.baidu.com/s/1QdFI-wYuD5M91Ep0ECKmfw 
提取码：dd7d 
复制这段内容后打开百度网盘手机App，操作更方便哦