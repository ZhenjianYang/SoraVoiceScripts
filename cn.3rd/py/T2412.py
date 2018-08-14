from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2412   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2412.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        '特蕾莎院长',                           # 9
        '目标用照相机',                         # 10
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02570 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH02570P._CP',             # 00
    )

    DeclNpc(
        X                   = -3000,
        Z                   = 0,
        Y                   = 14280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_F2",           # 00, 0
        "Function_1_168",          # 01, 1
        "Function_2_169",          # 02, 2
        "Function_3_2E6",          # 03, 3
        "Function_4_861",          # 04, 4
        "Function_5_D09",          # 05, 5
        "Function_6_D6E",          # 06, 6
    )


    def Function_0_F2(): pass

    label("Function_0_F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_101")
    SetChrFlags(0x10, 0x80)
    Jump("loc_14F")

    label("loc_101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_11C")
    SetChrPos(0x10, 32940, 0, -34330, 262)
    Jump("loc_14F")

    label("loc_11C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_137")
    SetChrPos(0x10, -3000, 0, 14280, 0)
    Jump("loc_14F")

    label("loc_137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_14F")
    SetChrPos(0x10, -3000, 0, 14280, 0)

    label("loc_14F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_167")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_167")
    Event(0, 4)

    label("loc_167")

    Return()

    # Function_0_F2 end

    def Function_1_168(): pass

    label("Function_1_168")

    Return()

    # Function_1_168 end

    def Function_2_169(): pass

    label("Function_2_169")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18E")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_2D0")

    label("loc_18E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A7")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_2D0")

    label("loc_1A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C0")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_2D0")

    label("loc_1C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D9")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_2D0")

    label("loc_1D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F2")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_2D0")

    label("loc_1F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20B")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_2D0")

    label("loc_20B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_224")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_2D0")

    label("loc_224")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23D")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_2D0")

    label("loc_23D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_256")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_2D0")

    label("loc_256")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26F")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_2D0")

    label("loc_26F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_288")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_2D0")

    label("loc_288")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A1")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_2D0")

    label("loc_2A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BA")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_2D0")

    label("loc_2BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D0")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_2D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E5")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2D0")

    label("loc_2E5")

    Return()

    # Function_2_169 end

    def Function_3_2E6(): pass

    label("Function_3_2E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_53F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E5, 1)), scpexpr(EXPR_END)), "loc_3F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_369")

    ChrTalk(    #0
        0x10,
        (
            "#750F今天我也打扫一下\x01",
            "自己的房间吧。\x02\x03",

            "#751F呵呵，说不定会有\x01",
            "可以拿到义卖会去的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ED")

    label("loc_369")


    ChrTalk(    #1
        0x10,
        (
            "#750F本来打算在打扫的同时\x01",
            "顺便整理一下能够\x01",
            "拿到义卖会去的东西……\x02\x03",

            "#751F呵呵，\x01",
            "每个都是充满回忆舍不得放手啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3ED")

    Jump("loc_53C")

    label("loc_3F0")


    ChrTalk(    #2
        0x14E,
        (
            "#1714F啊，老师！\x01",
            "打扫的话让我来吧……！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E5, 0)), scpexpr(EXPR_END)), "loc_483")

    ChrTalk(    #3
        0x10,
        (
            "#750F玛丽，\x01",
            "今天不是让你休息吗？\x02\x03",

            "打扫就交给老师，\x01",
            "你好好去玩吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F7")

    label("loc_483")


    ChrTalk(    #4
        0x10,
        (
            "#750F没关系啦，玛丽。\x02\x03",

            "偶尔也要休息一下，\x01",
            "尽情去玩吧。\x02\x03",

            "今天天气也不错，\x01",
            "就去开心一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F7")

    TurnDirection(0x10, 0x14F, 400)

    ChrTalk(    #5
        0x10,
        "#751F当然波利也是哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x14F,
        "#1732F好～！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F29)

    label("loc_53C")

    Jump("loc_85D")

    label("loc_53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_76F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E5, 0)), scpexpr(EXPR_END)), "loc_5D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_582")

    ChrTalk(    #7
        0x10,
        (
            "#750F好了，\x01",
            "今天就尽情去玩吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D6")

    label("loc_582")


    ChrTalk(    #8
        0x10,
        (
            "#750F玛丽，\x01",
            "今天就不用帮忙了。\x02\x03",

            "……总是让你\x01",
            "帮忙干这干那的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_5D6")

    Jump("loc_76C")

    label("loc_5D9")


    ChrTalk(    #9
        0x10,
        (
            "#753F哎呀，你们两个……\x02\x03",

            "#751F呵呵，有潮水的气味。\x01",
            "你们去海边了对吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #10
        0x14E,
        (
            "#1714F嗯、嗯……\x01",
            "那个……\x02",
        )
    )

    Jump("loc_675")

    label("loc_675")

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        (
            "#750F没关系啦，玛丽。\x02\x03",

            "偶尔也要休息一下，\x01",
            "尽情去玩吧。\x02\x03",

            "今天天气也不错，\x01",
            "就去开心一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x14E,
        (
            "#1712F……是、是的！\x02\x03",

            "（礼物的事\x01",
            "  得保密才行……）\x02\x03",

            "#1713F（对不起，老师！\x01",
            "  今天我就休息一下吧！）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F28)

    label("loc_76C")

    Jump("loc_85D")

    label("loc_76F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_85D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7DD")

    ChrTalk(    #13
        0x10,
        (
            "#750F今天玛诺利亚村\x01",
            "要召开义卖会哦。\x02\x03",

            "等一下得去帮忙\x01",
            "才行呢。\x02",
        )
    )

    Jump("loc_7D9")

    label("loc_7D9")

    CloseMessageWindow()
    Jump("loc_85D")

    label("loc_7DD")


    ChrTalk(    #14
        0x10,
        (
            "#750F哎呀，玛丽、波利。\x02\x03",

            "你们俩怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x14E,
        "#1714F没、没什么！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x14F,
        "#1732F什么事也没有～。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_85D")

    TalkEnd(0xFE)
    Return()

    # Function_3_2E6 end

    def Function_4_861(): pass

    label("Function_4_861")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-3160, 400, 13640, 0)
    OP_67(0, 7080, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(50000, 0)
    OP_6E(272, 0)
    OP_4A(0x10, 255)
    SetChrPos(0x10, -4100, 0, 14380, 0)
    OP_43(0x10, 0x1, 0x0, 0x6)
    SetChrPos(0x14E, -600, 0, 4320, 0)
    FadeToBright(2000, 0)

    def lambda_8E6():
        OP_6B(2760, 6000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_8E6)

    def lambda_8F6():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8F6)
    OP_0D()
    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)

    def lambda_911():
        OP_8E(0xFE, 0xFFFFF4AC, 0x0, 0x2F80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_911)
    WaitChrThread(0x14E, 0x1)
    Sleep(200)

    ChrTalk(    #17
        0x14E,
        "#1718F老师，我来帮忙做饭吧。\x02",
    )

    CloseMessageWindow()

    def lambda_95F():
        OP_8C(0xFE, 180, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_95F)
    Sleep(500)

    ChrTalk(    #18
        0x10,
        (
            "#751F不用，没关系的。\x01",
            "谢谢你，玛丽。\x02\x03",

            "#750F……总是让你帮忙干活\x01",
            "还有照顾其他人，\x01",
            "真是抱歉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x14E,
        (
            "#1714F咦……？\x02\x03",

            "#1710F不，\x01",
            "请别介意，老师。\x02\x03",

            "我年龄比较大，\x01",
            "这点小事是应该的嘛。\x02\x03",

            "#1719F科洛丝姐姐\x01",
            "也正在王都努力呢……\x01",
            "我也必须振作才行！\x02\x03",

            "#1718F……嗯，\x01",
            "那我就去打扫房间了。\x02\x03",

            "#1710F今天早上克拉姆又弄得乱七八糟的，\x01",
            "得去收拾收拾才行……\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x14E, 0x1, 0x0, 0x5)
    Sleep(500)

    ChrTalk(    #20 op#A
        0x10,
        "#753F#20A啊，玛丽……\x02",
    )

    Sleep(2000)
    OP_56(0x0)
    WaitChrThread(0x14E, 0x1)
    OP_22(0x191, 0x0, 0x64)
    Sleep(100)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x5)
    Sleep(1000)
    OP_63(0x14E)
    OP_8C(0x14E, 180, 500)
    Sleep(200)

    ChrTalk(    #21
        0x14E,
        (
            "#1714F咦？　怎么回事。\x02\x03",

            "是不是达尼艾尔\x01",
            "把水泼到鸡身上了？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x14E, 315, 500)

    ChrTalk(    #22
        0x14E,
        "#1710F我去看看！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14E, 180, 500)

    ChrTalk(    #23
        0x14E,
        "#1710F呼，好忙好忙……\x02",
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x0)

    def lambda_C1A():
        OP_8E(0xFE, 0xFFFFFBC8, 0x0, 0xFFFFFB8C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_C1A)
    Sleep(2000)
    OP_63(0x14E)

    def lambda_C3D():
        OP_6D(-3000, 400, 14280, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_C3D)
    Sleep(2000)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(300)

    ChrTalk(    #24
        0x10,
        (
            "#754F她总是帮忙干活，\x01",
            "虽然很让人高兴……\x02\x03",

            "但是最近\x01",
            "是不是努力过头了呢……\x02",
        )
    )

    Jump("loc_CDB")

    label("loc_CDB")

    CloseMessageWindow()

    def lambda_CE2():
        OP_6B(2460, 4000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_CE2)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_861 end

    def Function_5_D09(): pass

    label("Function_5_D09")

    Sleep(300)
    OP_8C(0x14E, 180, 500)

    def lambda_D1B():
        OP_6D(-3160, 400, 12140, 2000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_D1B)

    def lambda_D33():
        OP_8E(0xFE, 0xFFFFF4AC, 0x0, 0x2580, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_D33)
    WaitChrThread(0x14E, 0x2)

    def lambda_D53():
        OP_8E(0xFE, 0xFFFFFBC8, 0x0, 0x2580, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_D53)
    WaitChrThread(0x14E, 0x2)
    Return()

    # Function_5_D09 end

    def Function_6_D6E(): pass

    label("Function_6_D6E")

    Sleep(1000)

    def lambda_D79():
        OP_8E(0xFE, 0xFFFFEB10, 0x0, 0x3890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_D79)
    WaitChrThread(0x10, 0x2)
    OP_8C(0x10, 0, 500)
    Sleep(1500)

    def lambda_DA5():
        OP_8E(0xFE, 0xFFFFF448, 0x0, 0x37C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_DA5)
    WaitChrThread(0x10, 0x2)
    OP_8C(0x10, 0, 500)
    Return()

    # Function_6_D6E end

    SaveToFile()

Try(main)
