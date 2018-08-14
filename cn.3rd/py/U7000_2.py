from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U7000_2 ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7000.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60210",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/U7000   ._SN',
            '',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '',                                     # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_1B9C",         # 03, 3
        "Function_4_3A8D",         # 04, 4
        "Function_5_3AB0",         # 05, 5
        "Function_6_4FFE",         # 06, 6
        "Function_7_77B9",         # 07, 7
        "Function_8_77E9",         # 08, 8
        "Function_9_7823",         # 09, 9
        "Function_10_78F0",        # 0A, 10
        "Function_11_915F",        # 0B, 11
        "Function_12_ABD3",        # 0C, 12
        "Function_13_B0F6",        # 0D, 13
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Sleep(2000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0 op#A
        "\x07\x00#50W#20A………对不起…………\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #1 op#A
        "\x07\x00#50W#25A……对不起……凯文………\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #2 op#A
        (
            "\x07\x00#50W#55A……但是妈妈………\x01",
            "已经……很累了………\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #3 op#A
        (
            "\x07\x00#50W#55A……所以……\x01",
            "…………所以啊……凯文…………\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #4 op#A
        (
            "\x07\x00#50W#60A……就这样………\x01",
            "………和妈妈一起………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("少年")

    AnonymousTalk(    #5
        "\x07\x0C#3S#30W！！！\x02",
    )

    Jump("loc_226")

    label("loc_226")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS420._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS421._CH")
    OP_1D(0xB2)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    Sleep(3000)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("少年")

    AnonymousTalk(    #6
        (
            "\x07\x0C#30W呼、呼、呼、呼……\x02\x03",

            "………………………………\x02\x03",

            "………又来了吗。\x02\x03",

            "可恶，\x01",
            "从那时开始已经过了好几年……\x02\x03",

            "……偏偏是在\x01",
            "姐姐大显身手的日子……\x02\x03",

            "这样下去的话，\x01",
            "不管过多久我也会一直让别人担心……\x02",
        )
    )

    Jump("loc_3A3")

    label("loc_3A3")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("少女")

    AnonymousTalk(    #7
        (
            "\x07\x0C#30W……现在说这些\x01",
            "还有什么用……\x02",
        )
    )

    Jump("loc_3E8")

    label("loc_3E8")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("少年")

    AnonymousTalk(    #8
        "\x07\x0C#30W#3S！！！\x02",
    )

    Jump("loc_419")

    label("loc_419")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(50, 350, -1, -1)
    SetChrName("少年")

    AnonymousTalk(    #9
        (
            "\x07\x0C#30W莉、莉丝……别吓我啊！\x02\x03",

            "你什么时候来的！？\x02",
        )
    )

    Jump("loc_495")

    label("loc_495")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(320, 250, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #10
        (
            "\x07\x0C#30W从刚才开始就在这里了。\x02\x03",

            "明明轮到凯文打扫礼拜堂，\x01",
            "却一直不见你起床。\x02\x03",

            "然后一来就看到你\x01",
            "从噩梦中惊醒的样子。\x02",
        )
    )

    Jump("loc_535")

    label("loc_535")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 350, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #11
        (
            "\x07\x0C#30W是、是吗……\x02\x03",

            "……哈哈，\x01",
            "好像让你担心了。\x02",
        )
    )

    Jump("loc_58D")

    label("loc_58D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(320, 250, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #12
        (
            "\x07\x0C#30W没什么……已经过去了。\x02\x03",

            "凯文不中用\x01",
            "又不是从现在才开始的。\x02",
        )
    )

    Jump("loc_5F5")

    label("loc_5F5")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 350, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #13
        (
            "\x07\x0C#30W哼……你这家伙……\x02\x03",

            "算了，\x01",
            "难得今天是露菲娜姐姐重要的日子。\x02\x03",

            "为了早饭不要迟到，\x01",
            "还是赶快做准备吧。\x02",
        )
    )

    Jump("loc_696")

    label("loc_696")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 250, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #14
        "\x07\x0C#30W……嗯。\x02",
    )

    Jump("loc_6C6")

    label("loc_6C6")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Sleep(1500)
    Sleep(1000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS422._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS423._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    Sleep(3000)
    SetMessageWindowPos(35, 65, -1, -1)
    SetChrName("女孩")

    AnonymousTalk(    #15
        "\x07\x0C#30W……………………………\x02",
    )

    Jump("loc_78E")

    label("loc_78E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 350, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #16
        "\x07\x0C#30W姐姐……！？\x02",
    )

    Jump("loc_7C2")

    label("loc_7C2")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(140, 380, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #17
        "\x07\x0C#30W……姐姐……\x02",
    )

    Jump("loc_7F6")

    label("loc_7F6")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(50, 160, -1, -1)
    SetChrName("露菲娜")

    AnonymousTalk(    #18
        (
            "\x07\x0C#30W早上好。\x01",
            "莉丝、凯文。\x02\x03",

            "呵呵，真早呢。\x01",
            "你们两个是值日生吗？\x02",
        )
    )

    Jump("loc_887")

    label("loc_887")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 380, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #19
        "\x07\x0C#30W是的……\x02",
    )

    Jump("loc_8B7")

    label("loc_8B7")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 350, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #20
        (
            "\x07\x0C#30W为、为什么\x01",
            "起得这么早？\x02\x03",

            "如果不睡好的话，\x01",
            "旅途会很劳累的。\x02\x03",

            "亚尔特利亚\x01",
            "应该离这里很远吧？\x02",
        )
    )

    Jump("loc_946")

    label("loc_946")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(35, 180, -1, -1)
    SetChrName("露菲娜")

    AnonymousTalk(    #21
        (
            "\x07\x0C#30W呵呵，是啊。\x02\x03",

            "有一段时间\x01",
            "不能在这里祈祷了……\x02\x03",

            "我想趁现在好好祈祷一下，\x01",
            "所以这么早就起来了。\x02",
        )
    )

    Jump("loc_9DD")

    label("loc_9DD")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(320, 350, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #22
        "\x07\x0C#30W这算什么啊……\x02",
    )

    Jump("loc_A13")

    label("loc_A13")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 380, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #23
        (
            "\x07\x0C#30W呵呵……真符合姐姐的作风。\x02\x03",

            "……可是……\x01",
            "以后也会这么忙吗？\x02\x03",

            "连这里也不能经常回来……\x02",
        )
    )

    Jump("loc_A9E")

    label("loc_A9E")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Sleep(1500)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS424._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS425._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS426._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS427._CH")
    OP_C5(0x4, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS428._CH")
    OP_C5(0x5, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS429._CH")
    OP_C5(0x6, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS480._CH")
    OP_C5(0x7, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS481._CH")
    OP_C5(0x8, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS482._CH")
    OP_C5(0x9, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS483._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(50, 220, -1, -1)
    SetChrName("露菲娜")

    AnonymousTalk(    #24
        (
            "\x07\x0C#30W嗯……对不起。\x02\x03",

            "因为刚刚当上随从骑士，\x01",
            "最开始肯定忙得\x01",
            "连睡觉的时间都没有了。\x02\x03",

            "等到对工作习惯下来之后，\x01",
            "也许就能腾出一些时间了。\x02",
        )
    )

    Jump("loc_D38")

    label("loc_D38")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 380, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #25
        "\x07\x0C#30W是吗……\x02",
    )

    Jump("loc_D68")

    label("loc_D68")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(450, 200, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #26
        (
            "\x07\x0C#30W……真是的，\x01",
            "那趁现在好好休息一下不好吗。\x02\x03",

            "至少在吃早饭之前\x01",
            "去睡一会儿吧。\x02",
        )
    )

    Jump("loc_DE1")

    label("loc_DE1")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(80, 220, -1, -1)
    SetChrName("露菲娜")

    AnonymousTalk(    #27
        "\x07\x0C#30W凯文……你真无情……\x02",
    )

    Jump("loc_E45")

    label("loc_E45")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(410, 200, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #28
        "\x07\x0C#30W哎……？\x02",
    )

    Jump("loc_E98")

    label("loc_E98")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(45, 220, -1, -1)
    SetChrName("露菲娜")

    AnonymousTalk(    #29
        (
            "\x07\x0C#30W姐姐好不容易有最后一次机会\x01",
            "能够和你们在一起，\x01",
            "你却总嫌我碍事……\x02\x03",

            "呜呜……\x01",
            "是不是教育方法弄错了呢。\x02",
        )
    )

    Jump("loc_F3B")

    label("loc_F3B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(450, 200, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #30
        (
            "\x07\x0C#30W我、我可从来\x01",
            "没说过你碍事吧！？\x02\x03",

            "而且虽然受了你们照顾，\x01",
            "可是教育从何谈起呢！\x02",
        )
    )

    Jump("loc_FB6")

    label("loc_FB6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 380, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #31
        (
            "\x07\x0C#30W……凯文，你太不诚实了。\x02\x03",

            "能和姐姐说话，\x01",
            "明明是让你最高兴的事。\x02",
        )
    )

    Jump("loc_1024")

    label("loc_1024")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(400, 200, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #32
        "\x07\x0C#30W什……！？\x02",
    )

    Jump("loc_1079")

    label("loc_1079")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x4, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x3, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(70, 220, -1, -1)
    SetChrName("露菲娜")

    AnonymousTalk(    #33
        (
            "\x07\x0C#30W哎呀哎呀，真的么？\x02\x03",

            "是吗……\x01",
            "呵呵，是男孩子嘛，难怪了。\x02\x03",

            "因为要掩饰害羞的心情，\x01",
            "才会装出一幅冷淡的样子。\x02",
        )
    )

    Jump("loc_114B")

    label("loc_114B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(270, 380, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #34
        "\x07\x0C#30W这就叫做叛逆期吧。\x02",
    )

    Jump("loc_1185")

    label("loc_1185")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x5, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x4, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(450, 200, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #35
        (
            "\x07\x0C#30W哼……\x01",
            "你们这对只顾自己开心的姐妹……\x02\x03",

            "想将我这\x01",
            "可怜少年的心\x01",
            "玩弄到什么时候……\x02",
        )
    )

    Jump("loc_1232")

    label("loc_1232")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x6, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x5, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(50, 220, -1, -1)
    SetChrName("露菲娜")

    AnonymousTalk(    #36
        (
            "\x07\x0C#30W呵呵……\x01",
            "从那时起已经过了五年吗。\x02\x03",

            "对了，在乘坐列车之前\x01",
            "去街上买点巧克力吧。\x02\x03",

            "当然，\x01",
            "一定得是昆西·贝尔牌的。\x02",
        )
    )

    Jump("loc_1306")

    label("loc_1306")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(420, 200, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #37
        "\x07\x0C#30W啊……\x02",
    )

    Jump("loc_1334")

    label("loc_1334")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 380, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #38
        (
            "\x07\x0C#30W……要说现在的话，\x01",
            "我推荐新出的薄荷巧克力。\x02\x03",

            "虽然口味很浓，\x01",
            "但余味却十分清爽，\x01",
            "总之很不错呢。\x02",
        )
    )

    Jump("loc_13C0")

    label("loc_13C0")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 220, -1, -1)
    SetChrName("露菲娜")

    AnonymousTalk(    #39
        (
            "\x07\x0C#30W呵呵，\x01",
            "虽然那个听起来很好吃，\x01",
            "不过我还是照例想买牛奶巧克力呢。\x02",
        )
    )

    Jump("loc_142B")

    label("loc_142B")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x7, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x6, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(70, 220, -1, -1)
    SetChrName("露菲娜")

    AnonymousTalk(    #40
        "\x07\x0C#30W因为是我们回忆的味道嘛。\x02",
    )

    Jump("loc_1493")

    label("loc_1493")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x8, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x7, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(450, 200, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #41
        "\x07\x0C#30W回、回忆的味道……\x02",
    )

    Jump("loc_14F0")

    label("loc_14F0")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 380, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #42
        (
            "\x07\x0C#30W……………………………\x02\x03",

            "……凯文，你真下流。\x02",
        )
    )

    Jump("loc_154B")

    label("loc_154B")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x4, 0x3, -1, 0, 0)
    OP_C6(0x8, 0x3, 16777215, 400, 0)
    Sleep(800)
    SetMessageWindowPos(450, 200, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #43
        "\x07\x0C#30W#3S为、为什么会变成这样！？\x02",
    )

    Jump("loc_15B1")

    label("loc_15B1")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x6, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x4, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(50, 220, -1, -1)
    SetChrName("露菲娜")

    AnonymousTalk(    #44
        (
            "\x07\x0C#30W呵呵……\x01",
            "那是我们大家回忆的味道呢。\x02\x03",

            "从那时候开始发生了很多事情，\x01",
            "凯文变成了这里的一员，\x01",
            "每天大家都在一起度过……\x02\x03",

            "在这里的每一天的回忆，\x01",
            "都是我们无可替代的宝物。\x02",
        )
    )

    Jump("loc_16B1")

    label("loc_16B1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 380, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #45
        "\x07\x0C#30W姐姐……\x02",
    )

    Jump("loc_16E1")

    label("loc_16E1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(450, 200, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #46
        (
            "\x07\x0C#30W露菲娜姐姐……\x02\x03",

            "…………………………………\x02",
        )
    )

    Jump("loc_173A")

    label("loc_173A")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x9, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x6, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(450, 200, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #47
        (
            "\x07\x0C#30W……那么，\x01",
            "为什么要去当什么骑士呢。\x02\x03",

            "不论怎么想，\x01",
            "我都不觉得那个身份适合姐姐……\x02\x03",

            "当个普通的修女，\x01",
            "到镇上的礼拜堂去工作\x01",
            "不是已经很好了吗……\x02",
        )
    )

    Jump("loc_181F")

    label("loc_181F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 380, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #48
        "\x07\x0C#30W…………………………………\x02",
    )

    Jump("loc_1861")

    label("loc_1861")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS484._CH")
    SetMessageWindowPos(50, 220, -1, -1)
    SetChrName("露菲娜")

    AnonymousTalk(    #49
        (
            "\x07\x0C#30W……对不起。\x02\x03",

            "不过……\x01",
            "因为我似乎有一些天分。\x02\x03",

            "所以干脆就想发挥一下\x01",
            "来为大家做点事情。\x02\x03",

            "呵呵，说不定马上就成为拖后腿的，\x01",
            "丢尽脸面跑回来呢。\x02",
        )
    )

    Jump("loc_1966")

    label("loc_1966")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 400, 0)
    Sleep(800)
    OP_C6(0x9, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(450, 200, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #50
        (
            "\x07\x0C#30W哼……\x02\x03",

            "像姐姐这样老好人一个，\x01",
            "一定担当不起\x01",
            "那么困难的工作啦……\x02\x03",

            "什么时候想回来都可以。\x02",
        )
    )

    Jump("loc_1A17")

    label("loc_1A17")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 380, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #51
        "\x07\x0C#30W………………（无话可说）\x02",
    )

    Jump("loc_1A57")

    label("loc_1A57")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x7, 0x3, -1, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 400, 0)
    Sleep(800)
    SetMessageWindowPos(50, 220, -1, -1)
    SetChrName("露菲娜")

    AnonymousTalk(    #52
        (
            "\x07\x0C#30W呵呵，到那时候，\x01",
            "你们能亲切地欢迎我就好了。\x02\x03",

            "那么──要做扫除的话\x01",
            "就让我也帮个忙吧？\x02\x03",

            "反正机会难得，我们就来把这里的\x01",
            "每一处角落打扫得闪闪发亮吧。\x02",
        )
    )

    Jump("loc_1B46")

    label("loc_1B46")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x7, 0x3, 16777215, 1500, 0)
    Sleep(2000)
    OP_20(0x1388)
    OP_21()
    Sleep(1000)
    OP_C7(0x1, 0xFF, 0x0)
    OP_AD(0x2400E5, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x2504)
    OP_A2(0x2505)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_2_AC end

    def Function_3_1B9C(): pass

    label("Function_3_1B9C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x2602AD, 0x2602B2, 0x13)
    OP_D2(0x2602AC, 0x2602B1, 0x14)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x12, 0, 4000, -1770, 0)
    SetChrPos(0x109, -530, 4000, -2920, 0)
    SetChrPos(0x10F, -1180, 4000, -3890, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x11, 870, 4000, -4110, 0)
    SetChrPos(0x13, -1060, 4000, -5450, 0)
    SetChrPos(0x14, 1700, 4000, -5520, 0)
    SetChrPos(0x15, 200, 4000, -5060, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-950, 4000, -980, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(314000, 0)
    OP_6E(388, 0)
    OP_1D(0xD2)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_1D17():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1D17)

    def lambda_1D2F():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1D2F)

    def lambda_1D47():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_1D47)

    def lambda_1D57():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_1D57)
    OP_8F(0x12, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x12, 19)
    SetChrSubChip(0x12, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    SetChrPos(0x10, 100, 5100, 100, 0)
    PlayEffect(0x1, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_1E40():
        OP_8F(0xFE, 0x64, 0x1770, 0x64, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1E40)
    WaitChrThread(0x10, 0x0)
    Sleep(300)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrPos(0x12, 0, 4000, -490, 0)
    SetChrPos(0x109, -700, 4000, -2150, 0)
    SetChrPos(0x10F, -1450, 4000, -3000, 0)
    SetChrPos(0x11, 580, 4000, -3500, 0)
    SetChrPos(0x13, -1360, 4000, -4700, 0)
    SetChrPos(0x14, 1290, 4000, -4760, 0)
    SetChrPos(0x15, -60, 4000, -4150, 0)
    SetChrChipByIndex(0x12, 4)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x10, 0, 5700, 1000, 0)
    PlayEffect(0x1, 0x0, 0x10, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x10, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1FA3():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1FA3)

    def lambda_1FBB():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1FBB)

    def lambda_1FD3():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1FD3)

    def lambda_1FE3():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1FE3)

    def lambda_1FF3():
        OP_8F(0xFE, 0x0, 0x2008, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1FF3)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_201D():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_201D)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x10, 0, 300, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x10, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    Sleep(300)
    ClearChrFlags(0x16, 0x80)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x16, 0, 8000, 2800, 180)
    SetChrChipByIndex(0x16, 20)
    SetChrSubChip(0x16, 0)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x16, 0x4)
    ClearChrFlags(0x17, 0x80)
    OP_9F(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x17, 0, 8000, 2800, 180)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x17, 0x4)
    PlayEffect(0x6, 0x3, 0x16, 300, 300, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x4, 0x17, 0, 300, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(500)

    def lambda_218D():
        OP_8F(0xFE, 0xFFFFFCE0, 0x1F40, 0xAF0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_218D)

    def lambda_21A8():
        OP_8F(0xFE, 0x3E8, 0x1F40, 0xAF0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_21A8)
    WaitChrThread(0x16, 0x0)
    WaitChrThread(0x17, 0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #53
        0x10F,
        "#1444F#5P有两道光……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x109,
        "#1060F#5P唔……难道说。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetChrFlags(0x10, 0x80)
    OP_E5(0x2, 0xFF, 0x13, 500)
    OP_6D(-2230, 5000, 4310, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(365, 0)
    SetChrPos(0x16, -500, 8000, 2150, 180)
    SetChrPos(0x17, 1000, 8000, 2150, 180)
    PlayEffect(0x6, 0x3, 0x16, 300, 300, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x4, 0x17, 0, 300, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x12, 10, 4000, -490, 0)
    SetChrPos(0x109, -20, 4000, -2410, 0)
    SetChrPos(0x10F, -720, 4000, -3390, 0)
    SetChrPos(0x11, 1210, 4000, -4000, 0)
    SetChrPos(0x13, -660, 4000, -5230, 0)
    SetChrPos(0x14, 2290, 4000, -5300, 0)
    SetChrPos(0x15, 570, 4000, -4900, 0)

    def lambda_243A():
        OP_6D(-1210, 4000, 1510, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_243A)

    def lambda_2452():
        OP_67(0, 4850, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2452)

    def lambda_246A():
        OP_6B(2850, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_246A)

    def lambda_247A():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_247A)

    def lambda_248A():
        OP_8F(0xFE, 0xFFFFFF9C, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_248A)

    def lambda_24A5():
        OP_8F(0xFE, 0x320, 0xFA0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_24A5)
    WaitChrThread(0x16, 0x0)
    WaitChrThread(0x17, 0x0)
    SetChrSubChip(0x16, 0)
    SetChrSubChip(0x17, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    OP_82(0x2, 0x2)
    PlayEffect(0x6, 0x5, 0x16, 300, 300, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x17, 0, 300, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_2550():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_2550)

    def lambda_2562():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_2562)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_0D()
    Sleep(1000)
    PlayEffect(0x4, 0x3, 0x16, 300, 300, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x4, 0x17, 0, 300, 0, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_25F7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_25F7)

    def lambda_2609():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_2609)
    WaitChrThread(0x16, 0x0)
    WaitChrThread(0x17, 0x0)
    Fade(500)
    OP_82(0x5, 0x0)
    OP_82(0x6, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #55
        0x17,
        "#310F#11P啾……？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #56
        0x16,
        "科洛蒂娅公主",
        "#1169F#5P刚、刚才的是……\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0xFFFFFF06, 1200, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    SetChrSubChip(0x16, 1)
    OP_0D()
    Sleep(300)

    NpcTalk(    #57
        0x16,
        "科洛蒂娅公主",
        (
            "#1164F#5P尤莉亚小姐……？\x02\x03",

            "我记得你应该去\x01",
            "参加埃尔赛尤号的演习才对……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x12,
        (
            "#176F#6P……殿下…………\x01",
            "您没事真是太好了……\x02\x03",

            "#171F哈哈，没想到……\x01",
            "连基库也在一起呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x17,
        "#310F#11P啾？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #60
        0x16,
        "科洛蒂娅公主",
        (
            "#1163F#5P哎，那个……\x01",
            "到底是怎么回事……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x16, 0xFFFFFF06, 1200, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x16, 8)
    SetChrSubChip(0x16, 0)
    OP_0D()
    Sleep(300)

    NpcTalk(    #61
        0x16,
        "科洛蒂娅公主",
        "#1164F#11P咦……\x02",
    )

    CloseMessageWindow()

    def lambda_283C():
        OP_6D(-880, 4000, 300, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_283C)

    def lambda_2854():
        OP_67(0, 6060, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2854)

    def lambda_286C():
        OP_6B(2730, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_286C)
    OP_43(0x12, 0x0, 0x2, 0x4)
    Sleep(400)

    def lambda_2888():
        OP_8F(0xFE, 0x0, 0xFA0, 0xFFFFFA60, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2888)
    Sleep(200)

    def lambda_28A8():
        OP_8F(0xFE, 0xFFFFFD44, 0xFA0, 0xFFFFF650, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_28A8)
    Sleep(150)

    def lambda_28C8():
        OP_8F(0xFE, 0x578, 0xFA0, 0xFFFFF63C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_28C8)
    Sleep(150)

    def lambda_28E8():
        OP_8F(0xFE, 0x37A, 0xFA0, 0xFFFFF18C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_28E8)
    Sleep(150)

    def lambda_2908():
        OP_8F(0xFE, 0x898, 0xFA0, 0xFFFFEF98, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2908)
    Sleep(150)

    def lambda_2928():
        OP_8F(0xFE, 0xFFFFFE34, 0xFA0, 0xFFFFEF70, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2928)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x109, 0x3)
    Sleep(500)

    ChrTalk(    #62
        0x109,
        (
            "#1840F#6P哈哈……\x01",
            "久疏问候啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x11,
        (
            "#560F#6P那、那个那个……\x01",
            "好久不见了，科洛丝姐姐！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x13,
        "#277F#6P……………………（点头致意）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x14,
        (
            "#210F#6P哎，那个……\x01",
            "在奇怪的地方又见面了呢。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #66
        0x16,
        "科洛蒂娅公主",
        (
            "#1164F#11P凯文神父……\x01",
            "提妲、穆拉少校，\x01",
            "连乔丝特也在……\x02\x03",

            "#1382F还、还有……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x15,
        (
            "#1513F#6P科洛丝……很久不见了。\x02\x03",

            "#1501F基库也是，\x01",
            "还能这么打起精神来真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #68
        0x16,
        "科洛蒂娅公主",
        (
            "#1382F#11P约、约修亚……\x02\x03",

            "#1165F哈哈……\x01",
            "虽然不知道是怎么回事……\x02\x03",

            "#1168F但如果这是梦的话……\x01",
            "还真是不想醒过来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x17,
        "#311F#11P啾！\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0x16, 290, 4000, -190, 180)
    ClearChrFlags(0x16, 0x40)
    ClearChrFlags(0x16, 0x4)
    SetChrPos(0x17, -200, 4600, 50, 180)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x17, 0x4)
    ClearChrFlags(0x17, 0x1)
    SetChrPos(0x109, 270, 4000, -2029, 0)
    SetChrPos(0x10F, -870, 4000, -2950, 0)
    SetChrPos(0x11, 1260, 4000, -4600, 0)
    SetChrPos(0x12, 1550, 4000, -3380, 0)
    SetChrPos(0x13, -820, 4000, -5200, 0)
    SetChrPos(0x14, 2790, 4000, -5300, 0)
    SetChrPos(0x15, -150, 4000, -4400, 0)
    OP_6D(-1180, 4000, -600, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(315000, 0)
    OP_6E(381, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #70
        0x16,
        "科洛蒂娅公主",
        (
            "#1167F#11P……是这样啊………\x02\x03",

            "#1163F看来现在面临着\x01",
            "不同寻常的事态呢。\x02\x03",

            "虽然异界化的王都\x01",
            "是伪造的这一点值得庆幸……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10F,
        (
            "#1446F#6P……可是，真正的王都\x01",
            "并不一定就能确保平安无事。\x02\x03",

            "#1443F能够将那样广大的空间\x01",
            "毫无二致地再现出来的力量……\x02\x03",

            "我们根本无法判断\x01",
            "到底会给其它地方造成什么影响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x12,
        (
            "#175F#12P莉丝小姐……\x01",
            "何必这样说呢。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #73
        0x16,
        "科洛蒂娅公主",
        (
            "#1167F#11P没关系，听到这样的话，\x01",
            "我也能深刻体会到事态的严重性。\x02\x03",

            "#1162F──我明白了。\x01",
            "就让我也加入探索行动吧。\x02\x03",

            "虽然力量有限，\x01",
            "但我也想给大家帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x17,
        "#310F#5P啾！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x12,
        "#178F#6P殿下，可是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #76
        0x16,
        "科洛蒂娅公主",
        (
            "#1167F#11P抱歉，尤莉亚小姐。\x02\x03",

            "#1382F可是现在王都……\x01",
            "也许整个利贝尔\x01",
            "都被卷进了这个事件中。\x02\x03",

            "如果不能做些什么的话，\x01",
            "王太女这样名不副实的称号，\x01",
            "对我来说就没有任何意义了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x15,
        "#1500F#6P科洛丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x12,
        "#176F#6P………那我只好遵命了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x109,
        (
            "#1840F#6P那么，殿下。\x01",
            "就再次请你多关照了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #80
        0x16,
        "科洛蒂娅公主",
        (
            "#1165F#11P呵呵，彼此彼此，\x01",
            "我也要努力不给大家\x01",
            "扯后腿才行。\x02\x03",

            "#1162F那么……现在的目的地\x01",
            "就是『封印区域』最深处的\x01",
            "传送魔法阵对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x109,
        (
            "#1065F#6P嗯，进入那里之后\x01",
            "应该就可以到达下一个场所了。\x02\x03",

            "#1063F准确的说……\x01",
            "应该是下一个『星层』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x15,
        (
            "#1503F#6P『星层』……\x02\x03",

            "#1502F从你们说的看来，\x01",
            "应该是构成这个『影之国』的概念吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x10F,
        (
            "#1446F#5P女神所在的『天空』。\x01",
            "人类所居住的『地面』。\x01",
            "以及制裁罪人的『炼狱』。\x02\x03",

            "还有，在这三者之间\x01",
            "交织重叠着的\x01",
            "无数个『界』。\x02\x03",

            "#1443F──七耀教会关于世界的概念\x01",
            "和这里似乎很接近。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x13,
        (
            "#272F#6P嗯，也就是说……\x02\x03",

            "#270F越往下走就\x01",
            "越难受到女神的保佑了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    def lambda_335C():
        OP_6D(-900, 3700, -1600, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_335C)
    OP_8C(0x14, 270, 600)
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #85
        0x14,
        (
            "#216F#12P等、等一下……\x01",
            "别说这么不吉利的话嘛！\x02\x03",

            "#413F本来这里就\x01",
            "到处都徘徊着\x01",
            "对心脏不好的怪物了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_33F7():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_33F7)
    Sleep(50)

    def lambda_340A():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_340A)
    Sleep(50)

    def lambda_341D():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_341D)
    Sleep(50)

    def lambda_3430():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3430)
    Sleep(50)

    def lambda_3443():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3443)
    Sleep(50)
    OP_8C(0x12, 135, 400)

    ChrTalk(    #86
        0x13,
        (
            "#278F#5P哼……\x01",
            "你在说什么胆小怕事的话啊。\x02\x03",

            "#277F……对了。\x01",
            "你本来就只是个小丫头嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #87
        0x14,
        "#214F#12P#3S你、你说什么～！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_8C(0x11, 0, 400)

    ChrTalk(    #88
        0x11,
        (
            "#067F#6P哎，那个……\x02\x03",

            "#560F伪造的格兰赛尔\x01",
            "是『第二星层』的话……\x02\x03",

            "下一个地点\x01",
            "应该就是『第三星层』了吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_35BC():
        OP_6D(-1200, 3700, -1000, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_35BC)

    def lambda_35D4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_35D4)
    Sleep(50)

    def lambda_35E7():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_35E7)
    Sleep(50)

    def lambda_35FA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_35FA)
    Sleep(50)

    def lambda_360D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_360D)
    Sleep(50)

    def lambda_3620():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3620)
    Sleep(50)
    OP_8C(0x14, 315, 400)
    WaitChrThread(0xEE, 0x0)
    Sleep(200)

    ChrTalk(    #89
        0x109,
        (
            "#1060F#11P嗯，应该没错。\x02\x03",

            "#1065F先不说『影之王』的目的是什么，\x01",
            "但肯定有什么机关在等着。\x02\x03",

            "#1063F我们最好做好\x01",
            "万全的准备再前进。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x10F,
        "#1802F#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #91
        0x109,
        (
            "#1079F#11P嗯？……怎么了，莉丝？\x02\x03",

            "你注意到什么了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x10F,
        (
            "#1446F#5P………没什么。\x02\x03",

            "#1443F整理好装备之后，\x01",
            "我们就回到封印区域的最深处吧。\x02\x03",

            "还有，\x01",
            "如果有时间的话，\x01",
            "最好调查一下散落在各处的『门』。\x02",
        )
    )

    Jump("loc_3814")

    label("loc_3814")

    CloseMessageWindow()

    ChrTalk(    #93
        0x14,
        (
            "#210F#6P啊，是说那些到处都有的\x01",
            "很显眼的东西对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x15,
        (
            "#1505F#6P看来不是敌人\x01",
            "所设置的东西……\x02\x03",

            "#1500F有必要调查一下。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_38AB():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_38AB)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x2800)
    OP_28(0x2E, 0x1, 0x20)
    OP_28(0x2E, 0x1, 0x40)
    OP_28(0x2E, 0x1, 0x80)
    OP_28(0x2B, 0x4, 0x10)
    OP_28(0x2B, 0x4, 0x20)
    OP_28(0x2C, 0x4, 0x10)
    OP_28(0x2C, 0x4, 0x20)
    OP_28(0x2D, 0x4, 0x10)
    OP_28(0x2D, 0x4, 0x20)
    OP_28(0x2E, 0x4, 0x10)
    OP_28(0x2E, 0x4, 0x20)
    OP_28(0x2F, 0x4, 0x4)
    OP_28(0x2F, 0x4, 0x8)
    OP_28(0x2F, 0x1, 0x1)
    OP_28(0x2F, 0x1, 0x2)
    OP_28(0x2F, 0x1, 0x4)
    OP_3F(0x357, 1)
    OP_DB(0x0, 0x4)
    OP_A2(0x25CA)
    Call(6, 14)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0xF0, 0x80)
    ClearChrFlags(0xF1, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 16640, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x4100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 390, 4000, -1290, 180)
    SetChrPos(0x1, 390, 4000, -1290, 180)
    SetChrPos(0x2, 390, 4000, -1290, 180)
    SetChrPos(0x3, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Call(0, 5)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_3_1B9C end

    def Function_4_3A8D(): pass

    label("Function_4_3A8D")

    OP_8C(0xFE, 90, 400)
    OP_8F(0xFE, 0xFFFFFA24, 0xFA0, 0xFFFFFDA8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_4_3A8D end

    def Function_5_3AB0(): pass

    label("Function_5_3AB0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DC(0x2, 0xFF)
    ClearParty()
    AddParty(0x8, 0xEE, 0xFF)
    AddParty(0xE, 0xEF, 0xFF)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Sleep(2000)
    SetMessageWindowPos(-1, 120, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #95
        (
            "\x07\x0C#30W──第５４３期修炼生，\x01",
            "凯文·格拉汉姆。\x02\x03",

            "以伟大女神之名义，\x01",
            "任命你为『星杯』的随从骑士——\x02",
        )
    )

    Jump("loc_3B67")

    label("loc_3B67")

    CloseMessageWindow()
    OP_56(0x0)
    OP_1D(0xB2)
    OP_AD(0x240121, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #96
        (
            "\x07\x0C#30W──谨受任命。\x02\x03",

            "我发誓让自身的血与肉遵从七耀之理，\x01",
            "将灵魂献给女神。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 120, -1, -1)
    SetChrName("封圣省红衣主教")

    AnonymousTalk(    #97
        (
            "\x07\x0C#30W嗯。\x02\x03",

            "这样年轻就得到任命，\x01",
            "是很难得一见的事情。\x02\x03",

            "不过，我们相信你的天赋\x01",
            "及钻研之心会结出丰硕果实。\x02\x03",

            "今后作为女神的下仆，\x01",
            "请以圣礼守护者的身份继续努力。\x02",
        )
    )

    Jump("loc_3CCD")

    label("loc_3CCD")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_AE(0xC8)
    Sleep(3000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS434._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS435._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS436._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS437._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    Sleep(3000)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #98
        (
            "\x07\x0C#30W嗨，凯文·格拉汉姆。\x02\x03",

            "能够顺利通过\x01",
            "上头的审议真是太好了。\x02\x03",

            "善哉、善哉。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #99
        (
            "\x07\x0C#30W瑟尔纳特教官……\x01",
            "承蒙关照了。\x02\x03",

            "真是没想到\x01",
            "会让身为守护骑士的您\x01",
            "这样高层的人来监督。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #100
        (
            "\x07\x0C#30W呵呵，真是一本正经嘛。\x02\x03",

            "怎么也看不出来是\x01",
            "之前那个独闯封圣省,\x01",
            "喊着『让我当骑士吧』的少年。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #101
        (
            "\x07\x0C#30W哈哈，那个是因为……\x01",
            "我还太年轻了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #102
        (
            "\x07\x0C#30W不管怎么说，\x01",
            "反正当时我正好在场，\x01",
            "所以对你也有点兴趣。\x02\x03",

            "可是，没想到\x01",
            "你原来是露菲娜的家人。\x02\x03",

            "既然如此，\x01",
            "为何不让她引荐你呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #103
        (
            "\x07\x0C#30W那、那是……\x01",
            "因为一些事情……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #104
        (
            "\x07\x0C#30W呵呵，不用解释了。\x02\x03",

            "这样你也终于和我们一样，\x01",
            "成为教会的走狗了。\x02\x03",

            "今后还请多多照顾了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #105
        (
            "\x07\x0C#30W嗯，彼此彼此。\x02\x03",

            "可是，说什么『走狗』，\x01",
            "也太直白了吧？\x02\x03",

            "我可不认为这是适合\x01",
            "说给可爱的新人听的话。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #106
        (
            "\x07\x0C#30W呵呵……\x01",
            "你还会形容自己『可爱』吗。\x02\x03",

            "骑士团的本性\x01",
            "的确如其所形容的那样。\x02\x03",

            "追踪着秘迹的气味，\x01",
            "然后咬断被恶魔蛊惑的异端的喉咙，\x01",
            "将他们撕成碎片……\x02\x03",

            "这不是狗是什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #107
        (
            "\x07\x0C#30W反正我已经被狠狠地吓唬过，\x01",
            "现在更没有理由退缩了。\x02\x03",

            "………可是……………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #108
        (
            "\x07\x0C#30W呵呵，我知道你想说什么。\x02\x03",

            "你只是不希望自己最重要的女性\x01",
            "被以这样的词称呼……\x02\x03",

            "我说的没错吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #109
        (
            "\x07\x0C#30W才、才不是呢。\x02\x03",

            "露菲娜姐姐是……\x01",
            "只是我的恩人而已。\x02\x03",

            "我并没有打算那样……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 380, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #110
        (
            "\x07\x0C#30W『打算那样』……\x01",
            "到底是怎么样呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #111
        "\x07\x0C#30W#3S！！！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #112
        (
            "\x07\x0C#30W露、露菲娜姐姐！？\x02\x03",

            "你不是到雷米菲利亚\x01",
            "执行任务去了吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(280, 300, -1, -1)
    SetChrName("正骑士露菲娜")

    AnonymousTalk(    #113
        (
            "\x07\x0C#30W呵呵……\x01",
            "为了赶上你的就任仪式，\x01",
            "我可是努力的把工作尽快处理完了。\x02\x03",

            "──恭喜你，凯文。\x02\x03",

            "没想到你这么快\x01",
            "就能够独当一面了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #114
        (
            "\x07\x0C#30W露菲娜姐姐……\x02\x03",

            "嘿嘿，\x01",
            "我还差得远呢。\x02\x03",

            "为了早日赶上\x01",
            "姐姐你们，\x01",
            "我还得不断努力才行。\x02",
        )
    )

    Jump("loc_466D")

    label("loc_466D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(280, 300, -1, -1)
    SetChrName("正骑士露菲娜")

    AnonymousTalk(    #115
        (
            "\x07\x0C#30W啊，你还真谦虚。\x02\x03",

            "对了……\x01",
            "你已经告诉莉丝了吗？\x02",
        )
    )

    Jump("loc_46D9")

    label("loc_46D9")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #116
        (
            "\x07\x0C#30W还没，\x01",
            "我打算今晚给她写信。\x02\x03",

            "因为我突然决定\x01",
            "到亚尔特利亚来，\x01",
            "那家伙好像很生气呢。\x02\x03",

            "我得想办法逗她开心才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(280, 300, -1, -1)
    SetChrName("正骑士露菲娜")

    AnonymousTalk(    #117
        (
            "\x07\x0C#30W呵呵，如果有空的话\x01",
            "我们一起回乡吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x3, -1, 400, 0)
    Sleep(800)
    SetMessageWindowPos(280, 300, -1, -1)
    SetChrName("正骑士露菲娜")

    AnonymousTalk(    #118
        (
            "\x07\x0C对了──\x01",
            "谢谢你，爱因。\x02\x03",

            "让你放弃宝贵的假期\x01",
            "特地来照顾这小子。\x02",
        )
    )

    Jump("loc_4854")

    label("loc_4854")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(360, 320, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #119
        (
            "\x07\x0C#30W呵呵，没关系。\x01",
            "用来打发时间也不错。\x02\x03",

            "这家伙不管是武术\x01",
            "还是法术的素质都不错。\x02\x03",

            "不过因为总是实地修炼，\x01",
            "教养方面还差得很远……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x3, 16777215, 400, 0)
    Sleep(800)
    SetMessageWindowPos(280, 300, -1, -1)
    SetChrName("正骑士露菲娜")

    AnonymousTalk(    #120
        (
            "\x07\x0C#30W唉……\x01",
            "我就知道是这样。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #121
        (
            "\x07\x0C#30W哈、哈哈……\x02\x03",

            "——哦，对了！\x01",
            "总务局的人刚才找我有事。\x02\x03",

            "我得去领新的徽章\x01",
            "和房间的钥匙才行。\x02\x03",

            "我先走了，姐姐！\x01",
            "回头见！\x02",
        )
    )

    Jump("loc_4A20")

    label("loc_4A20")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName("正骑士露菲娜")

    AnonymousTalk(    #122
        "\x07\x0C#30W啊……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("正骑士露菲娜")

    AnonymousTalk(    #123
        "\x07\x0C#30W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(320, 280, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #124
        (
            "\x07\x0C#30W呵呵，怎么了？\x02\x03",

            "果然还是不想让家人\x01",
            "参与危险的工作吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("正骑士露菲娜")

    AnonymousTalk(    #125
        (
            "\x07\x0C#30W不……\x01",
            "选择什么样的道路\x01",
            "是那孩子的自由。\x02\x03",

            "……可是……………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(320, 280, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #126
        (
            "\x07\x0C#30W正如你所看好的那样，\x01",
            "他是块好材料，也有相当的毅力。\x02\x03",

            "一定会成为很优秀的骑士的。\x02\x03",

            "对了，露菲娜。\x01",
            "虽然这只是我的感觉……\x02\x03",

            "难道他……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("正骑士露菲娜")

    AnonymousTalk(    #127
        (
            "\x07\x0C#30W……和你一样\x01",
            "身上会显现『圣痕』吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(320, 280, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #128
        (
            "\x07\x0C#30W唔……\x01",
            "虽然你没被选中，但也注意到了啊。\x02\x03",

            "……我再一次觉得\x01",
            "如果你是守护骑士的\x01",
            "一员就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("正骑士露菲娜")

    AnonymousTalk(    #129
        (
            "\x07\x0C#30W呵呵……\x01",
            "就算是好友，这么称赞也太过分了。\x02\x03",

            "我的武术和法术都称不上出色……\x02\x03",

            "能够当上正骑士\x01",
            "已经是很不错了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(320, 280, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #130
        (
            "\x07\x0C#30W会这么想的也只有你了。\x02\x03",

            "那些和『蛇』有关的事件……\x01",
            "可不是靠平常的手段\x01",
            "就能够解决的。\x02\x03",

            "你不是也把它们\x01",
            "漂亮地摆平了吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("正骑士露菲娜")

    AnonymousTalk(    #131
        (
            "\x07\x0C#30W呵呵，那是因为\x01",
            "对方也有通情达理的人，\x01",
            "所以才能够有个了断。\x02\x03",

            "可是，凯文不一样。\x01",
            "他有着我无法企及的\x01",
            "优秀素质。\x02\x03",

            "但是……\x02",
        )
    )

    Jump("loc_4F3B")

    label("loc_4F3B")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    Sleep(1500)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("正骑士露菲娜")

    AnonymousTalk(    #132
        (
            "\x07\x0C#40W……他就是太善良了。\x02\x03",

            "太过善良……\x01",
            "以至于会把自己逼到绝境。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x1388)
    OP_21()
    Sleep(1000)
    OP_AD(0x2400E6, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x2504)
    OP_A2(0x2507)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_5_3AB0 end

    def Function_6_4FFE(): pass

    label("Function_6_4FFE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x270047, 0x27004C, 0x13)
    OP_D2(0x270048, 0x27004D, 0x14)
    OP_D2(0x70074, 0x7007C, 0x15)
    OP_D2(0x70075, 0x7007D, 0x16)
    OP_D2(0x260285, 0x26028A, 0x17)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x109, 0, 4000, -1770, 0)
    SetChrPos(0x10F, -560, 4000, -3010, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x11, 1270, 4000, -2970, 0)
    SetChrPos(0x12, 1870, 4000, -5330, 0)
    SetChrPos(0x13, 430, 4000, -5710, 0)
    SetChrPos(0x14, 2830, 4000, -4170, 0)
    SetChrPos(0x16, 940, 4000, -4120, 0)
    SetChrPos(0x15, -840, 4000, -4250, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-950, 4000, -980, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(314000, 0)
    OP_6E(388, 0)
    OP_1D(0xD2)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_51AD():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_51AD)

    def lambda_51C5():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_51C5)

    def lambda_51DD():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_51DD)

    def lambda_51ED():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_51ED)
    OP_8F(0x109, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x109, 23)
    SetChrSubChip(0x109, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x18, 0x4)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x18, 400, 5300, 0, 0)
    SetChrChipByIndex(0x18, 19)
    SetChrSubChip(0x18, 0)
    PlayEffect(0x1, 0x0, 0x18, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x18, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x19, 0x4)
    OP_9F(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x19, -400, 5300, 0, 0)
    SetChrChipByIndex(0x19, 21)
    SetChrSubChip(0x19, 0)
    PlayEffect(0x1, 0x2, 0x19, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0x19, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_5399():
        OP_8F(0xFE, 0x190, 0x1770, 0x64, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_5399)

    def lambda_53B4():
        OP_8F(0xFE, 0xFFFFFE70, 0x1770, 0x64, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_53B4)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x19, 0x0)
    Sleep(300)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrPos(0x109, 0, 4000, -500, 0)
    SetChrPos(0x10F, -700, 4000, -3010, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x18, 400, 6000, 1000, 0)
    SetChrPos(0x19, -400, 6000, 1000, 0)

    def lambda_546E():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_546E)

    def lambda_5486():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5486)

    def lambda_549E():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_549E)

    def lambda_54AE():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_54AE)

    def lambda_54BE():
        OP_8F(0xFE, 0x3E8, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_54BE)

    def lambda_54D9():
        OP_8F(0xFE, 0xFFFFFC18, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_54D9)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x19, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_5508():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5508)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x4, 0x18, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x5, 0x19, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x4, 0x18, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x5, 0x19, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x1, 0x18, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x3, 0x19, 0, 0, 0, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    WaitChrThread(0x109, 0x1)
    Sleep(500)
    Fade(500)
    OP_E5(0x2, 0xFF, 0x13, 500)
    OP_6D(-2230, 5000, 4310, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(365, 0)
    SetChrPos(0x19, 1000, 8000, 2150, 270)
    SetChrPos(0x18, -500, 8000, 2150, 90)
    SetChrPos(0x109, 0, 4000, -1770, 0)
    SetChrPos(0x10F, -560, 4000, -3010, 0)
    SetChrPos(0x11, 1270, 4000, -2970, 0)
    SetChrPos(0x12, 1870, 4000, -5330, 0)
    SetChrPos(0x13, 430, 4000, -5710, 0)
    SetChrPos(0x14, 2830, 4000, -4170, 0)
    SetChrPos(0x16, 940, 4000, -4120, 0)
    SetChrPos(0x15, -840, 4000, -4250, 0)

    def lambda_5786():
        OP_6D(-1210, 4000, 1510, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5786)

    def lambda_579E():
        OP_67(0, 4850, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_579E)

    def lambda_57B6():
        OP_6B(2850, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_57B6)

    def lambda_57C6():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_57C6)

    def lambda_57D6():
        OP_8F(0xFE, 0x4B0, 0xFA0, 0x532, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_57D6)

    def lambda_57F1():
        OP_8F(0xFE, 0xFFFFFCE0, 0xFA0, 0x532, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_57F1)
    PlayEffect(0x6, 0x1, 0x18, -100, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x3, 0x19, 0, 500, 0, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x19, 0x0)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x19, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    PlayEffect(0x6, 0x5, 0x18, -100, 500, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x19, 0, 700, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_82(0x1, 0x0)
    OP_82(0x3, 0x0)

    def lambda_5909():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_5909)

    def lambda_591B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_591B)
    OP_22(0x99, 0x0, 0x64)
    Sleep(1500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #133
        0x15,
        "#1504F#6P那是……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    PlayEffect(0x4, 0x3, 0x18, -100, 500, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x4, 0x19, 0, 700, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_5AAE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_5AAE)

    def lambda_5AC0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_5AC0)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x19, 0x0)
    Fade(500)
    OP_82(0x5, 0x0)
    OP_82(0x6, 0x0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #134
        0x18,
        "奥利维特皇子",
        "#1544F#5P……唔……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x19,
        "#572F#6P……嗯…………\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    SetChrChipByIndex(0x18, 20)
    SetChrSubChip(0x18, 0)
    Sleep(150)
    SetChrChipByIndex(0x19, 22)
    SetChrSubChip(0x19, 0)
    OP_0D()
    Sleep(300)

    NpcTalk(    #136
        0x18,
        "奥利维特皇子",
        "#1543F#5P……金先生？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x19,
        (
            "#073F#6P皇子……是你啊。\x02\x03",

            "#573F看来……\x01",
            "这应该不是梦了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #138
        0x18,
        "奥利维特皇子",
        (
            "#1545F#5P呵，没错。\x02\x03",

            "#1540F如果是雪拉君也就算了，\x01",
            "没想到梦中相见的人竟然是饮酒的同伴，\x01",
            "这有些不符合我的作风呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x19,
        (
            "#071F#6P哈哈，你还是老样子呢。\x02\x03",

            "#070F不过，我实在不敢\x01",
            "把雪拉扎德当成饮酒的同伴。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #140
        0x18,
        "奥利维特皇子",
        (
            "#1544F#5P宁愿被雪拉君吃掉，\x01",
            "也绝对不能被她的酒量所吞噬。\x02\x03",

            "这是在利贝尔得到的教训之一。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x19,
        (
            "#573F#6P呵呵，\x01",
            "那还真是宝贵的教训呢。\x02\x03",

            "#070F……好了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    SetChrChipByIndex(0x18, 10)
    SetChrSubChip(0x18, 0)
    Sleep(100)
    SetChrChipByIndex(0x19, 11)
    SetChrSubChip(0x19, 0)
    OP_0D()
    Sleep(300)

    def lambda_5DC5():
        OP_6D(-1210, 4000, 510, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5DC5)

    def lambda_5DDD():
        OP_8C(0x18, 180, 400)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_5DDD)
    Sleep(100)
    OP_8C(0x19, 180, 400)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #142
        0x19,
        (
            "#070F#11P……到底是怎么一回事，\x01",
            "你们能够说明一下吗？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #143
        0x18,
        "奥利维特皇子",
        (
            "#1541F#5P就在为久别重逢\x01",
            "而感动地拥抱之前。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x13,
        "#274F#6P真是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x109,
        (
            "#1075F#6P哈哈，不愧是这两人呢。\x02\x03",

            "#1840F就算是在这样的状况下，\x01",
            "也丝毫没有感到震惊呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0x109, 720, 4000, -1550, 0)
    SetChrPos(0x10F, 350, 4000, -2930, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x11, 2750, 4000, -2390, 315)
    SetChrPos(0x12, 3080, 4000, -5090, 0)
    SetChrPos(0x13, 2140, 4000, -3370, 0)
    SetChrPos(0x14, 0, 4000, -4800, 0)
    SetChrPos(0x15, 1120, 4000, -4450, 0)
    SetChrPos(0x16, 3740, 4000, -4210, 315)
    SetChrPos(0x18, 1470, 4000, 670, 180)
    ClearChrFlags(0x18, 0x40)
    ClearChrFlags(0x18, 0x4)
    SetChrPos(0x19, 0, 4000, 620, 180)
    ClearChrFlags(0x19, 0x40)
    ClearChrFlags(0x19, 0x4)
    OP_6D(-20, 4000, -440, 0)
    OP_67(0, 5450, -10000, 0)
    OP_6B(2190, 0)
    OP_6C(314000, 0)
    OP_6E(399, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #146
        0x19,
        "#074F#5P唔……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #147
        0x18,
        "奥利维特皇子",
        (
            "#1544F#11P……唔唔唔………\x01",
            "这到底该怎么办……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x13,
        (
            "#272F#6P虽然很难相信，\x01",
            "但这就是我们所处的状况。\x02\x03",

            "#270F必须先接受这一事实，\x01",
            "才能够进一步思考对策。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #149
        0x18,
        "奥利维特皇子",
        (
            "#1541F#11P啊，穆拉。\x01",
            "你搞错了一件事。\x02\x03",

            "#1540F因为我早就已经\x01",
            "接受这一事实了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x13,
        (
            "#273F#6P……那你为什么还\x01",
            "一副愁眉不展的样子？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #151
        0x18,
        "奥利维特皇子",
        (
            "#1540F#11P呵，那还用说吗。\x02\x03",

            "#1545F约修亚君、科洛蒂娅殿下、\x01",
            "提妲君、乔丝特君……\x02\x03",

            "还有尤莉亚小姐，\x01",
            "以及第一次见面的莉丝君……\x02\x03",

            "#1547F我正在为到底从谁开始\x01",
            "进行再会的拥抱而烦恼。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #152
        0x13,
        "#274F#6P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x11,
        "#067F#6P啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x16,
        (
            "#1382F#6P呵呵……\x01",
            "真是一点也没变呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x14,
        (
            "#413F#6P我说，约修亚……\x02\x03",

            "#212F这家伙真的是\x01",
            "帝国的皇子殿下吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x15,
        (
            "#1514F#6P哈哈……\x01",
            "算是吧。\x02",
        )
    )

    Jump("loc_6419")

    label("loc_6419")

    CloseMessageWindow()

    NpcTalk(    #157
        0x18,
        "奥利维特皇子",
        (
            "#1545F#11P唉……\x01",
            "这个暂且当作玩笑。\x02\x03",

            "#1540F从你们的话看来，\x01",
            "这次事件的谜题\x01",
            "已经有了一些线索。\x02\x03",

            "因此我也十分乐意\x01",
            "加入大家的行动……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x19,
        (
            "#074F#5P……但在那之前，\x01",
            "我有一些要确认的事情。\x02\x03",

            "#070F就是这样。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #159
        0x18,
        "奥利维特皇子",
        (
            "#1541F#11P呵，不愧是金先生。\x02\x03",

            "#1540F看你说话的口气，\x01",
            "似乎和我抱有\x01",
            "相同的疑问呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x109,
        "#1079F#6P……相同的疑问？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x15,
        "#1502F#6P有什么注意到的事情吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x19,
        (
            "#074F#5P是啊……\x01",
            "有几个吧。\x02\x03",

            "#072F首先，是出现过多次的\x01",
            "那个女性幽灵的存在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x12,
        "#178F#6P……是说『她』吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x16,
        (
            "#1162F#6P我记得……\x01",
            "第一次是在伪造的\x01",
            "格兰赛尔城女王宫出现的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x12,
        (
            "#176F#6P嗯……\x01",
            "她把通往殿下所在之处的\x01",
            "钥匙托付给了我们。\x02\x03",

            "#178F可是……\x01",
            "如果说是第一次出现，\x01",
            "那应该是更早的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x109,
        (
            "#1065F#5P……的确。\x02\x03",

            "#1060F我和莉丝最初\x01",
            "被传送到这个场所的时候\x01",
            "听到的声音……\x02\x03",

            "那个似乎也正是\x01",
            "『她』的声音。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x10F,
        "#1446F#5P………是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x11,
        (
            "#062F#6P一开始只有声音，\x01",
            "后来逐渐在我们面前显形……\x02\x03",

            "也许正好符合\x01",
            "那个黑衣哥哥所说的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x109,
        (
            "#1065F#5P嗯，就是所谓的\x01",
            "被『王』夺取了力量的『隐者』……\x02\x03",

            "#1063F以及『庭院之主』这个称谓。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x19,
        (
            "#074F#5P还有，\x01",
            "那里的石碑上刻有\x01",
            "『隐者之庭院』的字样。\x02\x03",

            "#072F从这些来推断……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x13,
        (
            "#277F#6P……这个『据点』本身\x01",
            "应该是和『她』\x01",
            "关系密切的场所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x16,
        "#1164F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x14,
        (
            "#210F#6P原来如此，我有些明白了。\x02\x03",

            "虽然还不清楚原因，\x01",
            "但这里和其它地方不同，有种舒适的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x109,
        (
            "#1075F#5P嗯……有些明朗了。\x02\x03",

            "#1060F看来『她』本来\x01",
            "应该存在于这个场所。\x02\x03",

            "可是由于『影之王』的出现，\x01",
            "她被夺取了力量，变成了那副样子。\x02\x03",

            "而且她不顾所处的困境，\x01",
            "仍然给了我们很多帮助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x15,
        (
            "#1513F#6P……从这种意义上说，\x01",
            "各地出现的石碑\x01",
            "可能也和她有所关联呢。\x02\x03",

            "#1500F因为那些石碑就像是\x01",
            "为了指引我们才被放置在那里的。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #176
        0x18,
        "奥利维特皇子",
        (
            "#1545F#11P对，并且有一件\x01",
            "重要的东西也是如此。\x02\x03",

            "#1540F凯文神父……\x01",
            "就是你所拿着的『方石』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x109,
        "#1079F#6P啊……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #178
        0x18,
        "奥利维特皇子",
        (
            "#1540F#11P我们现在还不能确定\x01",
            "那个『方石』的真实面貌……\x02\x03",

            "但至少很有可能是\x01",
            "和她有着紧密关系的东西。\x02\x03",

            "#1541F怎么样，这串分析？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x109,
        (
            "#1075F#6P……哎呀，真是了不起。\x02\x03",

            "#1840F在这种混乱的情况下，\x01",
            "还能够整理出这么多情报。\x02\x03",

            "可是这样一来……\x01",
            "我们除了单纯的前进，\x01",
            "又多了一个目的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x16,
        (
            "#1383F#6P把『她』的力量夺回来，\x01",
            "然后向她打听详细的事情……\x02\x03",

            "#1160F是这样吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x109,
        (
            "#1065F#5P嗯，你说的没错。\x02\x03",

            "#1063F如果不这样的话……\x01",
            "大概我们是无法与\x01",
            "『影之王』那些人对抗的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x12,
        "#178F#6P……的确。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #183
        0x18,
        "奥利维特皇子",
        (
            "#1541F#11P呼……\x01",
            "这个暂且不说。\x02\x03",

            "#1540F我还有一件\x01",
            "要确认的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x109,
        (
            "#1064F#6P哦……\x01",
            "还有吗？\x02",
        )
    )

    Jump("loc_6EB1")

    label("loc_6EB1")

    CloseMessageWindow()

    NpcTalk(    #185
        0x18,
        "奥利维特皇子",
        (
            "#1545F#11P是啊……\x01",
            "关于『影之王』的事情。\x02\x03",

            "#1540F我就开门见山地问了……\x01",
            "你心里对他的身份有没有结论？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #186
        0x10F,
        "#1445F#6P……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x109,
        "#1840F#6P……为什么问我？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #188
        0x18,
        "奥利维特皇子",
        (
            "#1540F#11P没什么，只是从刚才的话看来，\x01",
            "他好像对你有些执念呢。\x02\x03",

            "#1544F而且他还很熟悉\x01",
            "已经去世的\x01",
            "莉丝君的姐姐……\x02\x03",

            "并且还能够召唤\x01",
            "你们的圣典中\x01",
            "所出现的『恶魔』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x109,
        (
            "#1065F#6P嗯……\x01",
            "你这么一说的确是这样。\x02\x03",

            "#1840F……可是很遗憾，\x01",
            "我还没想到什么。\x02\x03",

            "那些家伙与其说是与我，\x01",
            "不如说是与『星杯骑士团』\x01",
            "敌对的可能性更大。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x10F,
        "#1802F#6P………………………………\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #191
        0x18,
        "奥利维特皇子",
        (
            "#1542F#11P嗯，虽然这么说有些不合适，\x01",
            "不过你们的组织树敌很多，\x01",
            "你的说法也在情理之中……\x02\x03",

            "#1545F唉，\x01",
            "从树敌多的这个角度来说，\x01",
            "我也处于相似的立场呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x13,
        (
            "#272F#6P真是的……\x01",
            "说得好像事不关己一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x15,
        (
            "#1503F#6P……关于敌人身份的讨论\x01",
            "就暂且到这里吧。\x02\x03",

            "#1502F如果能从对方那里\x01",
            "引出更多情报的话就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x109,
        (
            "#1075F#5P嗯，下次再出现的话\x01",
            "一定得问出个所以然来。\x02\x03",

            "#1078F……那么，\x01",
            "我们做好准备\x01",
            "就继续出发吧。\x02\x03",

            "目的地是『第四星层』──\x01",
            "在会合地点前方的传送阵。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(1000)

    ChrTalk(    #195
        0x10F,
        "#1446F#6P………凯文。\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_73B5():
        OP_6D(-70, 4000, -1410, 1200)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_73B5)

    def lambda_73CD():
        OP_8C(0x109, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_73CD)
    Sleep(100)

    def lambda_73E0():

        label("loc_73E0")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_73E0")

    QueueWorkItem2(0x11, 3, lambda_73E0)

    def lambda_73F1():

        label("loc_73F1")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_73F1")

    QueueWorkItem2(0x12, 3, lambda_73F1)
    Sleep(100)

    def lambda_7407():

        label("loc_7407")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_7407")

    QueueWorkItem2(0x13, 3, lambda_7407)

    def lambda_7418():

        label("loc_7418")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_7418")

    QueueWorkItem2(0x16, 3, lambda_7418)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #196
        0x109,
        (
            "#1079F#11P嗯……怎么了？\x02\x03",

            "你还有什么\x01",
            "想说的事情吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x10F,
        (
            "#1446F#6P……不。\x02\x03",

            "#1805F我的身体有些不舒服，\x01",
            "想退出探索行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x109,
        "#1064F#11P哎……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 135, 400)
    Sleep(500)

    ChrTalk(    #199
        0x10F,
        (
            "#1806F#5P对不起大家……\x01",
            "凯文就拜托你们照顾了。\x02\x03",

            "他虽然应该不会乱来，\x01",
            "但总是在关键时刻掉以轻心。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7568():
        OP_6D(40, 4000, -2960, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7568)

    def lambda_7580():
        OP_6B(2400, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7580)
    OP_43(0x10F, 0x0, 0x2, 0x8)

    def lambda_7597():

        label("loc_7597")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_7597")

    QueueWorkItem2(0x109, 3, lambda_7597)

    def lambda_75A8():

        label("loc_75A8")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_75A8")

    QueueWorkItem2(0x14, 3, lambda_75A8)

    def lambda_75B9():

        label("loc_75B9")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_75B9")

    QueueWorkItem2(0x15, 3, lambda_75B9)

    def lambda_75CA():

        label("loc_75CA")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_75CA")

    QueueWorkItem2(0x18, 3, lambda_75CA)

    def lambda_75DB():

        label("loc_75DB")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_75DB")

    QueueWorkItem2(0x19, 3, lambda_75DB)
    Sleep(1500)

    ChrTalk(    #200 op#A
        0x11,
        "#065F#11P#30A莉、莉丝姐姐？\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #201 op#A
        0x14,
        "#213F#11P#17A哎，等一下……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    OP_44(0x109, 0x3)
    OP_44(0x11, 0x3)
    OP_44(0x109, 0x3)
    OP_44(0x12, 0x3)
    OP_44(0x13, 0x3)
    OP_44(0x14, 0x3)
    OP_44(0x15, 0x3)
    OP_44(0x16, 0x3)
    OP_44(0x18, 0x3)
    OP_44(0x19, 0x3)
    Fade(500)
    OP_6D(270, 4000, -1010, 0)
    OP_67(0, 5450, -10000, 0)
    OP_6B(2210, 0)
    OP_6C(314000, 0)
    OP_6E(399, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #202
        0x109,
        "#1079F#11P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x19,
        (
            "#072F#11P……这样好吗？\x01",
            "不跟着追上去。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #204
        0x109,
        (
            "#1064F#6P啊……那个……\x02\x03",

            "#1067F……对不起。\x01",
            "我稍微失陪一会儿。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_44(0x109, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_A2(0x2505)
    NewScene("ED6_DT21/U7001   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_6_4FFE end

    def Function_7_77B9(): pass

    label("Function_7_77B9")

    OP_8C(0xFE, 225, 400)
    OP_8E(0xFE, 0xFFFFF79A, 0xFA0, 0xFFFFF0EC, 0x1388, 0x0)
    OP_8E(0xFE, 0xC8, 0x3E8, 0xFFFFA77C, 0x1388, 0x0)
    Return()

    # Function_7_77B9 end

    def Function_8_77E9(): pass

    label("Function_8_77E9")

    OP_8C(0xFE, 270, 400)
    Sleep(100)
    OP_8E(0xFE, 0xFFFFF79A, 0xFA0, 0xFFFFF0EC, 0xBB8, 0x0)
    OP_8E(0xFE, 0x64, 0x1004, 0xFFFFC964, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_8_77E9 end

    def Function_9_7823(): pass

    label("Function_9_7823")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 390, 4000, -1290, 180)
    SetChrPos(0x1, 390, 4000, -1290, 180)
    SetChrPos(0x2, 390, 4000, -1290, 180)
    SetChrPos(0x3, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_9_7823 end

    def Function_10_78F0(): pass

    label("Function_10_78F0")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_D2(0x260083, 0x260088, 0x13)
    OP_D2(0x260285, 0x26028A, 0x14)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x109, -60, 4000, -1440, 0)
    SetChrPos(0x102, 650, 4000, -2750, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x11, -950, 4000, -3010, 0)
    SetChrPos(0x12, -1390, 4000, -5900, 0)
    SetChrPos(0x13, 100, 4000, -6000, 0)
    SetChrPos(0x14, -2140, 4000, -4920, 0)
    SetChrPos(0x16, -740, 4000, -4410, 0)
    SetChrPos(0x18, 500, 4000, -4520, 0)
    SetChrPos(0x19, 1410, 4000, -5260, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(1220, 4000, -590, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(45000, 0)
    OP_6E(392, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    def lambda_7A9B():
        OP_6D(1760, 4000, 3840, 2000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7A9B)

    def lambda_7AB3():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7AB3)

    def lambda_7ACB():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7ACB)

    def lambda_7ADB():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_7ADB)
    OP_8F(0x109, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x102, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x109, 20)
    SetChrSubChip(0x109, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    ClearChrFlags(0x1A, 0x80)
    OP_9F(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x2)
    ClearChrFlags(0x1A, 0x1)
    SetChrChipByIndex(0x1A, 19)
    SetChrSubChip(0x1A, 0)
    SetChrPos(0x1A, 100, 5400, 0, 0)
    PlayEffect(0x1, 0x0, 0x1A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x1A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_7BF2():
        OP_8F(0xFE, 0x64, 0x1770, 0x64, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_7BF2)
    WaitChrThread(0x1A, 0x0)
    Sleep(300)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x1A, 0, 6000, 1000, 0)

    def lambda_7C74():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7C74)

    def lambda_7C8C():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7C8C)

    def lambda_7CA4():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7CA4)

    def lambda_7CB4():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7CB4)

    def lambda_7CC4():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_7CC4)
    WaitChrThread(0x1A, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_7CEE():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7CEE)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x1A, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x1A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x1A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    OP_20(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_23(0x146)
    Sleep(1000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP001._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP002._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(2000)
    Sleep(1000)
    OP_22(0x2D8, 0x0, 0x64)
    OP_C6(0x1, 0x3, -1, 2000, 0)
    Sleep(2000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    Sleep(1000)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Sleep(3000)
    OP_6D(1090, 5000, 1260, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(33000, 0)
    OP_6E(365, 0)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x3, 0x0)
    SetChrPos(0x109, 100, 4000, -1290, 0)
    SetChrPos(0x1A, -390, 8000, 2150, 180)
    SetChrSubChip(0x1A, 0)
    PlayEffect(0x6, 0x0, 0x1A, -500, 700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    OP_E5(0x2, 0xFF, 0x13, 500)
    OP_1D(0xD2)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_7F4B():
        OP_6D(1730, 4000, 2029, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7F4B)

    def lambda_7F63():
        OP_67(0, 4350, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7F63)

    def lambda_7F7B():
        OP_6B(3200, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7F7B)

    def lambda_7F8B():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_7F8B)

    def lambda_7F9B():
        OP_8F(0xFE, 0xFFFFFE7A, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_7F9B)
    WaitChrThread(0x1A, 0x0)
    SetChrSubChip(0x1A, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    PlayEffect(0x6, 0x1, 0x1A, -500, 700, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_8004():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_8004)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Sleep(1000)

    ChrTalk(    #205
        0x109,
        "#1079F#6P这、这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x102,
        "#1504F#6P……正在睡觉？\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x4, 0x4, 0x1A, -500, 700, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_8194():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_8194)
    OP_82(0x2, 0x2)
    WaitChrThread(0x1A, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #207
        0x1A,
        (
            "#1316F#5P#40W唔……\x01",
            "……呼噜呼噜……\x02\x03",

            "#817F可爱即正义……\x02\x03",

            "可爱是福气……\x02\x03",

            "可爱之愈深，喜爱之愈切……\x02\x03",

            "#1311F嘿嘿……\x01",
            "……古人真是厉害啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #208
        0x109,
        "#1068F#6P这、这是什么格言啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x11,
        "#067F#6P看、看起来一脸幸福的样子呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x102,
        (
            "#1514F#6P哈哈，如果就这样被叫醒的话，\x01",
            "总觉得有点可怜呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x18,
        (
            "#1541F#5P呵呵，那就没办法了。\x02\x03",

            "#1547F就让我陪着一起睡，\x01",
            "把她带往更加美好的桃源乡──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x13,
        (
            "#277F#6P……你要是这么想睡的话，\x01",
            "我就把你打晕过去怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x18,
        "#1544F#5P对不起，我说错话了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x16,
        "#1165F#6P嘻嘻……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x19,
        "#071F#11P哈哈，你还真是一点没变。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x1A,
        "#1316F#5P………嗯…………\x02",
    )

    CloseMessageWindow()
    OP_99(0x1A, 0x0, 0x2, 0x3E8)
    OP_99(0x1A, 0x2, 0x0, 0x3E8)
    Sleep(500)
    OP_99(0x1A, 0x0, 0x3, 0x3E8)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #217
        0x12,
        "#170F#5P……好像醒了。\x02",
    )

    CloseMessageWindow()
    OP_99(0x1A, 0x3, 0x7, 0x3E8)
    Sleep(500)

    ChrTalk(    #218
        0x1A,
        (
            "#813F#5P#40W……哇…………\x01",
            "…………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x102,
        "#1500F#6P很久不见了，亚妮拉丝小姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x11,
        (
            "#560F#6P那、那个……\x01",
            "早上好～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x109,
        (
            "#1066F#6P哈哈……\x01",
            "做了个好梦对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x1A,
        "#814F#5P#40W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_99(0x1A, 0x7, 0x9, 0x3E8)
    Sleep(500)
    OP_99(0x1A, 0x9, 0xD, 0x3E8)
    Sleep(500)
    OP_99(0x1A, 0xD, 0x13, 0x3E8)
    OP_99(0x1A, 0x10, 0x13, 0x3E8)
    Sleep(300)

    ChrTalk(    #223
        0x1A,
        (
            "#1314F#5P#40W嗯……\x01",
            "小提妲、约修亚\x01",
            "还有公主殿下暂且不说……\x02\x03",

            "尤莉亚小姐……\x01",
            "还有那个女孩子看起来也不错……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x14,
        "#213F#6P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x16,
        "#1164F#6P亚妮拉丝小姐……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x1A,
        (
            "#814F#5P#40W啊，不过长得像熊一样的\x01",
            "金先生也很出人意料……\x02\x03",

            "还有凯文先生的刺头，\x01",
            "像海胆一样可爱……\x02\x03",

            "#811F嘿嘿……\x01",
            "好多新的玩偶啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #227
        0x102,
        (
            "#1512F#6P她好像把我们\x01",
            "和等身大的玩偶弄混了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x109,
        "#1068F#6P睡、睡得这么迷糊……\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0x109, -140, 4000, -2170, 0)
    SetChrPos(0x102, 720, 4000, -3150, 0)
    SetChrPos(0x11, -1420, 4000, -3440, 0)
    SetChrPos(0x12, -1800, 4000, -5800, 0)
    SetChrPos(0x13, -400, 4000, -5850, 0)
    SetChrPos(0x14, -2500, 4000, -4800, 0)
    SetChrPos(0x16, -710, 4000, -4290, 0)
    SetChrPos(0x18, 500, 4000, -4400, 0)
    SetChrPos(0x19, 950, 4000, -5300, 0)
    SetChrPos(0x1A, 90, 4000, -340, 180)
    ClearChrFlags(0x1A, 0x40)
    ClearChrFlags(0x1A, 0x4)
    ClearChrFlags(0x1A, 0x2)
    SetChrFlags(0x1A, 0x1)
    SetChrChipByIndex(0x1A, 12)
    SetChrSubChip(0x1A, 0)
    OP_6D(1230, 4000, -1300, 0)
    OP_67(0, 5200, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(45000, 0)
    OP_6E(381, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #229
        0x1A,
        (
            "#1316F#5P唉，真是遗憾啊……\x02\x03",

            "我还以为好不容易\x01",
            "得到了新的玩偶伙伴呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x102,
        "#1508F#6P亚妮拉丝小姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x109,
        (
            "#1068F#6P都已经将整个事情说明了，\x01",
            "你的第一句话竟然是这个吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x1A,
        (
            "#1315F#5P哈哈，我明白我明白。\x02\x03",

            "#812F虽然还有点不太相信……\x01",
            "不过看大家这么认真，我就知道了。\x02\x03",

            "#815F不管怎么说，看到这么可爱的小提妲，\x01",
            "就是最好的证明了！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #233
        0x11,
        "#067F#6P啊哇……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x109,
        (
            "#1075F#6P唉，你能明白就好。\x02\x03",

            "#1060F那么，你打算怎么办呢？\x01",
            "要和我们一起行动吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x1A,
        (
            "#816F#5P嗯，当然了！\x02\x03",

            "这样的异常事态，\x01",
            "我作为游击士怎么能放手不管呢！\x02\x03",

            "#817F而且……\x01",
            "听你们说，卢·洛克尔训练场\x01",
            "不是变成了奇怪的状态吗。\x02\x03",

            "#812F那么也许其他的游击士们\x01",
            "也遭遇到了同样的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x12,
        "#176F#6P原来如此……说得有道理。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x11,
        "#065F#6P其、其他的游击士……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x102,
        (
            "#1503F#5P嗯……\x01",
            "能够想到的有不少呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x109,
        (
            "#1065F#5P总之，\x01",
            "这只是最初的『训练场』而已。\x02\x03",

            "#1060F现在应该已经可以\x01",
            "前往新的地点，\x01",
            "我们做好准备就出发吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x102,
        "#1500F#6P嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x18,
        (
            "#1541F#6P呵……\x01",
            "这不是很有趣吗。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8FAD():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8FAD)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x2905)
    OP_28(0x33, 0x4, 0x4)
    OP_28(0x33, 0x4, 0x8)
    OP_3F(0x35A, 1)
    OP_3F(0x32C, 1)
    OP_3E(0x32D, 1)
    OP_DB(0x0, 0x9)
    OP_A2(0x25CF)
    Call(6, 18)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    ClearChrFlags(0xF0, 0x80)
    ClearChrFlags(0xF1, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 258, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x102, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 390, 4000, -1290, 180)
    SetChrPos(0x1, 390, 4000, -1290, 180)
    SetChrPos(0x2, 390, 4000, -1290, 180)
    SetChrPos(0x3, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Call(0, 8)
    Call(0, 6)
    Call(0, 9)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_10_78F0 end

    def Function_11_915F(): pass

    label("Function_11_915F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_D2(0x270033, 0x270038, 0x13)
    OP_D2(0x270034, 0x270039, 0x14)
    OP_D2(0x260285, 0x26028A, 0x15)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x109, -320, 4000, -2790, 0)
    SetChrPos(0x102, -1330, 4000, -3360, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x11, 1030, 4000, -3520, 0)
    SetChrPos(0x12, 1540, 4000, -6410, 0)
    SetChrPos(0x13, 80, 4000, -6280, 0)
    SetChrPos(0x14, 2320, 4000, -5750, 0)
    SetChrPos(0x16, 730, 4000, -4710, 0)
    SetChrPos(0x18, -570, 4000, -4740, 0)
    SetChrPos(0x19, -1600, 4000, -5240, 0)
    SetChrPos(0x1A, 2400, 4000, -4510, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(-950, 4000, -980, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(314000, 0)
    OP_6E(388, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    def lambda_932A():
        OP_6D(-1180, 4000, 2780, 2000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_932A)

    def lambda_9342():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9342)

    def lambda_935A():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_935A)

    def lambda_936A():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_936A)
    OP_8F(0x109, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x102, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x109, 21)
    SetChrSubChip(0x109, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    ClearChrFlags(0x1B, 0x80)
    OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x1B, 0x4)
    SetChrFlags(0x1B, 0x1)
    SetChrChipByIndex(0x1B, 19)
    SetChrSubChip(0x1B, 0)
    SetChrPos(0x1B, 0, 5200, 100, 0)
    PlayEffect(0x1, 0x0, 0x1B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x1B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_947C():
        OP_8F(0xFE, 0x0, 0x1770, 0x64, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_947C)
    WaitChrThread(0x1B, 0x0)
    Sleep(300)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x1B, 0, 6000, 1000, 0)

    def lambda_94FE():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_94FE)

    def lambda_9516():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9516)

    def lambda_952E():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_952E)

    def lambda_953E():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_953E)

    def lambda_954E():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_954E)
    WaitChrThread(0x1B, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_9578():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9578)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x1B, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x1B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x1B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    OP_20(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_23(0x146)
    Sleep(1000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP002._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP003._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(2000)
    Sleep(1000)
    OP_22(0x2D8, 0x0, 0x64)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    Sleep(1000)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Sleep(3000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x3, 0x0)
    OP_6D(-2230, 5000, 4310, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(315000, 0)
    OP_6E(365, 0)
    SetChrPos(0x109, -220, 4000, -1910, 0)
    SetChrPos(0x11, 800, 4000, -3520, 0)
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 390, 3700, 1800, 180)
    SetChrPos(0x1B, 390, 8000, 2150, 180)
    SetChrSubChip(0x1B, 0)
    PlayEffect(0x6, 0x0, 0x1B, 300, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    OP_E5(0x2, 0xFF, 0x13, 500)
    OP_1D(0xD2)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_9807():
        OP_6D(-1510, 4000, 800, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9807)

    def lambda_981F():
        OP_67(0, 4850, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_981F)

    def lambda_9837():
        OP_6B(3200, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9837)

    def lambda_9847():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_9847)

    def lambda_9857():
        OP_8F(0xFE, 0x186, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_9857)
    WaitChrThread(0x1B, 0x0)
    SetChrSubChip(0x1B, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    PlayEffect(0x6, 0x1, 0x1B, 300, 300, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_98C0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_98C0)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #242
        0x109,
        "#1079F#6P哎，咦……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x102,
        "#1502F#6P不是雪拉姐姐吗……？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    PlayEffect(0x4, 0x4, 0x1B, 300, 300, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_9970():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_9970)
    OP_82(0x2, 0x2)
    WaitChrThread(0x1B, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #244
        0x1B,
        "#1525F#11P……唔、唔……\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #245
        0x11,
        "#064F啊#6P……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x102,
        "#1504F#6P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x16,
        "#1164F#6P哎呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x18,
        "#1543F#6P……哦哦………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x19,
        (
            "#070F#6P唔……\x01",
            "把头发剪短了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x1A,
        (
            "#811F#6P嗯，\x01",
            "好像是一个月之前剪短的。\x02\x03",

            "#1310F而且为了配合新发型，\x01",
            "连工作服装也换了新的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #251
        0x1B,
        (
            "#1532F#11P哼，真是奇怪……\x02\x03",

            "这种程度的酒\x01",
            "竟然会让我感到眩晕……\x02\x03",

            "#1526F……不行，这点小事算得了什么！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x1B, 20)
    SetChrSubChip(0x1B, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #252
        0x1B,
        (
            "#1524F#3S#11P快，爱娜！\x01",
            "今晚我们就来一决胜负──\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #253
        0x1B,
        (
            "#1523F#11P哎呀……？\x02\x03",

            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x102,
        (
            "#1513F#6P……雪拉姐姐。\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x1B, 13)
    SetChrSubChip(0x1B, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #255
        0x1B,
        (
            "#1523F#11P约修亚……！？\x02\x03",

            "#1521F你什么时候回来的……\x01",
            "艾丝蒂尔在哪儿？\x02\x03",

            "#1536F话说回来，\x01",
            "你好像又结实了不少嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x102,
        "#1514F#6P哈哈……谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x18,
        (
            "#1545F#6P啊啊……\x01",
            "可不要忘了我啊。\x02\x03",

            "#1540F我这个雪拉君忠实的仆人，\x01",
            "永远的偷心小贼！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x1B,
        (
            "#1523F#11P奥、奥利维尔……！？\x02\x03",

            "……等一下，\x01",
            "怎么有这么多熟悉的面孔……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x1B, 90, 400)
    Sleep(500)
    OP_8C(0x1B, 0, 400)
    Sleep(500)
    OP_8C(0x1B, 270, 400)
    Sleep(500)

    ChrTalk(    #259
        0x1B,
        (
            "#1525F#5P而、而且\x01",
            "周围的情况这么奇怪……\x02\x03",

            "#1524F啊啊，到底是怎么回事啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x1A,
        (
            "#819F#6P前辈、前辈。\x01",
            "请先冷静一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x16,
        (
            "#1165F#6P呵呵……\x01",
            "这么吃惊也是情有可原。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x14,
        "#210F#6P嗯，这才是普通的反应嘛。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_63(0x1B)
    SetChrPos(0x109, 270, 4000, -2029, 0)
    SetChrPos(0x102, -570, 4000, -2720, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x11, 2320, 4000, -3080, 315)
    SetChrPos(0x12, 2370, 4000, -5810, 0)
    SetChrPos(0x13, 910, 4000, -5690, 0)
    SetChrPos(0x14, 3660, 4000, -5200, 315)
    SetChrPos(0x16, 1810, 4000, -4220, 0)
    SetChrPos(0x18, 220, 4000, -4110, 0)
    SetChrPos(0x19, -770, 4000, -4950, 0)
    SetChrPos(0x1A, 3970, 4000, -3980, 315)
    SetChrPos(0x1B, 290, 4000, -190, 180)
    ClearChrFlags(0x1B, 0x40)
    ClearChrFlags(0x1B, 0x4)
    SetChrChipByIndex(0x1B, 13)
    SetChrSubChip(0x1B, 0)
    SetChrFlags(0x10, 0x80)
    OP_6D(-430, 4000, -900, 0)
    OP_67(0, 5290, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(315000, 0)
    OP_6E(381, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #263
        0x1B,
        (
            "#1526F#11P咳咳……\x01",
            "事情我大概明白了。\x02\x03",

            "#1534F可是，一般来说\x01",
            "这可不是能够轻易相信的事情。\x02\x03",

            "反倒是用喝醉之后做的梦\x01",
            "或者是露茜奥拉姐姐的幻术\x01",
            "解释起来更有说服力，不是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x109,
        (
            "#1840F#6P哈哈……\x01",
            "你会这么想也不是没道理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x18,
        (
            "#1546F哦哦，这是何等的悲剧！\x02\x03",

            "#1544F雪拉君看到我\x01",
            "竟然不相信这是真的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x1B,
        (
            "#1525F#11P好了好了。\x01",
            "我都说是『一般来说』了。\x02\x03",

            "#1527F再说，\x01",
            "谁会用这么乱来的幻术啊。\x02\x03",

            "如果是做梦的话，\x01",
            "逻辑也太过严密了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x19,
        "#071F#6P哈哈，没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x109,
        (
            "#1075F#6P你能相信真是太好了。\x02\x03",

            "#1060F那么你也赶快来\x01",
            "加入我们吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x1B,
        (
            "#1520F#11P嗯，当然了。\x02\x03",

            "#1526F从你们的叙述来看，\x01",
            "艾丝蒂尔好像也被卷进来了。\x02\x03",

            "#1536F不管是作为游击士还是姐姐，\x01",
            "我当然乐意助一臂之力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x102,
        "#1501F#6P雪拉姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x18,
        (
            "#1541F呵，不愧是雪拉君。\x01",
            "还是这么爽快。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x109,
        (
            "#1077F#6P那真是帮了我们的大忙了。\x02\x03",

            "#1078F──现在的状况\x01",
            "就如之前所说的一样。\x02\x03",

            "现在我们正在进行\x01",
            "对『第四星层』的探索。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x1B,
        (
            "#1526F#11P嗯……\x01",
            "是卢·洛克尔的训练场吗。\x02\x03",

            "几年前我也曾经作为训练生\x01",
            "在那里进行过修炼呢。\x02\x03",

            "#1522F从这层意义上来说……\x01",
            "也许被设置在那里的人物\x01",
            "都是曾经参加过训练的人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x19,
        (
            "#072F#6P原来如此……\x01",
            "这种可能性很高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x1A,
        (
            "#1317F#6P艾丝蒂尔当然不用说……\x02\x03",

            "克鲁茨前辈、格拉茨前辈、\x01",
            "卡露娜前辈也可以算在内呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x1B,
        (
            "#1526F#11P唔，那可说不好。\x02\x03",

            "#1520F那三个人好像只是\x01",
            "作为教官去过那里。\x02\x03",

            "我记得他们三个\x01",
            "都没有单纯作为训练生\x01",
            "而使用过那个训练场吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x1A,
        "#814F#6P是这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x11,
        (
            "#065F#6P请、请问，雪拉姐姐……\x02\x03",

            "阿加特大哥哥\x01",
            "使用过那个训练场吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_A7A5():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_A7A5)
    Sleep(50)

    def lambda_A7B8():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A7B8)
    Sleep(50)

    def lambda_A7CB():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A7CB)
    Sleep(50)

    def lambda_A7DE():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_A7DE)
    Sleep(50)

    def lambda_A7F1():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_A7F1)
    Sleep(400)

    ChrTalk(    #279
        0x1B,
        (
            "#1526F#5P嗯……应该用过。\x02\x03",

            "#1534F据说当时卡西乌斯老师巧妙地引他上钩，\x01",
            "结果在那里吃了大苦头呢。\x02\x03",

            "好像是大约四年前吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x11,
        (
            "#063F#6P是、是这样啊……\x02\x03",

            "#562F艾丝蒂尔姐姐和阿加特大哥哥\x01",
            "都有可能被抓起来了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x102,
        "#1503F#5P提妲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x16,
        (
            "#1383F#6P……没关系的。\x02\x01",

            "#1168F一定没关系的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x12,
        (
            "#170F#6P总之……\x01",
            "三个『训练场』\x01",
            "只剩下一个没去过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x13,
        (
            "#278F#6P嗯……\x02\x03",

            "#277F到底是谁被关在里面，\x01",
            "只要去了就能知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x109,
        (
            "#1060F#5P嗯，准备好了\x01",
            "就继续出发吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AA1C():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AA1C)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x290A)
    OP_28(0x34, 0x4, 0x4)
    OP_28(0x34, 0x4, 0x8)
    OP_3F(0x35B, 1)
    OP_3F(0x32D, 1)
    OP_3E(0x32E, 1)
    OP_DB(0x0, 0x2)
    OP_A2(0x25C8)
    Call(6, 12)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    ClearChrFlags(0xF0, 0x80)
    ClearChrFlags(0xF1, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 258, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x102, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 390, 4000, -1290, 180)
    SetChrPos(0x1, 390, 4000, -1290, 180)
    SetChrPos(0x2, 390, 4000, -1290, 180)
    SetChrPos(0x3, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Call(0, 8)
    Call(0, 6)
    Call(0, 9)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_11_915F end

    def Function_12_ABD3(): pass

    label("Function_12_ABD3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_D2(0x70054, 0x7005C, 0x13)
    OP_D2(0x70055, 0x7005D, 0x14)
    OP_D2(0x60119, 0x6011E, 0x15)
    OP_D2(0x260285, 0x26028A, 0x16)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    LoadEffect(0x3, "map\\mp253_02.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    LoadEffect(0x5, "map\\mp253_05.eff")
    LoadEffect(0x6, "map\\mp253_04.eff")
    SetChrPos(0x109, -90, 4000, -2980, 0)
    SetChrPos(0x102, 1080, 4000, -3580, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x11, -1450, 4000, -4380, 0)
    SetChrPos(0x12, -1100, 4000, -6420, 0)
    SetChrPos(0x13, 250, 4000, -6490, 0)
    SetChrPos(0x14, -2040, 4000, -5910, 0)
    SetChrPos(0x16, -410, 4000, -4920, 0)
    SetChrPos(0x18, 820, 4000, -5000, 0)
    SetChrPos(0x19, 2100, 4000, -6330, 0)
    SetChrPos(0x1A, 2270, 4000, -4300, 0)
    SetChrPos(0x1B, 1650, 4000, -5520, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(1220, 4000, -590, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(45000, 0)
    OP_6E(392, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    def lambda_ADBE():
        OP_6D(1760, 4000, 3840, 2000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_ADBE)

    def lambda_ADD6():
        OP_67(0, 5490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ADD6)

    def lambda_ADEE():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_ADEE)

    def lambda_ADFE():
        OP_6E(403, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_ADFE)
    OP_8F(0x109, 0x0, 0xFA0, 0xFFFFFE16, 0x3E8, 0x0)
    WaitChrThread(0x102, 0x0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x109, 22)
    SetChrSubChip(0x109, 0)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(100)
    ClearChrFlags(0x1C, 0x80)
    OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x1)
    SetChrChipByIndex(0x1C, 19)
    SetChrSubChip(0x1C, 0)
    SetChrPos(0x1C, 100, 5400, 0, 0)
    PlayEffect(0x1, 0x0, 0x1C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x1C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    OP_E5(0x2, 0xFF, 0x13, 1000)
    OP_0D()
    Fade(1000)
    OP_E5(0x2, 0xFF, 0x13, 700)
    OP_0D()

    def lambda_AF10():
        OP_8F(0xFE, 0x0, 0x1770, 0x64, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_AF10)
    WaitChrThread(0x1C, 0x0)
    Sleep(300)
    Fade(1000)
    OP_6D(0, 5000, 3260, 0)
    OP_67(0, 3980, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(363, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x1C, 0, 6000, 1000, 0)

    def lambda_AF92():
        OP_6D(0, 7500, 3760, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AF92)

    def lambda_AFAA():
        OP_67(0, 1650, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AFAA)

    def lambda_AFC2():
        OP_6B(2700, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AFC2)

    def lambda_AFD2():
        OP_6E(363, 3500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AFD2)

    def lambda_AFE2():
        OP_8F(0xFE, 0x0, 0x2134, 0xAF0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_AFE2)
    WaitChrThread(0x1C, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_B00C():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B00C)
    OP_22(0x147, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0x1C, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_23(0x147)
    Fade(500)
    OP_22(0xC, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x1C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    Sleep(300)
    PlayEffect(0x6, 0x3, 0x1C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/U5100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_ABD3 end

    def Function_13_B0F6(): pass

    label("Function_13_B0F6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x70054, 0x7005C, 0x13)
    OP_D2(0x70055, 0x7005D, 0x14)
    OP_D2(0x70061, 0x70069, 0x15)
    OP_D2(0x60119, 0x6011E, 0x16)
    OP_D2(0x2602CA, 0x2602CF, 0x17)
    LoadEffect(0x3, "map\\mp253_04.eff")
    LoadEffect(0x4, "map\\mp253_03.eff")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x11, -400, 4000, -1900, 0)
    SetChrPos(0x109, 190, 4000, -3230, 0)
    SetChrPos(0x102, -1570, 4000, -3620, 0)
    SetChrPos(0x12, -2190, 4000, -6100, 0)
    SetChrPos(0x13, -720, 4000, -6410, 0)
    SetChrPos(0x14, -2800, 4000, -5090, 0)
    SetChrPos(0x16, -1180, 4000, -4830, 0)
    SetChrPos(0x18, 180, 4000, -4830, 0)
    SetChrPos(0x19, 1550, 4000, -6200, 0)
    SetChrPos(0x1A, 1540, 4000, -3560, 0)
    SetChrPos(0x1B, 1250, 4000, -5170, 0)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(1090, 5000, 1260, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(365, 0)
    ClearChrFlags(0x1C, 0x80)
    OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x1)
    SetChrPos(0x1C, -390, 8000, 2150, 180)
    SetChrChipByIndex(0x1C, 19)
    SetChrSubChip(0x1C, 0)
    PlayEffect(0x3, 0x0, 0x1C, -400, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x50)
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, -390, 3700, 1900, 180)
    OP_E5(0x2, 0xFF, 0x13, 500)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_B336():
        OP_6D(1730, 4000, 2029, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B336)

    def lambda_B34E():
        OP_67(300, 4350, -10300, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B34E)

    def lambda_B366():
        OP_6B(3200, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B366)

    def lambda_B376():
        OP_6E(327, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_B376)

    def lambda_B386():
        OP_8F(0xFE, 0xFFFFFE7A, 0xFA0, 0x866, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_B386)
    WaitChrThread(0x1C, 0x0)
    SetChrSubChip(0x1C, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)
    PlayEffect(0x3, 0x1, 0x1C, -400, 500, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)

    def lambda_B3EF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_B3EF)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #286
        0x11,
        "#560F#6P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x102,
        "#1501F#6P呵呵，太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x109,
        (
            "#1071F#6P嗯嗯。\x01",
            "这头红发还是这么鲜艳呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    PlayEffect(0x4, 0x4, 0x1C, -400, 500, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)

    def lambda_B4C7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_B4C7)
    OP_82(0x2, 0x2)
    WaitChrThread(0x15, 0x0)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #289
        0x1C,
        (
            "#552F#5P呜……\x01",
            "这么突然，到底怎么回事……！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x1C, 20)
    SetChrSubChip(0x1C, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #290
        0x1C,
        (
            "#054F#3S#5P──喂，丹！\x01",
            "到底发生什么事了！？\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #291
        0x1C,
        "#055F#5P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x11,
        "#560F#6P阿、阿加特大哥哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x1C,
        (
            "#052F#5P怎么，提妲。\x01",
            "晚饭还没做好吗……\x02\x03",

            "#055F哎，奇怪……？\x02\x03",

            "我记得我刚走下定期船，\x01",
            "你和你父亲前来迎接……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x11,
        "#562F#6P……呜……………\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x11, 21)

    def lambda_B696():
        OP_6D(1730, 4000, 3030, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B696)

    def lambda_B6AE():
        OP_8E(0xFE, 0xFFFFFF74, 0xFA0, 0x640, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_B6AE)
    Sleep(500)
    Fade(500)
    OP_6D(770, 4000, 3030, 0)
    OP_67(0, 3550, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(36000, 0)
    OP_6E(299, 0)
    WaitChrThread(0x11, 0x0)
    SetChrChipByIndex(0x11, 22)
    SetChrSubChip(0x11, 0)
    OP_22(0x20C, 0x0, 0x64)
    OP_0D()
    Sleep(300)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #295
        0x1C,
        (
            "#055F#5P喂、喂……\x01",
            "怎么了，突然这样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x11,
        (
            "#562F#12P太、太好了……\x01",
            "真是太好了……\x02\x03",

            "阿加特大哥哥平安无事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x1C,
        (
            "#551F#5P平安无事……？\x01",
            "这之前不是刚刚才见过面吗。\x02\x03",

            "#555F喂，约修亚。\x01",
            "这是怎么回──\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #298
        0x1C,
        (
            "#052F#5P话说回来……\x01",
            "你是什么时候回来的？\x02\x03",

            "#055F而且，还有这个不良神父……？\x01",
            "为什么你也在啊！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B8BF():
        OP_6D(770, 4000, 1580, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B8BF)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #299
        0x102,
        "#1514F#6P哈哈，那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x109,
        (
            "#1840F#6P因为发生了很多\x01",
            "严重的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x1B,
        (
            "#1536F#8P话说在前面，\x01",
            "我们可是也在场哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x19,
        "#071F#8P嘿，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x16,
        "#1168F#8P呵呵，久疏问候。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x1A,
        (
            "#819F#8P真好啊，阿加特前辈。\x01",
            "你还是老样子，\x01",
            "和小提妲这么亲密……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x18,
        (
            "#1541F#8P呵，天下最幸福的人\x01",
            "指的一定就是你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x1C,
        (
            "#055F#5P白、白痴啊！\x01",
            "才不是这样呢！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x11, 3)
    SetChrSubChip(0x11, 0)

    def lambda_BA84():
        OP_6D(770, 4000, 580, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BA84)

    def lambda_BA9C():
        OP_8F(0xFE, 0xFFFFFF88, 0xFA0, 0x32A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_BA9C)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x109, 0x0)
    Fade(250)
    ClearChrFlags(0x1C, 0x40)
    ClearChrFlags(0x1C, 0x4)
    SetChrChipByIndex(0x1C, 14)
    SetChrSubChip(0x1C, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #307
        0x11,
        (
            "#067F#12P嘿嘿……\x01",
            "对不起，我太兴奋了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)
    Sleep(300)

    ChrTalk(    #308
        0x11,
        (
            "#061F#5P嗯，不过这样一来，\x01",
            "就只剩下艾丝蒂尔姐姐了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x1C,
        (
            "#052F#5P哎，艾丝蒂尔吗……\x02\x03",

            "#055F等一下，喂！\x01",
            "这到底是怎么回事！？\x02\x03",

            "这难道又是艾莉卡·拉赛尔\x01",
            "设下的圈套吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x19, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #310
        0x109,
        (
            "#1068F#6P艾莉卡博士……\x01",
            "她就这么视\x01",
            "阿加特为眼中钉吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x102,
        (
            "#1514F#6P……自从她的\x01",
            "父母回来之后，\x01",
            "好像发生了很多事情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x11,
        "#067F#5P唉……真是太丢人了……\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0x109, 150, 4000, -2370, 0)
    SetChrPos(0x102, -1230, 4000, -3650, 0)
    SetChrPos(0x11, 920, 4000, -3150, 0)
    SetChrPos(0x16, -900, 4000, -4520, 0)
    SetChrPos(0x18, 450, 4000, -4600, 0)
    SetChrPos(0x16, -950, 4000, -4770, 0)
    SetChrPos(0x14, -2390, 4000, -5120, 0)
    SetChrPos(0x13, -240, 4000, -6160, 0)
    SetChrPos(0x12, -1670, 4000, -6190, 0)
    SetChrPos(0x19, 1300, 4000, -6200, 0)
    SetChrPos(0x1A, 2000, 4000, -3500, 0)
    SetChrPos(0x1B, 1470, 4000, -5000, 0)
    SetChrPos(0x1C, 190, 4000, -340, 180)
    ClearChrFlags(0x1C, 0x40)
    ClearChrFlags(0x1C, 0x4)
    SetChrChipByIndex(0x1C, 14)
    SetChrSubChip(0x1C, 0)
    SetChrFlags(0x10, 0x80)
    OP_6D(1500, 4000, -1600, 0)
    OP_67(0, 5220, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(45000, 0)
    OP_6E(381, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #313
        0x1C,
        (
            "#555F#5P哼……算了。\x02\x03",

            "虽然无法接受，\x01",
            "不过这么磨磨蹭蹭也什么事都干不了。\x02\x03",

            "我也来给大伙帮忙，\x01",
            "赶快继续前进吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x102,
        "#1504F#6P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x109,
        (
            "#1840F#6P哈哈，\x01",
            "还是那样果断呢。\x02\x03",

            "如果有什么疑问的话，\x01",
            "我们可以尽量给你解释一下的哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x1C,
        (
            "#053F#5P算了，反正从刚才的话中\x01",
            "也已经了解了大概的情况。\x02\x03",

            "接下来只需要亲眼看一下，\x01",
            "或者问问其他人就知道了。\x02\x03",

            "#556F话说回来……\x01",
            "已经集结了这么多伙伴，\x01",
            "重要的家伙却不在场呢。\x02\x03",

            "还是赶快把那家伙\x01",
            "找出来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x11,
        "#560F#6P阿加特大哥哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x102,
        "#1505F#6P……谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x1C,
        (
            "#551F#5P哎呀，这就不用道谢了。\x02\x03",

            "跟你一样，\x01",
            "那家伙也算是我的后辈。\x02\x03",

            "#051F对了，约修亚。\x02\x03",

            "怎么样，到外国去修行后\x01",
            "是不是又变强了很多呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x102,
        (
            "#1513F#6P嗯……差不多吧。\x02\x03",

            "#1501F不过，比起我来，\x01",
            "艾丝蒂尔变得可靠很多呢。\x02\x03",

            "在旅途经过的协会支部里\x01",
            "也经常被委以重任呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x1C,
        (
            "#051F#5P嘿……\x01",
            "不愧是大叔的女儿呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x1B,
        (
            "#1536F#12P呵呵，不过阿加特啊……\x02\x03",

            "你还真能立刻就\x01",
            "接受目前的状况呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x1A,
        (
            "#1310F#6P你就没有怀疑\x01",
            "这是梦境或者幻术吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x1C,
        "#052F#5P那、那个嘛……\x02",
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #325
        0x18,
        (
            "#1547F#6P呵，那还用说吗。\x02\x03",

            "#1541F被提妲这么拥抱着的\x01",
            "那种新鲜的气息和柔软的触感……\x02\x03",

            "这种感觉太过真实，\x01",
            "没有怀疑的余地对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x1C,
        "#055F#5P嗯！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_8C(0x11, 180, 600)
    Sleep(300)
    OP_8C(0x11, 0, 600)

    ChrTalk(    #327
        0x11,
        "#565F#6P咦、咦、咦……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x12,
        "#179F#6P嗯……原来如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x16,
        (
            "#1380F#6P那、那个……\x02\x01",

            "#1165F嗯，的确非常顺理成章呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #330
        0x1C,
        (
            "#055F#5P等、等一下！\x01",
            "怎么会变成这样！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x1B,
        "#1521F#12P别害羞、别害羞㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x14,
        (
            "#210F#6P哎呀，不是很好吗？\x01",
            "现在年龄相差很大的也很常见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x1A,
        (
            "#1311F#5P不对不对！\x01",
            "不如说这个才是最佳的搭配！\x02\x03",

            "#1314F这种绝妙的距离感，\x01",
            "到底是不得不让人感到欣慰呢，\x01",
            "还是该替他们焦急得坐立不安呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x14,
        (
            "#415F#6P原来如此……\x01",
            "这就是所谓的浪漫吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x11,
        "#562F#6P唉、唉……\x02",
    )

    CloseMessageWindow()
    OP_62(0x1C, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #336
        0x1C,
        "#057F#5P你、你们这些……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x13,
        (
            "#277F#6P（哎呀哎呀……\x01",
            "  真是缺乏紧张感啊。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x19,
        (
            "#071F#11P（哈哈，这也算是\x01",
            "  我们这些伙伴独特的氛围吧。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x1C,
        (
            "#551F#5P真是……\x01",
            "你们还不赶快适可而止。\x02\x03",

            "#552F对了……\x01",
            "不是还有另一个伙伴吗？\x02\x03",

            "说是教会的修女什么的……\x01",
            "那家伙在什么地方啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x11,
        "#063F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x109,
        (
            "#1840F#6P……抱歉抱歉。\x01",
            "她就在那边的书架旁，\x01",
            "不过有些事情……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C84D():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C84D)
    Sleep(50)

    def lambda_C860():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C860)
    Sleep(50)
    OP_8C(0x1A, 315, 400)
    Sleep(300)

    ChrTalk(    #342
        0x1A,
        (
            "#816F#11P是叫做莉丝吧？\x02\x03",

            "#811F我和她稍微说了说话，\x01",
            "她是个很可爱的人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x1B,
        (
            "#1527F#12P我也和她谈了谈……　\x01",
            "还真是个性格独特的有趣的孩子。\x02\x03",

            "不过似乎她现在心情不好，\x01",
            "所以没能怎么搭上话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x102,
        (
            "#1505F#6P……凯文先生。\x02\x03",

            "#1503F把探索的事情交给我们，\x01",
            "你再去和莉丝小姐\x01",
            "谈一谈怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x109,
        "#1067F#5P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 225, 400)
    Sleep(300)

    ChrTalk(    #346
        0x109,
        (
            "#1078F#5P不用了……\x01",
            "对『方石』的操控\x01",
            "还是我最为熟悉。\x02\x03",

            "而且那些『恶魔』也十分危险……\x01",
            "我可不能离队啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x102,
        "#1503F#6P可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x109,
        (
            "#1075F#5P没事，她也不是小孩子了，\x01",
            "过一阵子心情就会好起来的。\x02\x03",

            "#1840F现在时间紧迫……\x01",
            "我们还是赶快出发吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x16,
        "#1163F#6P凯文先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x18,
        (
            "#1545F#6P呵，那就让我留下来\x01",
            "打开她的心扉吧……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CB71():
        OP_6D(1500, 4000, -2600, 800)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_CB71)

    def lambda_CB89():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_CB89)
    WaitChrThread(0x18, 0x1)
    WaitChrThread(0xEE, 0x0)
    Fade(250)
    SetChrChipByIndex(0x18, 23)
    SetChrSubChip(0x18, 0)
    OP_0D()

    def lambda_CBB1():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CBB1)

    def lambda_CBBF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_CBBF)
    Sleep(50)

    def lambda_CBD2():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_CBD2)

    def lambda_CBE0():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_CBE0)
    Sleep(50)

    def lambda_CBF3():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_CBF3)

    def lambda_CC01():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_CC01)
    Sleep(50)

    def lambda_CC14():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_CC14)
    OP_8C(0x1A, 225, 400)
    OP_22(0xBE, 0x0, 0x64)

    def lambda_CC2E():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_CC2E)
    WaitChrThread(0x18, 0x0)

    ChrTalk(    #351
        0x18,
        (
            "#1547F#5P用各位久违了的\x01",
            "超绝华丽的琴技！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x89, 0x0, 0x64)
    OP_62(0x18, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x19, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1B, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(2000)

    ChrTalk(    #352
        0x13,
        "#274F#6P白痴，还不给我住手。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x1B,
        (
            "#1525F#11P唉……\x01",
            "你也还是一点没变。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CDEC():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_CDEC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_63(0x18)
    OP_44(0x109, 0x0)
    OP_A2(0x290E)
    OP_28(0x34, 0x1, 0x8)
    OP_28(0x34, 0x1, 0x10)
    OP_3F(0x35C, 1)
    OP_DB(0x0, 0x5)
    OP_A2(0x25CB)
    Call(6, 15)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    ClearChrFlags(0xF0, 0x80)
    ClearChrFlags(0xF1, 0x80)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 258, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_C0(0x20, 0x1, 0x102, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 390, 4000, -1290, 180)
    SetChrPos(0x1, 390, 4000, -1290, 180)
    SetChrPos(0x2, 390, 4000, -1290, 180)
    SetChrPos(0x3, 390, 4000, -1290, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_E5(0x2, 0xFF, 0x13, 700)
    Call(0, 8)
    Call(0, 6)
    Call(0, 9)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_13_B0F6 end

    SaveToFile()

Try(main)
