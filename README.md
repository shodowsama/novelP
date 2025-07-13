# novelP

## 資料庫

1. 小說詳情

    ```text
    |_小說名稱_|_作者_|_小說分類_|_小說狀態_|_簡介_|_小說url_|_小說ID_|
    ```

2. 小說目錄

    ```text
    |_小說各章url_|_章節名稱_|_章節id_|_小說ID_|
    ```

3. 會員資訊

    ```text
    |_會員ID_|_會員名稱_|_會員帳號_|_會員密碼_|_收藏小說_|_最近點擊小說_|
    ```

## 基礎免費小說網站(不包含會員系統)

```yml
{
  "definitions": {

  },
  "info": {
    "description": "powered by Flasgger",
    "termsOfService": "/tos",
    "title": "A swagger API",
    "version": "0.0.1"
  },
  "paths": {
    "/": {
      "get": {
        "responses": {
          "200": {
            "description": "運行成功"
          },
          "500": {
            "description": "伺服器未開啟"
          }
        },
        "tags": [
          "小說入口網站"
        ]
      }
    },
    "/header": {
      "get": {
        "parameters": [
          {
            "description": "搜尋關鍵字",
            "in": "query",
            "name": "search_key",
            "required": false,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "返回搜尋結果",
            "schema": {
              "properties": {
                "keyward": {
                  "description": "搜尋關鍵字",
                  "type": "string"
                },
                "result": {
                  "description": "搜尋小說結果",
                  "type": "object"
                }
              }
            }
          },
          "500": {
            "description": "伺服器未開啟"
          }
        },
        "summary": "導覽頁\r",
        "tags": [
          "小說網站導覽列"
        ]
      }
    },
    "/menu": {
      "get": {
        "parameters": [
          {
            "description": "小說ID",
            "in": "query",
            "name": "book_id",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "返回小說目錄條目",
            "schema": {
              "properties": {
                "resultM": {
                  "description": "搜尋關鍵字",
                  "type": "string"
                }
              }
            }
          },
          "500": {
            "description": "伺服器未開啟"
          }
        },
        "summary": "當前小說目錄\r",
        "tags": [
          "當前小說目錄"
        ]
      }
    },
    "/ranking": {
      "get": {
        "parameters": [
          {
            "default": 0,
            "description": "小說狀態",
            "in": "query",
            "name": "ranking_status",
            "type": "string"
          },
          {
            "default": 0,
            "description": "小說類型",
            "in": "query",
            "name": "ranking_type",
            "type": "string"
          },
          {
            "default": 1,
            "description": "搜尋關鍵字",
            "in": "query",
            "name": "page",
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "返回搜尋結果",
            "schema": {
              "properties": {
                "book_status_map": {
                  "description": "小說狀態",
                  "type": "string"
                },
                "book_type_map": {
                  "description": "小說類型",
                  "type": "string"
                },
                "page": {
                  "description": "頁數",
                  "type": "string"
                },
                "reply_status": {
                  "description": "當前小說狀態",
                  "type": "string"
                },
                "reply_type": {
                  "description": "當前小說類型",
                  "type": "string"
                },
                "result": {
                  "description": "搜尋小說結果",
                  "type": "object"
                }
              }
            }
          },
          "500": {
            "description": "伺服器未開啟"
          }
        },
        "summary": "小說排行榜\r",
        "tags": [
          "小說排行榜"
        ]
      }
    }
  },
  "swagger": "2.0"
}
```

## 會員系統

## 爬蟲爬取

## 管理員後台創建
