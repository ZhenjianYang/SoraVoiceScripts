from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U7004   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7004.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60210",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
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


    AddCharChip(
        'ED6_DT27/CH04150 ._CH',             # 00
        'ED6_DT26/CH20219 ._CH',             # 01
        'ED6_DT27/CH03084 ._CH',             # 02
        'ED6_DT27/CH03085 ._CH',             # 03
        'ED6_DT26/CH20609 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT27/CH04150P._CP',             # 00
        'ED6_DT26/CH20219P._CP',             # 01
        'ED6_DT27/CH03084P._CP',             # 02
        'ED6_DT27/CH03085P._CP',             # 03
        'ED6_DT26/CH20609P._CP',             # 04
    )

    ScpFunction(
        "Function_0_D2",           # 00, 0
        "Function_1_EF",           # 01, 1
        "Function_2_109",          # 02, 2
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_EE")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_EE")

    Return()

    # Function_0_D2 end

    def Function_1_EF(): pass

    label("Function_1_EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_108")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_108")

    Return()

    # Function_1_EF end

    def Function_2_109(): pass

    label("Function_2_109")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 630, -11150, -97460, 180)
    SetChrChipByIndex(0x109, 1)
    SetChrSubChip(0x109, 0)
    SetChrFlags(0x109, 0x800)
    ClearChrFlags(0x109, 0x1)
    SetChrPos(0x10F, -230, -11150, -100420, 90)
    SetChrChipByIndex(0x10F, 4)
    SetChrSubChip(0x10F, 0)
    SetChrFlags(0x10F, 0x2)
    SetChrFlags(0x10F, 0x800)
    ClearChrFlags(0x10F, 0x1)
    OP_6D(290, -11150, -97800, 0)
    OP_67(0, 7200, -10000, 0)
    OP_6B(1600, 0)
    OP_6C(315000, 0)
    OP_6E(547, 0)
    OP_E5(0x1, 0xFF, 0x13, 262144)
    OP_E5(0x1, 0xFF, 0x14, 262144)
    OP_E5(0x1, 0xFF, 0x1B, 262144)
    OP_E5(0x1, 0xFF, 0x1D, 262144)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    OP_82(0x86, 0x0)
    OP_82(0x87, 0x0)
    OP_82(0x88, 0x0)
    OP_82(0x89, 0x0)
    OP_82(0x8A, 0x0)
    OP_82(0x8B, 0x0)
    Sleep(2000)
    SetMessageWindowPos(250, 50, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #0
        (
            "\x07\x00#1065F（嗯……）\x02\x03",

            "#1067F（怎么……\x01",
            "  我……为什么……）\x02\x03",

            "#1063F#3S！！！\x02",
        )
    )

    Jump("loc_25E")

    label("loc_25E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    def lambda_270():
        OP_6B(1350, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_270)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    OP_9E(0x109, 0xF, 0x0, 0x258, 0xBB8)
    Sleep(100)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x109, 2)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x109, 0x800)
    SetChrFlags(0x109, 0x1)
    SetChrPos(0x109, 630, -11150, -97200, 180)
    OP_0D()
    Sleep(500)

    ChrTalk(    #1
        0x109,
        "#1067F#5P这里怎么回事……\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0xFFFFFE70, 1300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x109)
    Fade(250)
    SetChrChipByIndex(0x109, 3)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #2
        0x109,
        "#1069F#11P喂，莉丝！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    def lambda_371():
        OP_6D(-790, -11150, -99080, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_371)
    OP_8E(0x109, 0xAA, 0xFFFFD472, 0xFFFE7BF4, 0xFA0, 0x0)
    WaitChrThread(0x109, 0x0)
    Fade(250)
    SetChrChipByIndex(0x109, 3)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #3
        0x109,
        (
            "#1069F#11P莉丝！\x01",
            "醒一醒！\x02\x03",

            "#1067F哼……\x01",
            "……到底怎么回事……\x02",
        )
    )

    Jump("loc_40C")

    label("loc_40C")

    CloseMessageWindow()
    OP_9E(0x10F, 0xF, 0x0, 0x12C, 0xBB8)
    OP_99(0x10F, 0x0, 0x2, 0x1F4)

    ChrTalk(    #4
        0x10F,
        "#1445F#6P#40W嗯……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    OP_99(0x10F, 0x3, 0x5, 0x1F4)
    OP_0D()
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    ChrTalk(    #5
        0x10F,
        (
            "#1802F#6P#40W……凯文……？\x02\x03",

            "为什么在这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        (
            "#1068F#11P呼……\x01",
            "你醒了吗。\x02\x03",

            "#1840F感觉怎么样？\x01",
            "是不是有些恶心？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #7
        0x10F,
        "#1445F#6P#40W……好难受啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x109,
        "#1069F#11P真、真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10F,
        (
            "#1446F#6P肚子太饿了。\x02\x03",

            "#1801F已经到极限了……\x01",
            "刚才买的面包\x01",
            "快让我吃了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x109,
        (
            "#1068F#11P呃……\x01",
            "我很明白你的心情！\x02\x03",

            "#1069F但在那之前\x01",
            "先给我把疑问整理清楚！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10F,
        (
            "#1805F#6P唔……\x01",
            "吃饭可是一切的基本啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 1600, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x10F)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    ClearChrFlags(0x10F, 0x2)
    ClearChrFlags(0x10F, 0x800)
    SetChrFlags(0x10F, 0x1)
    SetChrPos(0x10F, -30, -11150, -100600, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(    #12
        0x10F,
        (
            "#1802F#6P……对了。\x02\x03",

            "那个奇怪的男人出现后，\x01",
            "『方石』发出一片白色光芒……\x02\x03",

            "#1445F#40W……接着………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #13
        0x109,
        (
            "#1065F#11P没错……\x01",
            "就不知道发生了什么了。\x02\x03",

            "#1063F还有……\x01",
            "你看看周围。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10F,
        "#1802F#6P………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(1240, -6070, -99140, 0)
    OP_67(0, 5270, -10000, 0)
    OP_6B(1750, 0)
    OP_6C(351000, 0)
    OP_6E(626, 0)

    def lambda_85B():
        OP_6C(314000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_85B)
    OP_8C(0x10F, 270, 400)
    Sleep(300)
    OP_8C(0x109, 315, 400)
    Sleep(300)
    OP_8C(0x10F, 315, 400)
    Sleep(300)
    OP_8C(0x109, 0, 400)
    Sleep(800)
    WaitChrThread(0x109, 0x0)
    Fade(500)
    OP_6D(-790, -11150, -99080, 0)
    OP_67(0, 7600, -10000, 0)
    OP_6B(1550, 0)
    OP_6C(315000, 0)
    OP_6E(465, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #15
        0x10F,
        (
            "#1802F#6P……石头做的书架……\x02\x03",

            "在遗迹里面……？\x01",
            "不对，这么说……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 0, 400)
    Sleep(300)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #16
        0x10F,
        "#1444F#6P…………哎…………………\x02",
    )

    CloseMessageWindow()
    OP_1D(0xB8)

    def lambda_994():
        OP_6D(3910, -1150, -54470, 7000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_994)

    def lambda_9AC():
        OP_67(0, 6340, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9AC)

    def lambda_9C4():
        OP_6B(12640, 10000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9C4)

    def lambda_9D4():
        OP_6C(315000, 7000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_9D4)

    def lambda_9E4():
        OP_6E(728, 7000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_9E4)
    Sleep(4000)
    Fade(1000)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    OP_44(0x10F, 0x1)
    OP_6D(43530, -13900, -40220, 0)
    OP_67(0, 8550, -10000, 0)
    OP_6B(4870, 0)
    OP_6C(327000, 0)
    OP_6E(618, 0)

    def lambda_A4F():
        OP_6D(42230, -13900, -22970, 7000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A4F)
    Sleep(5000)
    Fade(1000)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    OP_44(0x10F, 0x1)
    OP_6D(-81350, -11900, -62590, 0)
    OP_67(0, 8550, -10000, 0)
    OP_6B(4870, 0)
    OP_6C(267000, 0)
    OP_6E(618, 0)

    def lambda_AC2():
        OP_6D(-104910, -11900, -78140, 7000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AC2)
    Sleep(5000)
    Fade(1000)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    OP_44(0x10F, 0x1)
    OP_6D(-13220, -11900, 5130, 0)
    OP_67(0, 8550, -10000, 0)
    OP_6B(4870, 0)
    OP_6C(315000, 0)
    OP_6E(618, 0)

    def lambda_B35():
        OP_6D(-14770, -11900, 28930, 7000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B35)
    Sleep(5000)
    Fade(1000)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    OP_44(0x10F, 0x1)
    OP_6D(-11930, -5200, -30050, 0)
    OP_67(0, 6450, -10000, 0)
    OP_6B(10780, 0)
    OP_6C(321000, 0)
    OP_6E(660, 0)

    def lambda_BA8():
        OP_6D(3910, -1150, -54470, 7000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BA8)

    def lambda_BC0():
        OP_67(0, 6340, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BC0)

    def lambda_BD8():
        OP_6B(12640, 10000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BD8)

    def lambda_BE8():
        OP_6C(315000, 7000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_BE8)

    def lambda_BF8():
        OP_6E(728, 7000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_BF8)
    OP_C8(0x200, 0x46, "C_PLAC31._CH", 0x1, 0x7D0)
    WaitChrThread(0x109, 0x2)
    Sleep(1000)
    Fade(500)
    OP_6D(-790, -11150, -99080, 0)
    OP_67(0, 6770, -10000, 0)
    OP_6B(1550, 0)
    OP_6C(315000, 0)
    OP_6E(465, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #17
        0x109,
        (
            "#1067F#5P……真难办。\x02\x03",

            "#1065F这任务……\x01",
            "比想象中还要麻烦得多啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_CC8():
        OP_6B(2200, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_CC8)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x25E7)
    OP_C4(0x1, 0x4000)
    Sleep(500)
    WaitChrThread(0x109, 0x0)
    OP_AD(0x2400EC, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x2582)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x155), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存】\x01",              # 0
            "【继续下面剧情】\x01",      # 1
        )
    )

    Jump("loc_D58")

    label("loc_D58")

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6C")
    ShowSaveMenu()

    label("loc_D6C")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_20(0x7D0)
    OP_21()
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_A3(0x2582)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2504)
    NewScene("ED6_DT21/U7001   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_2_109 end

    SaveToFile()

Try(main)
