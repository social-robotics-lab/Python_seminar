"""
今回の練習問題では、コンソールで遊べる戦闘ゲームを作ってもらいます。
基本的に皆さんの好きに作ってもらってもいいですが、以下の条件を必ず満たしてください。
1. キャラクターのクラスを作り、味方と敵とでそれぞれ継承する
2. 味方は自分を除き何人登場してもいいが、敵は3人以上登場させる
2. プログラムの最後には勝ったか負けたかを明記して終わる
3. 実行ファイルとクラスを定義するファイルは分ける
"""

import time

from exercise2_class import Enemy, MainCharacter

print("戦闘ゲームにようこそ。")
diff_input = input("「簡単」・「普通」・「難しい」から難易度を選択してください: ")
if diff_input == "簡単":
    diff = "easy"
elif diff_input == "普通":
    diff = "normal"
elif diff_input == "難しい":
    diff = "hard"
    
name = input("名前を入力してください: ")
main = MainCharacter(name=name)
print(f"{main.name}はHP{main.hp}と基本攻撃{main.skills.base.damage}を得た！")

enemy_name = ["ダスクファング", "ナイトテラー", "ヴォイドエンフォーサー"]

count = 0
for i in range(len(enemy_name)):
    enemy = Enemy(name=enemy_name[i], difficulty=diff, index=i)
    print(f"敵の{enemy.name}が現れた！")
    time.sleep(2)
    while True:
        print(f"{main.name}のHP: {main.hp} / 敵{enemy.name}のHP: {enemy.hp}")

        if count == 6:
            print(f"{main.name}の特殊攻撃{main.skills.special.damage}を得た。", end=" ")
            if main.skills.special.self_damage != 0:
                print(f"なお、特殊攻撃1回につき自分のHPが{main.skills.special.self_damage}減る。")
            if main.skills.special.self_healing != 0:
                print(f"なお、特殊攻撃1回につき自分のHPが{main.skills.special.self_healing}回復する。")
            time.sleep(2)
        
        # 自分のターン
        if count >= 6:
            attack_type = input("「基本攻撃」と「特殊攻撃」から攻撃を選んで入力してください: ")
            if attack_type == "基本攻撃":
                print(f"{main.name}は{enemy.name}に基本攻撃{main.skills.base.damage}をした！")
                damage = main.attack(type="base")
            else:
                print(f"{main.name}は{enemy.name}に特殊攻撃{main.skills.special.damage}をした！")
                damage = main.attack(type="special")
        else:
            attack_type = input("「基本攻撃」から攻撃を選んで入力してください: ")
            print(f"{main.name}は{enemy.name}に基本攻撃{main.skills.base.damage}をした！")
            damage = main.attack(type="base")
        enemy.get_damage(damage=damage)
        count += 1
        time.sleep(2)
        
        if main.is_dead:
            print("YOU LOSED....")
            exit()
        
        # 敵のターン
        damage = enemy.attack()
        main.get_damage(damage=damage)
        print(f"{enemy.name}は{main.name}に攻撃{enemy.skill.damage}をした！")
        time.sleep(2)
        if enemy.is_dead:
            print(f"敵の{enemy.name}を倒した！")
            time.sleep(2)
            break
    
print("YOU WON!")