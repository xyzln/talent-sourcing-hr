<div align="center">

<img src="assets/hero-agent-temp-worker.jpg" width="760" alt="Agent's HR"/>

# Agent's HR · 智能体设计师

### 不知道怎么创建智能体？不会生成子 agent？
**先研究现实岗位是怎么设计的，再把岗位设计翻译成 agent 人格与技能，直接生成对应智能体。**

<p>
  <img src="https://img.shields.io/badge/version-1.1.0-0d9488?style=flat-square" alt="version"/>
  <img src="https://img.shields.io/badge/license-MIT-2563eb?style=flat-square" alt="license MIT"/>
  <img src="https://img.shields.io/badge/languages-5-7c3aed?style=flat-square" alt="5 languages"/>
  <img src="https://img.shields.io/badge/platform-WorkBuddy%20Expert-0f766e?style=flat-square" alt="platform"/>
  <img src="https://img.shields.io/badge/SkillHub-published-f59e0b?style=flat-square" alt="SkillHub"/>
</p>

</div>

---

## 📖 目录

- [💡 为什么需要它](#-为什么需要它)
- [✨ 核心能力](#-核心能力)
- [🔄 五步工作流](#-五步工作流)
- [📊 覆盖度评分](#-覆盖度评分)
- [🚀 快速开始](#-快速开始)
- [💬 使用示例](#-使用示例)
- [🌐 多语言版本](#-多语言版本)
- [⚠️ 合规承诺](#️-合规承诺)
- [📁 仓库结构](#-仓库结构)
- [📄 开源协议](#-开源协议)

---

## 💡 为什么需要它

想造个 agent（或子 agent、技能），却不知道怎么设计，只能让通用 agent 碰运气？Agent's HR 的方法论只有一条：**不凭空设计 agent，先去看现实中干这活的人是怎么被设计的**。岗位职责、任职要求、工作流、协作界面、考核指标全部查清楚，再把岗位设计逐项翻译成 agent 设计，直接产出能落地的智能体规格。

| 痛点 | 通用 agent 的做法 | Agent's HR 的做法 |
|:---|:---|:---|
| 不知道怎么创建智能体 / 子 agent | 凭感觉写提示词，碰运气 | 先研究现实岗位怎么设计的，再生成 agent |
| 设计没有依据 | 拍脑袋编人格和技能 | 每项设计追溯到岗位研究证据（信源 + 获取时间） |
| 岗位要素抓不全 | 想到哪写到哪 | 六要素采集清单：职责 / 任职要求 / 工作流 / 协作界面 / 考核指标 / 工具栈 |
| 设计质量没验收 | 「看起来能用」 | 0-5 级覆盖度锚定 + 加权评分 + 一票否决 |
| 落不了地 | 只给建议不给规格 | 输出完整 agent 规格 + 落地方式与启用步骤 |

---

## ✨ 核心能力

| # | 能力 | 说明 |
|:--|:---|:---|
| 1 | **现实岗位设计研究** | 全网检索对应岗位的设计：真实 JD 的职责拆解、任职要求、日常工作流、协作界面、考核指标、工具栈；多源交叉验证，查不到如实说明 |
| 2 | **岗位 → 智能体映射** | 把六大岗位要素逐项翻译成 agent 设计要素：角色定位→人格、职责→技能与工作流、任职要求→能力锚定与铁律、协作界面→输入输出规格、考核指标→验收标准、工具栈→工具清单 |
| 3 | **设计覆盖度评分** | 5-8 个设计维度 0-5 级锚定打分，`match_score.py` 加权计算，输出覆盖度分级、强覆盖项、缺口项与一票否决标记 |
| 4 | **Agent 规格生成** | 结论先行输出完整智能体设计规格（frontmatter、人格、技能、工作流、工具、边界铁律、验收标准），并给出落地方式（专家包 / 独立技能 / 子 agent）与启用步骤 |

---

## 🔄 五步工作流

<img src="assets/workflow_CN.svg" width="100%" alt="五步工作流"/>

| 步骤 | 输入 | 输出 |
|:--|:---|:---|
| 1. 需求澄清 | 用户的 agent 想法 | 用途 / 场景 / 落地形态 / 边界四问 |
| 2. 岗位设计研究 | 需求 | 六要素研究摘要 + 信源与获取时间 |
| 3. 岗位 → 智能体映射 | 岗位设计摘要 | 设计草案（人格 / 技能 / 工作流 / 工具 / 边界） |
| 4. 覆盖度评分 | 设计草案 + 岗位证据 | 覆盖度总分 + 分级 + 缺口项与补齐建议 |
| 5. 规格生成 | 全部结果 | 完整 agent 规格 + 落地方式与启用步骤 |

---

## 📊 覆盖度评分

评分只基于岗位研究证据，无证据不评分。加权平均 × 20 = 覆盖度百分制：

| 覆盖度 | 分级 | 行动建议 |
|:--|:---|:---|
| ≥ 85 | **A · 可直接落地** | 按规格直接建成专家包 / 技能 / 子 agent |
| 70 – 84 | **B · 基本可用** | 落地同时补齐缺口项（补研究或补设计） |
| 50 – 69 | **C · 有缺口** | 先补岗位研究或补设计，再落地 |
| < 50 | **D · 不匹配** | 回到第 2 步重新研究岗位 |
| 核心项 ≤ 2 分 | **一票否决** | 无论总分默认 D，除非需求方明确豁免 |

---

## 🚀 快速开始

### 方式一：安装为专家包（推荐）

把本仓库作为 WorkBuddy 专家包安装：

```bash
# 克隆仓库
git clone https://github.com/xyzln/talent-sourcing-hr.git

# 复制到专家目录
cp -r talent-sourcing-hr ~/.workbuddy/plugins/marketplaces/my-experts/plugins/

# 注册（脚本位于 expert-manager 技能的 scripts/ 目录）
python3 register_expert.py ~/.workbuddy/plugins/marketplaces/my-experts/plugins/talent-sourcing-hr
```

然后在 WorkBuddy 专家中心选择「**Agent's HR**」，直接说你想造个什么 agent 即可。

### 方式二：单独使用技能

技能目录 `skills/recruit-web-sourcing/` 可独立复制到 `~/.workbuddy/skills/` 使用，或在 SkillHub 搜索 `recruit-web-sourcing` 安装对应语言版本。

---

## 💬 使用示例

> 不知道怎么创建智能体或子 agent？我想让这个 agent 干「用户行为分析并输出可执行结论」，帮我研究现实岗位怎么设计，直接生成 agent。

> 研究一下「数据分析师」这个岗位在现实中是怎么设计的：职责、任职要求、工作流、协作界面和考核指标。

> 把这个岗位的设计翻译成 agent 规格：人格、技能、工具、工作流和边界铁律。

---

## 🌐 多语言版本

| 语言 | README | SkillHub 技能 |
|:---|:---|:---|
| 🇨🇳 简体中文 | [README_CN.md](README_CN.md) | `recruit-web-sourcing-cn` |
| 🇹🇼 繁體中文 | [README_TW.md](README_TW.md) | `recruit-web-sourcing-tw` |
| 🇬🇧 English | [README_EN.md](README_EN.md) | `recruit-web-sourcing-en` |
| 🇷🇺 Русский | [README_RU.md](README_RU.md) | `recruit-web-sourcing-ru` |
| 🇸🇦 العربية | [README_AR.md](README_AR.md) | `recruit-web-sourcing-ar` |

各语言版本完整翻译了 SKILL.md、三份参考手册与评分脚本的输出文案。

---

## ⚠️ 合规承诺

- 岗位设计研究**只依据公开可查信源**，所有结论标注信源与获取时间，不编造
- **不设计用于作弊、欺诈、歧视、绕过监管或侵犯隐私的 agent**
- agent 的每项设计必须来自岗位研究证据，不凭空发明能力
- 覆盖度评分只基于证据，无证据 = 0 分并标注「待验证」

---

## 📁 仓库结构

```text
talent-sourcing-hr/
├── README.md                        # 入口（语言切换）
├── README_CN.md / _TW / _EN / _RU / _AR   # 五语言落地页
├── assets/                          # 配图
│   ├── hero-agent-temp-worker.jpg   # 人设主图
│   ├── talent-sourcing-network.jpg  # 岗位设计研究概念图
│   └── workflow_{CN,TW,EN,RU,AR}.svg      # 五步流程图（五语言）
├── .codebuddy-plugin/plugin.json    # 专家包清单
├── agents/talent-sourcing-hr.md     # 专家人格（Agent's HR · 顾寻）
├── avatars/expert.png               # 专家头像
├── skills/recruit-web-sourcing/     # 技能源码（简体中文）
│   ├── SKILL.md
│   ├── references/                  # 岗位设计研究手册 / 映射模型 / 设计规格模板
│   └── scripts/match_score.py       # 覆盖度计算器
├── i18n/{CN,TW,EN,RU,AR}/           # 五语言技能完整版本
└── LICENSE
```

---

## 📄 开源协议

[MIT](LICENSE) © 2026 talent-sourcing-hr contributors

<div align="center">

**⭐ 觉得好用就点个 Star，让更多不知道怎么建 agent 的人找到 Agent's HR**

</div>
