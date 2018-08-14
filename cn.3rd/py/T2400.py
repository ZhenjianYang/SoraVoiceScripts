from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2400   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2400.x',
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
        '克拉姆',                               # 9
        '乔儿',                                 # 10
        '目标用照相机',                         # 11
        '鸡',                                   # 12
        '鸡',                                   # 13
        '鸡',                                   # 14
        '梅威海道方向',                         # 15
        '',                                     # 16
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
        'ED6_DT07/CH02590 ._CH',             # 00
        'ED6_DT07/CH02640 ._CH',             # 01
        'ED6_DT07/CH02630 ._CH',             # 02
        'ED6_DT07/CH02570 ._CH',             # 03
        'ED6_DT07/CH02320 ._CH',             # 04
        'ED6_DT06/CH20051 ._CH',             # 05
        'ED6_DT07/CH00040 ._CH',             # 06
        'ED6_DT07/CH00041 ._CH',             # 07
        'ED6_DT07/CH01720 ._CH',             # 08
        'ED6_DT07/CH02390 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH02590P._CP',             # 00
        'ED6_DT07/CH02640P._CP',             # 01
        'ED6_DT07/CH02630P._CP',             # 02
        'ED6_DT07/CH02570P._CP',             # 03
        'ED6_DT07/CH02320P._CP',             # 04
        'ED6_DT06/CH20051P._CP',             # 05
        'ED6_DT07/CH00040P._CP',             # 06
        'ED6_DT07/CH00041P._CP',             # 07
        'ED6_DT07/CH01720P._CP',             # 08
        'ED6_DT07/CH02390P._CP',             # 09
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 22900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 1060,
        Z                   = 0,
        Y                   = -23220,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1DA",          # 00, 0
        "Function_1_222",          # 01, 1
        "Function_2_223",          # 02, 2
        "Function_3_239",          # 03, 3
        "Function_4_38C",          # 04, 4
        "Function_5_415",          # 05, 5
        "Function_6_43B",          # 06, 6
        "Function_7_A3F",          # 07, 7
        "Function_8_120C",         # 08, 8
        "Function_9_1291",         # 09, 9
    )


    def Function_0_1DA(): pass

    label("Function_0_1DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_221")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_218")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_203")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 9)
    Jump("loc_215")

    label("loc_203")

    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_215")

    Jump("loc_221")

    label("loc_218")

    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_221")

    Return()

    # Function_0_1DA end

    def Function_1_222(): pass

    label("Function_1_222")

    Return()

    # Function_1_222 end

    def Function_2_223(): pass

    label("Function_2_223")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_238")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_223")

    label("loc_238")

    Return()

    # Function_2_223 end

    def Function_3_239(): pass

    label("Function_3_239")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    OP_8D(0xFE, -8760, 13210, 8700, 24630, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_267")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38B")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_350")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2238), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0x339A), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x21FC), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x6036), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_325")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_312():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_312)
    Jump("loc_348")

    label("loc_325")


    def lambda_32B():
        OP_8D(0xFE, -8760, 13210, 8700, 24630, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32B)
    Sleep(200)

    label("loc_348")

    Sleep(30)
    Jump("loc_388")

    label("loc_350")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_388")
    OP_44(0xFE, 0x2)

    def lambda_370():
        OP_8D(0xFE, -8760, 13210, 8700, 24630, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_370)

    label("loc_388")

    Jump("loc_267")

    label("loc_38B")

    Return()

    # Function_3_239 end

    def Function_4_38C(): pass

    label("Function_4_38C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_414")
    OP_43(0xFE, 0x2, 0x0, 0x5)
    OP_22(0x191, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_414")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x38B, 1)"), scpexpr(EXPR_END)), "loc_414")
    TalkBegin(0xFE)
    OP_A2(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x8B\x03\x07\x00。\x02",
    )

    Jump("loc_3FC")

    label("loc_3FC")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFE)

    label("loc_414")

    Return()

    # Function_4_38C end

    def Function_5_415(): pass

    label("Function_5_415")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_430")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_5_415")

    label("loc_430")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_415 end

    def Function_6_43B(): pass

    label("Function_6_43B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(900, 0, 4660, 0)
    OP_67(0, 4460, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(144000, 0)
    OP_6E(304, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 900, 0, -8600, 0)
    SetChrPos(0x105, -160, 0, -8740, 0)

    def lambda_4B1():
        OP_8E(0xFE, 0x384, 0x0, 0xC80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4B1)

    def lambda_4CC():
        OP_8E(0xFE, 0xFFFFFF60, 0x0, 0xA8C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4CC)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x105, 0x1)
    Sleep(500)

    ChrTalk(    #1
        0x105,
        "#043F#11P啊………………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x1)
    TurnDirection(0x10, 0x105, 400)
    OP_62(0x10, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #2
        0x10,
        (
            "#772F#3P姐姐？\x01",
            "……怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x105,
        "#049F#11P嗯…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    FadeToDark(2000, 0, 120)
    OP_0D()
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x18\x07\x0C#40W…………『玛西亚孤儿院』。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #5
        "\x18\x07\x0C#40W是我最重要的地方。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "\x18\x07\x0C#40W但是，我却不能来这里。\x01",
            "软弱的我一定会立刻产生依赖心。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #7
        "\x18\x07\x0C#40W其实，我最想赶回来的就是这里。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #8
        "\x18\x07\x0C#40W但是我……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #9
        "\x18\x07\x0C#40W已经决定以自己的力量走下去了……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(2000, 0)
    OP_0D()
    OP_C4(0x1, 0x800)
    OP_62(0x10, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_95(0x10, 0x0, 0x0, 0x0, 0x1F4, 0xFA0)
    OP_95(0x10, 0x0, 0x0, 0x0, 0x1F4, 0xFA0)
    Sleep(300)

    ChrTalk(    #10
        0x10,
        (
            "#774F#3P姐、姐姐，\x01",
            "到底怎么啦！\x02\x03",

            "#772F我要把你介绍给老师了哦？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #11
        0x105,
        "#049F#11P嗯、嗯……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #12
        0x105,
        (
            "#047F#11P（我也……稍微坚强了点吧。）\x02\x03",

            "（习惯了班级和校园生活，\x01",
            "  也有了亲密的朋友。）\x02\x03",

            "（重新拾起了剑术的练习，\x01",
            "  追赶雷克特学长时\x01",
            "  也锻炼了体力……）\x02\x03",

            "#042F（现在的我，或许没问题了。）\x02\x03",

            "（现在应该能够挺起胸膛\x01",
            "  回到这个重要的地方……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#775F#3P姐、姐姐？？\x01",
            "你身体不舒服吗……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x10, 400)
    Sleep(300)

    ChrTalk(    #14
        0x105,
        (
            "#543F#11P……不，没事。\x02\x03",

            "#542F对了，克拉姆。\x01",
            "你能带我进去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#771F#3P嗯、嗯！\x01",
            "交给我吧！\x02\x03",

            "#770F好啦，\x01",
            "再磨磨蹭蹭就把你丢下了哦！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9D1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_9D1)
    Sleep(200)
    OP_8C(0x105, 0, 400)
    Sleep(100)

    def lambda_9F0():
        OP_8F(0xFE, 0x384, 0x0, 0x3390, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9F0)
    Sleep(300)

    def lambda_A10():
        OP_8F(0xFE, 0xFFFFFF60, 0x0, 0x319C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A10)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2410   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_43B end

    def Function_7_A3F(): pass

    label("Function_7_A3F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x00#40W翌日―――\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x11, 0, 0, -5700, 0)
    SetChrPos(0x105, 100, 0, 34400, 180)
    OP_6D(0, 0, 37440, 0)
    OP_67(0, 8540, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(456, 0)
    OP_1D(0xF)

    def lambda_AF5():
        OP_6D(0, 0, 9920, 12000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_AF5)

    def lambda_B0D():
        OP_6C(315000, 12000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_B0D)
    OP_22(0x1C2, 0x0, 0x64)
    OP_C8(0x200, 0x46, "C_PLAC05._CH", 0x1, 0x7D0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x12, 0x0)
    OP_23(0x1C2)
    Sleep(300)
    Fade(1000)
    OP_6D(-580, 0, 5000, 0)
    OP_67(0, 7540, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    def lambda_B90():
        OP_8E(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B90)
    WaitChrThread(0x11, 0x1)
    Sleep(500)

    ChrTalk(    #17
        0x11,
        "#1890F#6P唔，这里就是孤儿院吗。\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #18
        0x11,
        (
            "#644F#6P好、好了，\x01",
            "今天只是侦察而已呢！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C34():
        OP_6D(-2580, 0, 5000, 1200)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_C34)

    def lambda_C4C():
        OP_67(0, 6060, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C4C)

    def lambda_C64():
        OP_8E(0xFE, 0xFFFFF998, 0x0, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_C64)
    WaitChrThread(0x11, 0x1)

    def lambda_C84():
        OP_8E(0xFE, 0xFFFFEF34, 0x0, 0xCE4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_C84)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 180, 700)
    Sleep(500)

    ChrTalk(    #19
        0x11,
        (
            "#1892F#5P（……上次果然\x01",
            "  是我的不对吗……）\x02\x03",

            "（对孤儿院一点也不了解，\x01",
            "  就随便开那样的玩笑……）\x02\x03",

            "#647F………………………………\x02\x03",

            "#1890F要是对孤儿院了解多一些，\x01",
            "就能好好向科洛丝道歉了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)
    Sleep(500)
    OP_8C(0x11, 0, 700)
    Sleep(300)
    OP_95(0x11, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(300)
    OP_8C(0x11, 180, 700)
    Sleep(300)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)
    Sleep(500)

    def lambda_E04():
        OP_8E(0xFE, 0xFFFFF6B4, 0x0, 0x5DC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E04)
    WaitChrThread(0x11, 0x1)

    def lambda_E24():
        OP_6D(-1660, 0, 15000, 1500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_E24)

    def lambda_E3C():
        OP_6E(376, 1500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_E3C)

    def lambda_E4C():
        OP_8E(0xFE, 0xFFFFFB8C, 0x0, 0x5DC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E4C)
    WaitChrThread(0x11, 0x1)

    def lambda_E6C():
        OP_8E(0xFE, 0xFFFFFB8C, 0x0, 0x2328, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E6C)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 315, 700)
    Sleep(700)
    OP_8C(0x11, 45, 700)
    Sleep(700)
    OP_8C(0x11, 0, 700)
    Sleep(300)

    ChrTalk(    #20
        0x11,
        (
            "#643F#6P怎么，没人在啊。\x02\x03",

            "#645F呼…………\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x11, 0x3, 0x0, 0x8)
    Sleep(3000)

    ChrTalk(    #21 op#A op#5
        0x11,
        (
            "#643F#6P#15A哦～…………\x05\x02\x03",

            "#640F#15A……这地方挺不错的嘛。\x02",
        )
    )

    Sleep(7000)
    Fade(1000)
    OP_6D(-2540, 0, 34300, 0)
    OP_67(0, 4740, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(314000, 0)
    OP_6E(376, 0)
    Sleep(1000)
    OP_44(0x11, 0xFF)
    SetChrPos(0x11, 100, 0, 23420, 0)

    def lambda_FA7():
        OP_8E(0xFE, 0x64, 0x0, 0x73A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_FA7)
    WaitChrThread(0x11, 0x1)
    Sleep(300)

    ChrTalk(    #22
        0x11,
        (
            "#1892F#6P嗯……\x01",
            "这里就是她提到的……\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_70(0x0, 0x14)
    OP_73(0x0)

    def lambda_100D():
        OP_8E(0xFE, 0xDC, 0x0, 0x7D50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_100D)
    WaitChrThread(0x105, 0x1)
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0x105,
        (
            "#044F#11P啊…………\x02\x03",

            "……乔儿同学？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #24
        0x11,
        (
            "#1891F#6P啊啊啊，#20W哎～……！？\x02\x03",

            "#641F啊、啊哈……那个……\x01",
            "好、好久不见～…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x105,
        (
            "#040F#11P嗯……\x02\x01",

            "#543F………………进来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x11,
        (
            "#643F#6P啊……嗯…………\x02\x03",

            "#1890F打、打扰了……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 0, 400)

    def lambda_11A1():
        OP_8E(0xFE, 0x64, 0x0, 0x8660, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11A1)
    Sleep(400)

    def lambda_11C1():
        OP_8E(0xFE, 0x64, 0x0, 0x8660, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_11C1)
    Sleep(2500)
    OP_72(0x0, 0x8)
    ExitThread()
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x0, 20)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2410   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_A3F end

    def Function_8_120C(): pass

    label("Function_8_120C")


    def lambda_1212():
        OP_8E(0xFE, 0xFFFFFF9C, 0x0, 0x2774, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1212)
    WaitChrThread(0x11, 0x1)

    def lambda_1232():
        OP_8E(0xFE, 0xFFFFFF9C, 0x0, 0x3A98, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1232)
    WaitChrThread(0x11, 0x1)
    Sleep(300)
    OP_8C(0x11, 315, 700)
    Sleep(700)
    OP_8C(0x11, 45, 700)
    Sleep(700)
    OP_8C(0x11, 0, 700)

    def lambda_1276():
        OP_8E(0xFE, 0xFFFFFF9C, 0x0, 0x5208, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1276)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_8_120C end

    def Function_9_1291(): pass

    label("Function_9_1291")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_11(0xA0, 0xB4, 0xFF, 0xA410, 0x2BF20, 0x0)
    SetChrFlags(0x105, 0x8)
    OP_6D(960, 0, 29820, 0)
    OP_67(0, 17600, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(356, 0)
    OP_22(0x1C2, 0x0, 0x64)

    def lambda_12FA():
        OP_6B(3000, 25000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_12FA)
    FadeToBright(2000, 0)
    OP_0D()
    OP_23(0x1C2)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #27
        (
            "\x07\x0C#40W唉，\x01",
            "不知怎么回事，突然犯困了……\x02",
        )
    )

    Jump("loc_1358")

    label("loc_1358")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #28
        (
            "\x07\x0C#40W这种懒洋洋的天气，\x01",
            "真是让人受不了……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x0C#40W…………我说，乔儿。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #30
        (
            "\x07\x0C#40W亲手把握住最重要的东西\x01",
            "是不是就是这样一回事呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #31
        "\x07\x0C#40W啊～…………？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(2000)
    FadeToDark(3800, 16777215, -1)
    OP_0D()
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetChrName("")

    AnonymousTalk(    #32
        "\x18\x07\x0C#40W孤儿院总是一如既往地在这里。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #33
        (
            "\x18\x07\x0C#40W无论是我固执己见的时候，\x01",
            "还是为心之所在而烦恼的时候。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #34
        (
            "\x18\x07\x0C#40W『这种心情是伪善吗？』\x01",
            "这种事已经无所谓了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #35
        "\x18\x07\x0C#40W我喜欢这个地方。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #36
        (
            "\x18\x07\x0C#40W哪怕我的眼睛被蒙蔽，\x01",
            "看不到自己的身影。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #37
        (
            "\x18\x07\x0C#40W无论多少次我都要尽力牢牢抓住。\x01",
            "我自己，还有对我来说最重要的场所。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #38
        "\x18\x07\x0C#40W……因为，我就是我。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(2000)
    SetChrName("")

    AnonymousTalk(    #39
        "\x18\x07\x0C#40W而且，我还发现了一件事。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #40
        (
            "\x18\x07\x0C#40W我还没有向那个人\x01",
            "说过一声谢谢。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    ClearMapFlags(0x10)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapFlags(0x10)
    ClearChrFlags(0x105, 0x8)
    OP_20(0xFA0)
    OP_21()
    Sleep(2000)
    OP_A2(0x2504)
    OP_A2(0x2F6F)
    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1291 end

    SaveToFile()

Try(main)
