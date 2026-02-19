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
<!-- _paginate: false -->

### Chapter 15

# 手機部署 

## Horazon
## 手機遊戲開發

---

# 複習：遊戲完成

-   [x] 遊戲邏輯 (Game Loop) 完整。
-   [x] 主選單、遊玩、結算皆已串接。
-   [x] 玩家、敵人、UI 皆已實作。

現在，它還只是一個「電腦遊戲」。
今天我們要把它變成真正的**App**！

---

# 本章目標

1.  切換平台至 **Android**。
2.  開啟手機 **Developer Mode** (開發者模式)。
3.  設定 **Player Settings** (Icon, Name)。
4.  輸出 **APK** 檔案。
5.  了解常見建置錯誤 (Build Error)。

---

# 步驟 1：切換平台 (Switch Platform)

Unity 預設是用 PC (Windows/Mac) 模式開發。
我們要切換到 Android。

1.  **File** -> **Build Settings**。
2.  在 Platform 下拉選單選擇 **Android**。
3.  按下右下角的 **Switch Platform** 按鈕。
4.  *(這步會跑很久，因為 Unity 要重新壓縮所有貼圖)*。

---

# 步驟 2：設定 Player Settings

這是你 App 的身分證。

1.  在 Build Settings 視窗左下角，點 **Player Settings**。
2.  展開 **Player** 分頁。

### Company Name & Product Name
-   **Company Name**：你的名字或公司名 (如 `HorazonGame`)。
-   **Product Name**：遊戲顯示在手機上的名稱 (如 `Super Cat`)。

---

# 設定 Icon (圖示)

選一張漂亮的圖當 App 圖示。

1.  在 Player Settings -> **Default Icon**。
2.  點選 Select，選擇你的圖片。
3.  *(Unity 會自動幫你裁切成各種大小)*。

---

# 重要設定：Identification

展開 **Other Settings** -> **Identification**。

### Package Name (套件名稱)
-   這是 App 在 Android 系統裡的**唯一身分證字號**。
-   格式：`com.公司名.產品名` (全小寫)。
-   例如：`com.horazon.supercat`。
-   **絕對不能跟別人重複！**

### Minimum API Level
-   支援的最低 Android 版本。
-   建議設為 **Android 7.0 (Nougat)** 或 8.0，相容性較好。

---

# 重要設定：Configuration

### Scripting Backend
-   **Mono**：建置快，相容性好 (開發測試用)。
-   **IL2CPP**：效能好，安全性高 (上架 Google Play 必選)。
    -   注意：選 IL2CPP 需要花更久時間打包，且需要安裝 NDK。

### Target Architectures
-   如果是 IL2CPP，記得勾選 **ARM64** (支援現代手機)。

*(如果是課堂練習，建議先選 Mono 比較快)*

---

# 步驟 3：手機端設定 (Developer Mode)

你的手機必須允許「被除錯」。

1.  打開手機 **設定** -> **關於手機**。
2.  找到 **版本號碼 (Build Number)**。
3.  **狂按它 7 次**，直到出現「您現在是開發人員！」。
4.  回到上一頁，找到 **系統** -> **開發人員選項**。
5.  開啟 **USB 偵錯 (USB Debugging)**。

---

# 連接手機

1.  用 USB 線連接手機與電腦。
2.  手機會跳出「允許 USB 偵錯嗎？」-> 勾選 **一律允許** 並確定。
3.  回到 Unity Build Settings。
4.  在 **Run Device** 下拉選單中，按 Refresh。
5.  你應該要看到你的手機型號！

*(如果沒看到，可能是驅動程式沒裝，或線材只有充電功能)*

---

# 步驟 4：建置與執行 (Build And Run)

最緊張的時刻。

1.  在 Build Settings 視窗。
2.  按下 **Build And Run**。
3.  選擇一個資料夾存放 APK (建議開個 `Builds` 資料夾)。
4.  取檔名 `MyGame_v1.apk`。
5.  存檔！

---

# 等待建置 (Building...)

Unity 會開始編譯。
-   Compiling Shader...
-   Building Gradle Project...
-   Copying to Device...

如果一切順利，你的手機會**自動黑屏，然後啟動遊戲！**

---

# 常見錯誤：JDK / SDK 找不到？

Q: 跳出視窗說 "JDK not found"？

A:
1.  Edit -> **Preferences** -> **External Tools**。
2.  檢查 **JDK, SDK, NDK** 是否都勾選了 **Installed with Unity**？
3.  如果沒勾，或是路徑是空的 -> 代表你安裝 Unity 時忘了勾 Android Build Support 裡的 OpenJDK。
4.  **解法**：開 Unity Hub -> Installs -> Add Modules -> 補勾。

---

# 常見錯誤：Build 失敗 (Gradle Error)

Q: 紅字一堆 "Gradle Build Failed"？

A:
這通常是路徑或套件名稱問題。
1.  檢查 **Company Name / Product Name** 有沒有中文或怪符號？
2.  檢查 **Package Name** 格式對不對？(`com.xxx.xxx`)
3.  檢查專案路徑有沒有中文？(`D:\我的遊戲\...` -> 母湯)

---

# 輸出純 APK (給朋友玩)

如果你只想輸出 APK 檔，不需要直接跑在手機上。

1.  在 Build Settings 按 **Build** (不要按 Build And Run)。
2.  生成的 `.apk` 檔案，可以用 Line 或雲端傳給朋友。
3.  朋友安裝時手機會警告「未知的來源」，點允許安裝即可。

---

# 優化：螢幕方向 (Orientation)

如果你的遊戲是橫向的，但手機一轉就變直向？

1.  Player Settings -> **Resolution and Presentation**。
2.  **Default Orientation**：
    -   **Portrait**：直向 (如跑酷、益智)。
    -   **Landscape Left/Right**：橫向 (如捲軸動作)。
    -   **Auto Rotation**：自動旋轉。

*(本課程建議鎖定為 Landscape)*

---

# 總結

今天我們成功把遊戲帶出了電腦。

1.  **Switch Platform** 切換到 Android。
2.  設定 **Package Name** 與 **Icon**。
3.  開啟手機 **USB Debugging**。
4.  **Build And Run** 實機測試。

看到自己的遊戲在手機上跑，是開發者最有成就感的一刻！

---

# 下週預告

我們已經能打包了，但 App 只有基本的「點擊」。
下週是最後一堂課，我們要加入：

-   **Mobile Input** (手機專用操作)。
-   虛擬搖桿 (Joystick) 或按鈕。
-   多點觸控 (Multi-touch) 概念。

---

# Q & A

-   USB 連不到手機？
    -   換一條線試試看 (很多線只能充電)。
    -   安裝手機品牌的 USB Driver (Samsung Driver 等)。
-   可以出 iOS 版嗎？
    -   需要 Mac 電腦 + Xcode + Apple 開發者帳號 ($99/年)。
    -   流程比 Android 複雜非常多。

*(助教巡堂協助)*
