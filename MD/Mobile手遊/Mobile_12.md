---
marp: true
theme: HoraStyle
paginate: true
style: |
  :root {
    --title-bg: linear-gradient(90deg, #15803d, #22c55e);
    --title-text-color: #ffffff;
  }
  section.lead {
    background: linear-gradient(135deg, #052e16 0%, #000000 100%);
  }
---

<!-- _class: lead -->
<!--_paginate: false-->

### Chapter 12
# 遊戲體感優化 (Audio & VFX)

## Horazon
## 手遊程式設計

---

# 章節目標

-   **Audio**：背景音樂 (BGM) 與 音效 (SFX)
-   **Particle System**：粒子特效 (吃金幣效果)
-   **Cinemachine**：攝影機運鏡

---

# 1. 聲音管理 (Audio Source)

Unity 播放聲音的組件是 **Audio Source**。

-   **背景音樂 (BGM)**：
    1.  在場景建立空物件 `BGM_Player`。
    2.  Add Component -> Audio Source。
    3.  把音樂檔拖入 `AudioClip`。
    4.  勾選 **Loop** (循環播放) 與 **Play On Awake**。

---

# 2. 播放音效 (SFX) - 吃金幣

音效通常是「瞬間」的，例如跳躍聲、吃金幣聲。

修改 `PlayerController`：

```csharp
public AudioSource sfxPlayer; // 音效播放器
public AudioClip coinSound;   // 金幣聲音檔

void OnTriggerEnter2D(Collider2D other)
{
    if (other.tag == "Coin")
    {
        // 播放單次音效 (PlayOneShot)
        // 優點：聲音可以疊加，不會切斷前一次的聲音
        sfxPlayer.PlayOneShot(coinSound);
        
        // ... (原本的加分邏輯) ...
    }
}
```

---

# 3. 粒子特效 (Particle System)

粒子是用來做爆炸、魔法、煙霧的神器。

1.  Hierarchy 右鍵 -> Effects -> **Particle System**。
2.  你會看到一堆白色光點噴出來。
3.  **調整參數**：
    -   **Shape**：改為 Circle (圓形發散)。
    -   **Color over Lifetime**：隨時間變透明。
    -   **Texture Sheet Animation**：如果是像素風，可換成像素顆粒圖。

---

# 4. 生成特效 (Instantiate)

吃金幣時，不只要消失，還要「碰」一聲爆出粒子。

```csharp
public GameObject coinEffect; // 粒子預製物 (Prefab)

void OnTriggerEnter2D(Collider2D other)
{
    if (other.tag == "Coin")
    {
        // 在金幣的位置生成特效
        Instantiate(coinEffect, other.transform.position, Quaternion.identity);
        
        Destroy(other.gameObject);
    }
}
```

<mark>記得把做好的粒子特效存成 Prefab，然後把場景上的刪掉。</mark>

---

# 5. 攝影機跟隨 (Cinemachine)

這學期我們做的是捲軸遊戲，攝影機一定要跟著主角走。
使用 Unity 官方神器：**Cinemachine**。

1.  Window -> Package Manager -> 安裝 Cinemachine。
2.  上方選單 Cinemachine -> **Create 2D Camera**。
3.  場景會出現 `CM vcam1`。
4.  將 **Follow** 欄位，拖入主角 (Player)。
5.  調整 **Lens Size** (畫面遠近)。
6.  調整 **Dead Zone** (緩衝區)，讓鏡頭運鏡更平滑。

---

# 總結

現在你的遊戲：
-   有熱血的 BGM。
-   吃金幣有聽覺 (叮!) 與視覺 (粒子) 的回饋。
-   攝影機會平滑地跟著主角移動，不會死板板。

這些「多汁 (Juicy)」的細節，是區分「作業」與「遊戲」的關鍵！

下一章，我們要來解決最後一個技術難題：**手機沒有鍵盤怎麼玩？**
