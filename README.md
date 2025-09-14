</div>

<div align="center">

![:name](https://count.getloli.com/@astrbot_plugin_pplxsearch?name=astrbot_plugin_pplxsearch&theme=minecraft&padding=7&offset=0&align=top&scale=1&pixelated=1&darkmode=auto)

# astrbot_plugin_pplxsearch

_✨ [astrbot](https://github.com/AstrBotDevs/AstrBot) Perplexity AI搜索插件 ✨_

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/作者-YourName-blue)](https://github.com/YourName)

</div>

## 📦 插件简介

【智能搜索】本插件让AstrBot接入Perplexity AI的互联网搜索（需自备API密钥），支持精准、快速查询网络最新信息。管理员可在 控制面板>插件配置 填写API KEY、调整模型参数，群友可通过命令调用搜索。

## ⌨️ 命令

|     命令           |      说明                           |
|:------------------:|:-----------------------------------:|
| /pplx 搜索内容     | 使用Perplexity AI检索相关内容并回复  |

> 例： `/pplx 2025年诺贝尔奖得主是谁`

## ⚙️ 配置方式

1. 前往 [Perplexity API](https://www.perplexity.ai) 申请你的 API Key
2. 在 AstrBot 控制台插件面板填写 API Key 及模型参数，可自定义 answers 风格和token长度

| 配置项          | 说明                      |
| --------------- | ------------------------- |
| API密钥         | 必填，自行申请            |
| API地址         | 默认无需更改              |
| 模型名称        | sonar（其他模型请查官方文档） |
| 最大Token数     | 默认4000，建议保持默认    |
| 采样温度        | 默认0.2，越高越发散       |

## 📌 注意事项

- 大陆使用本插件需魔法或代理中转保证API可联通
- 如API接口调整，仅需在插件配置中更新模型与接口参数，无需修改代码
- 合理使用API额度，避免滥用导致调用异常

## ❓ 常见问题

### Q: 为什么提示"API密钥未配置"？

- 未在插件面板填写API Key；
- API Key填写有误或已过期，请检查账号和密钥。

### Q: 返回内容不完整或异常？

- 检查Max_Token设置及Perplexity账户额度
- 可尝试更换模型或降低temperature参数

---

## 🐔 联系作者

- **GitHub**：[LovelyGuYiMeng 的 GitHub](https://github.com/LovelyGuYiMeng)
- **反馈**：欢迎在 [GitHub Issues](https://github.com/LovelyGuYiMeng/astrbot_plugin_pplxsearch/issues) 提交问题或建议

---

## 🌟 支持

- Star 这个项目，让更多人用上智能搜索！

## 📜 开源协议

本项目采用 [MIT License](LICENSE)
