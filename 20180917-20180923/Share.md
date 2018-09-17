# 将 m3u8 文件转换成 MP4
m3u8 实际不是真实的文件路径，而是路径片段的存储文件。所以直接下载是没法下载的,其他工具感觉也不怎么好用，还好使用 ffmpeg 可以很好的下载。

```
ffmpeg -user_agent "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7" -i https://v-replay.cdn.huya.com/vhuya/record/2018-08-24/huyalive/1421632169-1421632169-6105863672796545024-4626002232-10057-A-0-1/2018-08-24-09:43:14_2018-08-24-09:50:06.m3u8 -c copy test.mp4
```