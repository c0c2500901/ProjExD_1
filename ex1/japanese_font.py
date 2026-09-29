import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    # 練習1：スクリーンの準備（問題文の画面サイズに合わせています）
    screen = pg.display.set_mode((800, 900))
    clock = pg.time.Clock()

    # 練習1：背景画像の読み込み
    bg_img = pg.image.load("fig/pg_bg.jpg")
    # 練習8：2枚目の背景画像を左右反転
    bg_img2 = pg.transform.flip(bg_img, True, False)

    # 練習3：こうかとん画像の読み込み & 左右反転
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)

    # 練習10-1, 10-2：Rectの取得と初期位置（横300, 縦200）の設定
    kk_rct = kk_img.get_rect()
    kk_rct.center = (300, 200)

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 練習10-3：キー押下状態の取得
        key_lst = pg.key.get_pressed()

        # 移動量の初期化
        vx = 0
        vy = 0

        # 練習10-4：押下キーに応じた移動量の設定
        if key_lst[pg.K_UP]:
            vy = -1
        if key_lst[pg.K_DOWN]:
            vy = 1
        if key_lst[pg.K_LEFT]:
            vx = -1
        if key_lst[pg.K_RIGHT]:
            vx = 1

        # 練習10-4：Rectの位置更新
        kk_rct.move_ip(vx, vy)

        # 練習5, 9：背景のループ移動用変数の計算 (0 〜 3199)
        x = tmr % 3200

        # 練習5, 7, 8, 9：背景画像の描画（オリジナル1, 反転1, オリジナル2）
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x + 1600, 0])
        screen.blit(bg_img, [-x + 3200, 0])

        # 練習4, 10-5：こうかとんの描画
        screen.blit(kk_img, kk_rct)

        pg.display.update()

        tmr += 1
        # 練習6：FPSを200に変更
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()