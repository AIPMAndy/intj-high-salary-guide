# INTJ 职场拿高薪的保姆级攻略

> **别等公司主动给你涨薪。先看岗位值多少钱，再拿出你的成果证据。**
>
> 10 章攻略 · 7 天行动计划 · 6 份可复制模板 · Offer 税前年现金对比计算器。免费开源、无登录、无收费墙。

**INTJ 怎么在职场拿高薪？** 这份由 AI 酋长 Andy 写的免费开源攻略有 10 章教程、7 天行动计划、6 份可复制模板和 Offer 税前年现金对比计算器，从岗位定价、成果证据讲到谈薪。高薪取决于市场机会和能力证据，不由 MBTI 类型决定。


**作者：AI 酋长 Andy** · [个人主页](https://metaver.vip/) · [职业咨询与高管陪跑](https://metaver.vip/services) · 微信 `AIPMAndy`

![项目分享封面](assets/social-preview.png)

## 🌐 在线网站

**[立即打开互动版](https://aipmandy.github.io/intj-high-salary-guide/)** · [7天开始](START-HERE.md) · [30天进阶](guides/30-day-plan.md) · [证据和研究来源](docs/sources.md)

## 适合谁

- 工作3～10年，有技术/产品/运营/管理经验，却一直不知道如何为自己定价的人。
- 工作做得不少，但简历讲不出成果、面试说不清贡献的人。
- 想转向有更大业务价值的岗位，但还没想清楚下一步的人。
- 想内部晋升，需要跟主管谈责任边界和职级标准的人。
- 正在拿 Offer、准备谈薪，希望看清固定现金和浮动报酬差别的人。

这里的“INTJ”是为了方便读者找到话题的**人格偏好标签**。一个人能否获得高薪取决于市场机会、能力及其证据、岗位责任和谈判条件等，不由MBTI类型决定。MBTI也不应用于招聘筛选。[参见官方说明](https://www.themyersbriggs.com/en-US/Explore-Solutions/MBTI?type=page)。

## 10章目录

| 章节 | 解决什么问题 | 必须带走的成果 |
| --- | --- | --- |
| 01 岗位定价 | 我的岗位到底值多少钱？ | 20条可比岗位样本 |
| 02 成果账本 | 我给公司创造了什么价值？ | 3个有证据的STAR故事 |
| 03 业务杠杆 | 哪些岗位值得争取？ | 3个岗位机会评分卡 |
| 04 简历改造 | 招聘方为什么要面我？ | 一份针对性简历 |
| 05 面试准备 | 我怎样证明自己能胜任？ | 8题问题库+3个案例 |
| 06 晋升提案 | 怎么拿到更高一级责任？ | 一页晋升业务提案 |
| 07 影响力建设 | 怎样让业务成果被看见？ | 4周成果周报 |
| 08 谈薪筹码 | 薪资怎么开口？ | 目标/底线/BATNA备忘录 |
| 09 Offer核算 | 13薪、奖金、股权怎么算？ | 两份Offer对比表 |
| 10 入职90天 | 高薪入职后怎么站稳？ | 30/60/90天业务计划 |

## 5分钟上手

1. **定目标**：打开[互动网站](https://aipmandy.github.io/intj-high-salary-guide/)，选“跳槽涨薪 / 内部晋升 / 正在谈 Offer”。
2. **补证据**：先做第01章的岗位样本表，或第02章的成果账本。没有证据先别报价。
3. **实际行动**：按7天计划每天留下一份交付物；进度可勾选并导出 Markdown。
4. **算清楚账**：利用 Offer 对比器核算税前年固定现金；股票和奖金单列核查。
5. **拿走模板**：在网站复制HR谈薪、晋升提案、结果周报等6份模板。

## 💻 网站功能

- 10 章可折叠的完整图文步骤，支持关键词检索、主题筛选。
- 依据跳槽、晋升、Offer谈薪阶段切换的行动路线。
- 7天进度打卡，存于当前浏览器 `localStorage`，支持导出 `.md`。
- Offer 对比器，区分**保证固定年现金**和**可能取得的浮动奖金**，不做不可靠的税后预测。
- 6份可复制模板；浏览器拒绝复制时下载本地文本。
- 纯前端，无后端、无第三方CDN、无账号。
- 手机 / 电脑响应式；兼容键盘操作与减弱动效偏好。

## 🛠 本地预览 / 修改

**无需 Node，Python 3.9+ 即可。**

```bash
python3 scripts/build.py
python3 -m unittest discover -s tests -v
python3 -m http.server 8000
```

浏览器访问 `http://localhost:8000/`。修改 `data/chapters.json`、`data/templates.json`、`data/plan.json` 或 `site/template.html` 后，运行 `python3 scripts/build.py` 重新生成独立站点首页。

## 项目结构

```text
intj-high-salary-guide/
├── index.html               # 已构建的独立响应式网站
├── site/template.html       # 原始页面模板和交互代码
├── data/                    # 10章内容 / 7天计划 / 6份模板
├── guides/                  # 30天进阶行动计划
├── templates/               # Markdown实操表格
├── docs/sources.md          # 来源核验、方法边界
├── scripts/build.py         # 无依赖构建
├── scripts/publish.sh       # 新仓库创建与部署
├── tests/test_project.py    # 单元和静态检查
├── assets/                  # 原创项目封面与favicon
├── .github/workflows/       # 测试与GitHub Pages部署
├── START-HERE.md            # 开始指南
├── CODEX-PUBLISH.md         # 给Codex的上线任务
└── CONTRIBUTING.md
```

## 隐私与真实案例声明

- 网站不收集账号和简历数据，打卡状态只存当前浏览器本地。清除浏览器存储后会丢失。
- 计算器默认数字只是**演示数据**，不能当作市场真实薪酬或成功案例。
- 所有岗位和薪资需读者自行核验城市、时间、工作年限和合同口径。
- 所有示例均为教学示例；不暗示作者真实客户获得某个具体涨薪幅度。
- 本项目为职业教育与信息整理，不替代法律、税务、劳动合同或个人财务专业意见。

欢迎 Star ⭐、Issue、PR 共建。贡献时请避免上传客户资料和未经授权的内部数据，详情见 [CONTRIBUTING.md](CONTRIBUTING.md)。

**AI 酋长 Andy** · https://metaver.vip/ · 微信 `AIPMAndy`

---

<!-- andy-author-card:start -->
## 作者 / About the author

**AI 酋长 Andy（Andy Liu，GitHub/X @AIPMAndy）**：前腾讯/百度 AI 产品专家，大模型独角兽前 VP，现专注 AI + 产品方法论创业。

微信 `AIPMAndy`（备注「INTJ 高薪」） · [X @AIPMAndy](https://x.com/AIPMAndy) · [Telegram @AIPMAndy](https://t.me/AIPMAndy) · [个人官网 metaver.vip](https://metaver.vip/)

*AI Chief Andy (Andy Liu, @AIPMAndy on GitHub and X) is a former Tencent and Baidu AI product expert and former VP at an LLM unicorn, now a serial entrepreneur focused on AI and product methodology.*

### Andy 的其他免费指南

- [GitHub 赚钱实战指南](https://aipmandy.github.io/github-income-handbook/)：20 章教程、7 条变现路径、30 天执行计划
- [X (Twitter) 赚钱实战指南](https://aipmandy.github.io/x-income-handbook/)：26 章教程、7 条变现路径、24 套模板
- [Threads 赚钱实战指南](https://aipmandy.github.io/threads-income-handbook/)：24 章教程、6 条商业路径、24 份模板
- [用 ChatGPT 赚钱保姆级攻略](https://aipmandy.github.io/chatgpt-income-handbook/)：34 章教程、10 个服务包、64 套提示词
- [失业自救手册](https://aipmandy.github.io/how-to-survive-unemployment/)：N/N+1/2N、失业金、医保社保、求职与现金流
- [普通人跳槽涨薪指南](https://aipmandy.github.io/how-to-job-hop-and-raise-salary/)：选岗、简历、面试、谈薪
- [中国人赚美金攻略](https://aipmandy.github.io/how-to-earn-usd-from-china/)：8 种海外收入路线

<!-- andy-author-card:end -->
