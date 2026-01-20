---
marp: true

theme: HoraStyle
paginate: false
style: |
  :root {
    --title-bg: linear-gradient(90deg, #333333, #000000);
    --title-text-color: #ffffff;
  }
  section.lead {
    background: linear-gradient(135deg, #1a1a1a 0%, #000000 100%);
  }
---

<!-- _class: lead -->

# 企劃

---

# 遊戲玩法

請趕快定調你們的遊戲玩法
除了戰鬥要素低的橫向卷軸以外，沒看到太多想法
但只有這樣其實也可以，可以定調為 **劇情導向的橫向卷軸**
<br>

不要再用多款遊戲名稱舉例的方式來混淆玩法
請確切的講出一款參考作品就好

---

# 關卡 & 腳本

請認真決定三個關卡會出現的內容、人物等等
<br>

接著 撰寫三個關卡要表達的劇情
並且撰寫會出現的 劇情腳本 & 對話
不要流於單純的構想階段
<br>

**所有內容都要記錄下來，才能執行**


---


<!-- _class: lead -->

# 美術

---

# 遊戲畫面示意圖

**所有設計請用1920x1080來製作**

請盡快產出一張**遊戲畫面的示意圖**
如果該圖由AI產出，請務必確認該圖能充分表達遊戲的呈現，例如：

1. 角色大小
1. 人物設計 (&人物動作的可能性)
2. 地板製作方式
3. 背景製作方式

---

# 人物設計
**所有設計請用1920x1080來製作**
<br>

依照示意圖 與 立繪圖
製作可用於遊戲中使用的人物
<br>

並且開始著手動作部分
可以思考是Sprite-sheet模式
或是其他模式

---
# 地板製作
**所有設計請用1920x1080來製作**
<br>

請理解一下TileMap，討論一下是否使用TileMap
(我推薦使用..)

給出一些能用的地板 (視前段討論決定是否TileMap)
讓程式確認地板可用

---
# 場景 & 背景製作
**所有設計請用1920x1080來製作**
<br>

請討論遊戲畫面是否會縱向捲動 / 橫向捲動
是否使用Parallax Scrolling背景

https://www.youtube.com/watch?v=AoRBZh6HvIk


---


<!-- _class: lead -->

# 核心程式

---

# 2D角色控制
1. 利用Rigidbody2D或CharacterController2D來完成
    - 前者比較簡單，後者可以做更多設計
2. 移動 + 跳躍
4. 與物件互動功能
    - 需要思考要有那些互動 (對話/拾取物品？)
3. 是否有縱向捲動或橫向捲動 (推薦CineMachine)


---
# 場景
1. 依照討論，確認是否使用TileMap
2. 確認如何使用Parallax Scrolling背景
https://www.youtube.com/watch?v=AoRBZh6HvIk

---

# 對話系統

1. 如何啟動對話 (角色控制的互動功能)
1. 多段對話 
2. 對話框 & 大頭貼
3. 文字打字機效果。

---

# 其他

以下內容，請留待之後再思考

1. 物件互動
    - 撿道具
    - 開門
    - 進入Cutin
3. QTE戰鬥

---

<!-- _class: lead -->

# UI+流程 程式

---

# 場景相關流程1

<br>

取得一個正確的 <mark> [遊戲引擎]作業3 完成品 </mark>
場景相關

1. 確認目前存在的三個場景
2. 新增一個場景[關卡1]
3. 設法讓「開始遊戲」按鈕能到達該場景
```cs
public class MenuPanel : UIPanelBase
{
    //開始遊戲按鈕事件
    public void OnClick_StartGame()
    {
        this.Hide();
        UIManager.Instance.loadingPanel.LoadScene(UIManager.BATTLE_SCENE);
    }
...
```


---

# 場景相關流程2

建立另一個場景起始程式，可先閱讀
```
Script/Scene/GameSceneBaseScript.cs    //基底
Script/Scene/StartGameScene.cs
Script/Scene/FinishGameScene.cs
Script/Scene/BattleGameScene.cs
```
1. 為剛才建立的新場景，建立一段起始程式碼
2. 讓該段程式碼，可開啟任何一個UI (如:FinishPanel)


---
# UI相關程式

1. 閱讀 UI相關程式碼
```
Scripts/UI/UIPanelBase.cs
Scripts/UI/MenuPanel.cs
```
2. 建立一個新的UI程式碼 OptionPanel.cs，
3. 讓[開始遊戲]場景的Option可開啟該UI。
3. 在左上角放上一個按鈕，點擊會關閉該UI。
4. 嘗試將該UI設定為Popup，而非Panel


