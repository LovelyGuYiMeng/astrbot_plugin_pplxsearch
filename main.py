from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

import httpx
import re

@register("astrbot_plugin_pplxsearch", "LovelyGuYiMeng", "Perplexity AI 搜索插件", "1.2.0")
class PPLXSearchPlugin(Star):
    def __init__(self, context: Context, config):
        super().__init__(context)
        self.config = config

    @filter.command("pplx")
    async def pplx_search(self, event: AstrMessageEvent):
        query = re.sub(r'^/?pplx\s*', '', event.message_str, flags=re.IGNORECASE).strip()
        if not query:
            yield event.plain_result("请在指令后输入搜索内容，比如 /pplx 最新iPhone参数")
            return

        api_key = self.config.get("api_key")
        if not api_key:
            yield event.plain_result("请先在插件设置页面填写 Perplexity API 密钥")
            return

        api_url = self.config.get("api_url")
        model = self.config.get("model")
        max_tokens = self.config.get("max_tokens")
        temperature = self.config.get("temperature")
        top_p = self.config.get("top_p")
        show_citation = self.config.get("show_citation", True)

        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": "Be precise and concise."},
                {"role": "user", "content": query}
            ],
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p
        }
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        try:
            async with httpx.AsyncClient(timeout=15) as client:
                resp = await client.post(api_url, json=payload, headers=headers)
                resp.raise_for_status()
                data = resp.json()
                content = ""
                if "choices" in data and data["choices"]:
                    content = data["choices"][0].get("message", {}).get("content", "")
                    search_results = data.get("search_results", [])
                    if show_citation and search_results:
                        citations = "\n".join(
                            f"- [{item.get('title', '链接')}]({item.get('url', '')})" for item in search_results
                        )
                        reply = f"## 搜索来源:\n{citations}\n\n## 内容:\n{content}"
                    else:
                        reply = content
                else:
                    reply = "未获取到搜索结果"
                yield event.plain_result(reply)
        except httpx.RequestError as e:
            logger.exception(f"请求 PPLX 接口 httpx 异常: {e}")
            yield event.plain_result("请求PPLX接口异常，请联系管理员查看后台日志。")
        except httpx.HTTPStatusError as e:
            logger.exception(f"PPLX接口 HTTP 状态错误: {e}")
            yield event.plain_result("PPLX接口返回了错误的 HTTP 状态码，请联系管理员查看后台日志。")
        except Exception as e:
            logger.exception(f"请求 PPLX 接口发生未捕获异常: {e}")
            yield event.plain_result("请求PPLX接口异常，请联系管理员查看后台日志。")

    async def initialize(self):
        pass

    async def terminate(self):
        pass
