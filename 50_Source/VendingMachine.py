from InventoryControl import InventoryControl
from Coffee import Coffee
from Water  import Water
from Tea    import Tea

MAX_ENTRY  = 100  # 最大登録数
INIT_STOCK = 30  # 各初期在庫数

class VendingMachine:
    def __init__(self):
        self.inv = InventoryControl(MAX_ENTRY)
        self.moneyFromCustomer = 0  # お客から預かったお金

    def main(self):
        '自動販売機のシステム'
        self.inv.add(Coffee('BOSS RAINBOW', 130, 'コロンビア'))
        self.inv.add(Coffee('BOSS PREMIUM', 130, 'グアテマラ'))
        self.inv.add(Water('エ ビ ア ン', 100, 'フランス'))
        self.inv.add(Water('おいしい天然水', 120, '富士山麓'))
        self.inv.add(Tea('綾鷹 あやたか ', 180, '緑茶'))
        self.inv.add(Tea('爽 健 美 茶', 180, 'ブレンド茶'))

        self.inv.setInitStock(INIT_STOCK)
        while True:
            print('\n\n◆◆　操作メニュー　◆◆')
            print('\n(1) 商品を購入する')
            print('\n(2) 在庫を確認する')
            print('\n(3) 終了')
            s = self.inputString('\n番号を入力してください。>')

            no = int(s)
            if no == 1:
                self.inv.dispGoodsList()
                self.buying()
            elif no == 2:
                self.inv.dispStockList()
                self.inputEnter('\n表示を確認してください。[Enter]>')
            else:
                return

        self.inv.setInitStock(INIT_STOCK)
        while True:
            print('\n\n◆◆　操作メニュー　◆◆')
            print('\n(1) お金を投入する')
            print('\n(2) 商品を選択する')
            print('\n(3) キャンセル')
            s = self.inputString('\n番号を入力してください。>')

            no = int(s)
            if no == 1:
                self.inv.dispGoodsList()
                self.buying()
            elif no == 2:
                self.inv.dispStockList()
                self.inputEnter('\n表示を確認してください。[Enter]>')
            else:
                return

    def buying(self):
        '商品を購入する'
        money = 0
        while True:
            self.inv.setInitStock(INIT_STOCK)


            s1 = self.inputString('\nお金を投入してください。 >')
            money += int(s1)
            self.moneyFromCustomer = money

            s2 = self.inputString('\n商品を選んでください。>')
            goods = int(s2)

            # 商品購入
            change = self.inv.buying(self.moneyFromCustomer, goods)

            if change < 0:
                continue

            self.moneyFromCustomer = money - change;  # 自販機のお金を減額
            print('\nおつりは')
            if change != 0:
                print('{}円です。'.format(change))
                self.inputEnter('\n商品とおつりをお取りください。[Enter]>')
            else:
                print('ありません。')
                self.inputEnter('\n商品をお取りください。[Enter]>')
            break

    def inputString(self, prompt):
        '文字列を入力する'
        while True:
            line = input(prompt)
            if line != '':
                return line

    def inputEnter(self, prompt):
        'Enterキーを入力する'
        input(prompt)

vendingMachine = VendingMachine()
vendingMachine.main()
