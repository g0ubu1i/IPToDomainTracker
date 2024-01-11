# IPToDomainTracker

## 简介

这是一个用于反查IP地址信息的工具。通过该工具，你可以获取关于特定IP地址的有用信息，如域名、域名使用时间、icp备案公司等。

## 功能

- **域名反查**: 对IP地址进行反向域名解析，获取相关的域名信息。
- **icp备案**：对反查到的域名进行icp备案查询
-  **域名归属地**：获取域名的归属地信息

## 安装

```
git clone https://github.com/g0ubu1i/IPToDomainTracker.git
cd IPToDomainTracker
pip install -r requirements.txt
```

## 使用

```
python IPToDomainTracker.py --list <target_ip_file>
```

替换 `<target_ip_file>` 为你要反查的目标IP文件。

## 示例

```
python IPToDomainTracker.py --list url.txt
```

## 限制

- 该工具依赖于第三方服务，可能会受到其限制。

## 贡献

欢迎提出问题、报告bug或贡献代码。请提交问题和建议至GitHub Issues，我们将尽快处理。