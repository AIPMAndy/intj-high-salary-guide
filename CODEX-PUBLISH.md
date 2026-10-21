# 给 Codex 的上线任务（一条指令即可使用）

你现在位于一个完整的静态 GitHub Pages 项目根目录。目标是把这个项目发布成公开的、独立的新仓库 `AIPMAndy/intj-high-salary-guide`，网站网址目标为 `https://aipmandy.github.io/intj-high-salary-guide/`。**千万不要覆盖 `AIPMAndy/intj-growth-guide`。**

1. 运行 `python3 scripts/build.py --check`、`python3 -m unittest discover -s tests -v`，有错误就修复。
2. 检查当前 GitHub 身份确实有权操作 `AIPMAndy`，然后执行 `bash scripts/publish.sh`。如果本地缺少 `gh` 或未登录，就先请我在终端完成身份认证；不要把 token 写进仓库。
3. 在仓库 Settings → Pages 确认 Source 是 **GitHub Actions**；如果自动脚本无法开启，用 GitHub 网页手动选择。
4. 检查 Actions → Deploy GitHub Pages 成功，再实际打开 `https://aipmandy.github.io/intj-high-salary-guide/`，验证所有核心交互在桌面和手机正常。
5. 在仓库 About 设置 Website 为上述 Pages 地址，Topics 可设 `intj`, `career`, `salary-negotiation`, `chinese`, `github-pages`, `job-search`, `promotion`。
6. 将部署结果、最终仓库链接和实际可访问网站链接反馈给我；任何一步失败必须明确报告，不能假装已上线。

内容原则：INTJ 只是内容识别标签，不可宣称人格决定收入；示例必须标注假设，收入数字一律以用户输入为准；不可杜撰客户涨薪案例。不得改掉真实来源和隐私声明。
