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

### Chapter 13

# 手機部署 

## Horazon
## 手機程式設計

---

<!-- 說明iOS 程式語言、商店、測試的難度 -->

# 平台比較：iOS 很難搞

想把遊戲放到 iPhone 上？先有心理準備。

-   **程式語言**：Swift / Objective-C (用 Unity 開發可以不用碰)。
-   **開發環境**：一定要有 **Mac 電腦** + **Xcode**，缺一不可。
-   **商店**：只能透過 **App Store**，而且審核嚴格、常被退件。
-   **費用**：Apple Developer 帳號 **$99 美金/年**。
-   **測試**：要透過 TestFlight，不能隨手把檔案丟給朋友裝。

*(又貴又麻煩，所以今天我們先不碰 iOS)*

---

<!-- 說明android 程式語言、商店、.apk的狀況  -->

# 平台比較：Android 親民

Android 開放很多。

-   **程式語言**：Java / Kotlin (一樣，用 Unity 不用碰)。
-   **開發環境**：Windows / Mac 都可以。
-   **商店**：Google Play (上架費 **$25 美金，繳一次終身**)。
-   **關鍵優勢**：可以直接輸出 **.apk** 檔案！
    -   不用上架，把檔案放到手機或模擬器就能安裝。
    -   就像在電腦上裝 `.exe` 一樣方便。


---

# 步驟 1：切換平台 (Switch Platform)

Unity 預設是用 PC (Windows/Mac) 模式開發。
我們要切換到 Android。

1.  **File** -> **Build Settings**。
2.  在 Platform 下拉選單選擇 **Android**。
3.  按下右下角的 **Switch Platform** 按鈕。
4.  *(這步會跑很久，因為 Unity 要重新壓縮所有貼圖)*。


---

<!-- 設定起始場景 -->

# 設定起始場景 (Scenes In Build)

打包前，必須先告訴 Unity「要包含哪些場景」。

1.  在 **Build Settings** 視窗上方的 **Scenes In Build** 清單。
2.  把你的場景都拖進去。

![](image-4.png)
> 現在只有一個場景，未來有多個場景時，都要放入，而且第一個場景是打開遊戲先看到的。

---

# 步驟 2：設定 Player Settings

這是你 App 的身分證。

1.  在 Build Settings 視窗左下角，點 **Player Settings**。
2.  展開 **Player** 分頁。

### Company Name & Product Name
-   **Company Name**：你的名字或公司名 (如 `HorazonGame`)。
-   **Product Name**：遊戲顯示在手機上的名稱 (如 `Super Cat`)。

---

# Player Settings

![center width:700px](image-5.png)


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

*(建議先選 Mono 比較快)*

---


# 步驟 3：建置 APK (Build)

我們不接手機、不除錯，直接輸出 .apk 檔。

1.  在 Build Settings 視窗。
2.  按下 **Build** (不是 Build And Run)。
3.  選擇一個資料夾存放 APK (建議開個 `Builds` 資料夾)。
4.  取檔名 `MyGame_v1.apk`。
5.  存檔，開始編譯！

---

# 等待建置 (Building...)

Unity 會開始編譯。
-   Compiling Shader...
-   Building Gradle Project...
-   Packaging APK...

如果一切順利，剛剛指定的 `Builds` 資料夾裡，就會出現一個 **`.apk` 檔案！**

---

# 如果沒有成功...

## 聲明：

### 說實話，我在備課的時候，完全無法確認學校電腦這部分的狀況...
### 如果真得無法建立.apk，就暫時不在課堂上處理了
### 這段處理起來很麻煩 

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

# 步驟 4：安裝到手機

有了 .apk，怎麼放進手機？(這就是直接 Build 的好處)

1.  把 `.apk` 檔傳到手機：用 **USB 拷貝**、**Line 傳給自己**、或丟雲端硬碟。
2.  在手機上點開這個 `.apk` 檔。
3.  手機會警告「**未知的來源**」-> 點 **允許安裝**。
4.  安裝完成，桌面就出現你的遊戲了！

*(同一個檔案也能直接安裝到模擬器，不用上架商店)*

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
3.  直接 **Build** 輸出 `.apk`。
4.  傳到手機、允許 **未知來源** 安裝。

看到自己的遊戲在手機上跑，是開發者最有成就感的一刻！

---

# 下週預告

我們已經能打包了，測試的話，應該會發現無法操控!：

-   **Mobile Input** (手機專用操作)。
-   虛擬搖桿 (Joystick) 或按鈕。
-   多點觸控 (Multi-touch) 概念。

