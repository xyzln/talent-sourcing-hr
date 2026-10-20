<div align="center">

<img src="assets/hero-agent-temp-worker.jpg" width="760" alt="招聘尋訪官"/>

# 招聘尋訪官 · Talent Sourcing Officer

### 不會搭臨時 agent？還在讓 agent 碰運氣？
**憑真實招聘經驗與需求，精準匹配你的 agent 臨時工。**

<p>
  <img src="https://img.shields.io/badge/version-1.0.0-0d9488?style=flat-square" alt="version"/>
  <img src="https://img.shields.io/badge/license-MIT-2563eb?style=flat-square" alt="license MIT"/>
  <img src="https://img.shields.io/badge/languages-5-7c3aed?style=flat-square" alt="5 languages"/>
  <img src="https://img.shields.io/badge/platform-WorkBuddy%20Expert-0f766e?style=flat-square" alt="platform"/>
  <img src="https://img.shields.io/badge/SkillHub-published-f59e0b?style=flat-square" alt="SkillHub"/>
</p>

</div>

---

## 📖 目錄

- [💡 為什麼需要它](#-為什麼需要它)
- [✨ 核心能力](#-核心能力)
- [🔄 五步工作流](#-五步工作流)
- [📊 匹配度評分](#-匹配度評分)
- [🚀 快速開始](#-快速開始)
- [💬 使用範例](#-使用範例)
- [🌐 多語言版本](#-多語言版本)
- [⚠️ 合規承諾](#️-合規承諾)
- [📁 倉庫結構](#-倉庫結構)
- [📄 開源協議](#-開源協議)

---

## 💡 為什麼需要它

通用 agent 什麼都答一點，招聘尋訪卻是個精細活：需求要拆解、管道要覆蓋、能力要對分、結論要可追溯。這個「agent 臨時工」把整套方法論預製好了——你出業務要求，它出尋訪結論。

| 痛點 | 通用 agent 的做法 | 招聘尋訪官的做法 |
|:---|:---|:---|
| 不知道怎麼設定臨時 agent | 憑感覺寫提示詞，碰運氣 | 方法論預製：五步流程 + 三份參考文件 |
| 需求模糊 | 直接開搜，搜到啥算啥 | 先結構化人才畫像，缺資訊先提問 |
| 檢索沒章法 | 一兩個關鍵字碰運氣 | 關鍵字矩陣 × 管道分層，多輪交叉驗證 |
| 匹配靠感覺 | 「看起來挺合適」 | 0-5 級行為錨定 + 加權評分 + 一票否決 |
| 結論不可追溯 | 說得熱鬧，沒有信源 | 每個判斷掛證據，行情資料標記取得時間 |

---

## ✨ 核心能力

| # | 能力 | 說明 |
|:--|:---|:---|
| 1 | **業務要求結構化** | 把「要個能扛事的後端」這類口語要求，轉成結構化人才畫像：硬性條件、能力維度、權重、一票否決項 |
| 2 | **全網檢索尋訪** | 關鍵字矩陣 + 管道分層（招聘網站 / 社群社群 / 競品動態 / 產業報告），多輪檢索，交叉驗證供給密度與薪資行情 |
| 3 | **能力建模與精準匹配** | 5-8 個可評分能力維度、0-5 級行為錨定量表、`match_score.py` 加權計算，輸出匹配度分級、優勢項、缺口項 |
| 4 | **尋訪報告輸出** | 結論先行：供給概況、Top 匹配線索表、觸達建議、風險備案、72 小時行動清單 |

---

## 🔄 五步工作流

<img src="assets/workflow_TW.svg" width="100%" alt="五步工作流"/>

| 步驟 | 輸入 | 輸出 |
|:--|:---|:---|
| 1. 需求結構化 | 業務要求 / JD | 人才畫像（硬性條件 + 能力維度 + 權重） |
| 2. 檢索策略 | 人才畫像 | 關鍵字矩陣 + 管道清單 + 檢索輪次 |
| 3. 全網檢索 | 檢索策略 | 命中紀錄（信源 + 時間 + 品質評級） |
| 4. 能力匹配 | 候選線索 + 能力模型 | 匹配度總分 + 優勢項 + 缺口項 |
| 5. 尋訪報告 | 全部結果 | 結論先行的尋訪報告 + 72 小時行動清單 |

---

## 📊 匹配度評分

評分只基於公開管道證據，無證據不評分。加權平均 × 20 = 匹配度百分制：

| 匹配度 | 分級 | 行動建議 |
|:--|:---|:---|
| ≥ 85 | **A · 優先尋訪** | 立即觸達，準備定向話術 |
| 70 – 84 | **B · 可培養** | 觸達同時評估缺口項培養成本 |
| 50 – 69 | **C · 謹慎** | 供給緊張時作為替代人選 |
| < 50 | **D · 不匹配** | 不進入尋訪清單 |
| 必備項 ≤ 2 分 | **一票否決** | 無論總分預設 D，除非業務方明確豁免 |

---

## 🚀 快速開始

### 方式一：安裝為專家包（推薦）

把本倉庫作為 WorkBuddy 專家包安裝：

```bash
# 克隆倉庫
git clone https://github.com/xyzln/talent-sourcing-hr.git

# 複製到專家目錄
cp -r talent-sourcing-hr ~/.workbuddy/plugins/marketplaces/my-experts/plugins/

# 註冊（腳本位於 expert-manager 技能的 scripts/ 目錄）
python3 register_expert.py ~/.workbuddy/plugins/marketplaces/my-experts/plugins/talent-sourcing-hr
```

然後在 WorkBuddy 專家中心選擇「**招聘尋訪官**」，直接提業務要求即可。

### 方式二：單獨使用技能

技能目錄 `skills/recruit-web-sourcing/` 可獨立複製到 `~/.workbuddy/skills/` 使用，或在 SkillHub 搜尋 `recruit-web-sourcing` 安裝對應語言版本。

---

## 💬 使用範例

> 我是業務負責人，這是我們的職位需求和業務要求，請全網檢索並精準匹配人才，給出尋訪結論。

> 拆解這個職位的能力模型，給出篩選標準和匹配評分表。

> 彙總近期目標產業的招聘需求動態，輸出人才市場洞察簡報。

---

## 🌐 多語言版本

| 語言 | README | SkillHub 技能 |
|:---|:---|:---|
| 🇨🇳 简体中文 | [README_CN.md](README_CN.md) | `recruit-web-sourcing` |
| 🇹🇼 繁體中文 | [README_TW.md](README_TW.md) | `recruit-web-sourcing-tw` |
| 🇬🇧 English | [README_EN.md](README_EN.md) | `recruit-web-sourcing-en` |
| 🇷🇺 Русский | [README_RU.md](README_RU.md) | `recruit-web-sourcing-ru` |
| 🇸🇦 العربية | [README_AR.md](README_AR.md) | `recruit-web-sourcing-ar` |

各語言版本完整翻譯了 SKILL.md、三份參考文件與評分腳本的輸出文案。

---

## ⚠️ 合規承諾

- 篩選與匹配**只基於職位相關能力與公開管道證據**，不涉及年齡、性別、地域、婚育、戶籍等歧視性維度
- **不編造信源與候選人**，檢索不到會如實說明並給出擴搜建議
- 只使用公開管道資訊，保護候選人隱私
- 所有結論標記信源與取得時間

---

## 📁 倉庫結構

```text
talent-sourcing-hr/
├── README.md                        # 入口（語言切換）
├── README_CN.md / _TW / _EN / _RU / _AR   # 五語言落地頁
├── assets/                          # 配圖
│   ├── hero-agent-temp-worker.jpg   # 人設主圖
│   ├── talent-sourcing-network.jpg  # 全網檢索概念圖
│   └── workflow_{CN,TW,EN,RU,AR}.svg      # 五步流程圖（五語言）
├── .codebuddy-plugin/plugin.json    # 專家包清單
├── agents/talent-sourcing-hr.md     # 專家人格（招聘尋訪官·顧尋）
├── avatars/expert.png               # 專家頭貼
├── skills/recruit-web-sourcing/     # 技能源碼（简体中文）
│   ├── SKILL.md
│   ├── references/                  # 檢索文件 / 匹配模型 / 報告模板
│   └── scripts/match_score.py       # 匹配度計算機
├── i18n/{CN,TW,EN,RU,AR}/           # 五語言技能完整版本
└── LICENSE
```

---

## 📄 開源協議

[MIT](LICENSE) © 2026 talent-sourcing-hr contributors

<div align="center">

**⭐ 覺得好用就點個 Star，讓更多被 agent 碰運氣折磨的人找到這個臨時工**

</div>
