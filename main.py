from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
import requests

@register("astrbot_plugin_pplxsearch", "LovelyGuYiMeng", "Perplexity AI 搜索插件", "1.0.0")
class PPLXSearchPlugin(Star):
    def __init__(self, context: Context, config):
        super().__init__(context)
        self.config = config

    @filter.command("pplx")
    async def pplx_search(self, event: AstrMessageEvent, *args, **kwargs):
        query = event.message_str.strip()
        if not query:
            yield event.plain_result("请在指令后输入搜索内容，比如 /pplx 最新iPhone的详细参数？")
            return
        api_key = self.config.get("api_key")
        if not api_key:
            yield event.plain_result("请先在插件设置页面填写 Perplexity API密钥")
            return
        api_url = self.config.get("api_url")
        model = self.config.get("model")
        max_tokens = self.config.get("max_tokens")
        temperature = self.config.get("temperature")
        top_p = self.config.get("top_p")

        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": "Be precise and concise."},
                {"role": "user", "content": query}
            ],
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
        }
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        try:
            resp = requests.post(api_url, json=payload, headers=headers, timeout=15)
            resp.raise_for_status()
            data = resp.json()
            # 获取主内容
            content = data.get('choices', [{}])[0].get('message', {}).get('content', 'No content')
            # 获取引用来源
            search_results = data.get('search_results', [])
            citation_txt = ""
            if len(search_results) > 0:
                lines = []
                for idx, item in enumerate(search_results):
                    line = f"- [{item.get('title','来源')}]({item.get('url','')})"
                    lines.append(line)
                citation_txt = "## 搜索来源:\n" + "\n".join(lines) + "\n\n"
            yield event.plain_result(f"{citation_txt}{content}")
        except Exception as e:
            yield event.plain_result(f"请求PPLX接口异常：{e}")

    async def initialize(self):
        pass
    async def terminate(self):
        pass
