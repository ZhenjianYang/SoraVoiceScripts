from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3230   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3230.x',
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
        '毛婆婆',                               # 9
        '内燃机',                               # 10
        '汽油罐',                               # 11
        '汽油罐',                               # 12
        '汽油罐',                               # 13
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
        'ED6_DT07/CH02430 ._CH',             # 00
        'ED6_DT06/CH20020 ._CH',             # 01
        'ED6_DT06/CH20020 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH02430P._CP',             # 00
        'ED6_DT06/CH20020P._CP',             # 01
        'ED6_DT06/CH20020P._CP',             # 02
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Unknown3            = 458753,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1966081,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1966081,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1966081,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_162",          # 00, 0
        "Function_1_1BA",          # 01, 1
        "Function_2_208",          # 02, 2
        "Function_3_23B",          # 03, 3
        "Function_4_8FC",          # 04, 4
        "Function_5_968",          # 05, 5
        "Function_6_9D9",          # 06, 6
        "Function_7_A26",          # 07, 7
        "Function_8_A73",          # 08, 8
        "Function_9_BD2",          # 09, 9
        "Function_10_15EC",        # 0A, 10
        "Function_11_1BB6",        # 0B, 11
        "Function_12_1C40",        # 0C, 12
    )


    def Function_0_162(): pass

    label("Function_0_162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176")
    SetMapFlags(0x10000000)
    Event(0, 3)
    Jump("loc_1B9")

    label("loc_176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_195")
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_1B9")

    label("loc_195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B9")
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_1B9")

    Return()

    # Function_0_162 end

    def Function_1_1BA(): pass

    label("Function_1_1BA")

    OP_82(0x80, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1F3")
    SetChrPos(0x9, -20, 250, 8200, 270)
    OP_A1(0x9, 0x3)
    OP_72(0x3, 0x4)
    OP_22(0xA1, 0x1, 0xC8)
    OP_22(0xCF, 0x1, 0x64)
    OP_43(0x9, 0x1, 0x0, 0x2)
    Jump("loc_207")

    label("loc_1F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_202")
    Jump("loc_207")

    label("loc_202")

    OP_22(0xA1, 0x1, 0xC8)

    label("loc_207")

    Return()

    # Function_1_1BA end

    def Function_2_208(): pass

    label("Function_2_208")

    OP_22(0xA1, 0x1, 0x64)
    OP_22(0xCF, 0x1, 0x64)
    OP_C4(0x0, 0x20)

    label("loc_218")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_23A")
    OP_7C(0x0, 0x14, 0xBB8, 0x64)
    Sleep(100)
    Jump("loc_218")

    label("loc_23A")

    Return()

    # Function_2_208 end

    def Function_3_23B(): pass

    label("Function_3_23B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_252")
    Call(0, 11)
    Call(0, 12)

    label("loc_252")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(-1190, 0, 5790, 0)
    OP_67(0, 6120, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(284, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x101, 0x1, 0x0, 0x4)
    OP_43(0x102, 0x1, 0x0, 0x5)
    OP_43(0xF8, 0x1, 0x0, 0x6)
    OP_43(0xF9, 0x1, 0x0, 0x7)

    def lambda_2CF():
        OP_6D(-1190, 0, 5790, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2CF)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #0
        0x101,
        (
            "#1015F#6P……果然是完全\x01",
            "停止了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#1035F#6P虽然是旧式的，\x01",
            "不过这装置也是导力器驱动的。\x02\x03",

            "#1043F不可能不受导力\x01",
            "停止现象的影响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1007F#6P唔……\x02\x03",

            "#1015F不过泵装置说到底\x01",
            "就只是从那里的源泉把水\x01",
            "传到澡堂吧？\x02\x03",

            "感觉应该还能有\x01",
            "其他办法的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_452")

    ChrTalk(    #3
        0x108,
        (
            "#074F#6P不过要是用水桶运过去\x01",
            "也不太现实。\x02\x03",

            "#072F看来还是只能想办法\x01",
            "让这个装置动起来了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52F")

    label("loc_452")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C2")

    ChrTalk(    #4
        0x103,
        (
            "#026F#6P不过要是用水桶运过去\x01",
            "也不太现实。\x02\x03",

            "#022F看来还是只能想办法\x01",
            "让这个装置动起来了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52F")

    label("loc_4C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52F")

    ChrTalk(    #5
        0x106,
        (
            "#053F#6P不过要是用水桶运过去\x01",
            "也不太现实吧。\x02\x03",

            "#050F看来还是只能想办法\x01",
            "让这个装置动起来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66E")
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #6
        0x101,
        (
            "#1004F#4P说起来，『零力场发生器』\x01",
            "就不能用在这个泵上吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #7
        0x102,
        (
            "#1035F#5P可能有点难。\x02\x03",

            "#1040F博士说只能用在大小\x01",
            "可以双手捧住的导力器上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1007F#4P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x107,
        "#064F#6P………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_631():

        label("loc_631")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_631")

    QueueWorkItem2(0x102, 1, lambda_631)
    Sleep(500)

    ChrTalk(    #10
        0x102,
        "#1044F#5P提妲，怎么了？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2009)
    OP_28(0xC2, 0x1, 0x2)
    Call(0, 9)
    Jump("loc_8FB")

    label("loc_66E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B9")
    OP_62(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x106, 0x102, 400)

    ChrTalk(    #11
        0x106,
        (
            "#052F#6P说起来，『零力场发生器』\x01",
            "就不能用在这东西上吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6DD():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6DD)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_703")

    def lambda_6F8():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_6F8)
    Jump("loc_711")

    label("loc_703")


    def lambda_709():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_709)

    label("loc_711")

    TurnDirection(0x102, 0x106, 400)
    Sleep(500)

    ChrTalk(    #12
        0x102,
        (
            "#1035F#5P可能有点难。\x02\x03",

            "#1040F博士说只能用在大小\x01",
            "可以双手捧住的导力器上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x106,
        "#555F#6P唔……对。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1007F#2P唔……\x01",
            "就没什么好办法吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2009)
    OP_28(0xC2, 0x1, 0x2)
    EventEnd(0x0)
    Jump("loc_8FB")

    label("loc_7B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FB")
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x103, 0x102, 400)

    ChrTalk(    #15
        0x103,
        (
            "#023F#6P说起来，『零力场发生器』\x01",
            "对这个泵没用吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_822():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_822)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_848")

    def lambda_83D():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_83D)
    Jump("loc_856")

    label("loc_848")


    def lambda_84E():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_84E)

    label("loc_856")

    TurnDirection(0x102, 0x103, 400)
    Sleep(500)

    ChrTalk(    #16
        0x102,
        (
            "#1035F#5P可能有点难。\x02\x03",

            "#1040F博士说只能用在大小\x01",
            "可以双手捧住的导力器上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x103,
        "#025F#6P嗯……对。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1007F#2P唔……\x01",
            "就没什么好办法吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2009)
    OP_28(0xC2, 0x1, 0x2)
    EventEnd(0x0)

    label("loc_8FB")

    Return()

    # Function_3_23B end

    def Function_4_8FC(): pass

    label("Function_4_8FC")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 100, 0, -230, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_923():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_923)
    OP_8E(0xFE, 0x1EA, 0x0, 0x11EE, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_4_8FC end

    def Function_5_968(): pass

    label("Function_5_968")

    Sleep(700)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 100, 0, -230, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_994():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_994)
    OP_8E(0xFE, 0xFFFFFDBC, 0x0, 0x119E, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_5_968 end

    def Function_6_9D9(): pass

    label("Function_6_9D9")

    Sleep(1400)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 100, 0, -230, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_A05():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A05)
    OP_8E(0xFE, 0x352, 0x0, 0xD16, 0x7D0, 0x0)
    Return()

    # Function_6_9D9 end

    def Function_7_A26(): pass

    label("Function_7_A26")

    Sleep(2100)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 100, 0, -230, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_A52():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A52)
    OP_8E(0xFE, 0xFFFFFD76, 0x0, 0xD48, 0x7D0, 0x0)
    Return()

    # Function_7_A26 end

    def Function_8_A73(): pass

    label("Function_8_A73")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(-1190, 0, 5790, 0)
    OP_67(0, 6120, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(284, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x101, 0x1, 0x0, 0x4)
    OP_43(0x102, 0x1, 0x0, 0x5)
    OP_43(0xF8, 0x1, 0x0, 0x6)
    OP_43(0xF9, 0x1, 0x0, 0x7)

    def lambda_AF2():
        OP_6D(-1190, 0, 5790, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AF2)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #19
        0x101,
        (
            "#1015F#6P唔，要是能想办法让\x01",
            "泵动就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        (
            "#1043F#6P嗯……要是『零力场发生器』\x01",
            "能用就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x107,
        "#064F#6P………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_BA0():

        label("loc_BA0")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_BA0")

    QueueWorkItem2(0x102, 1, lambda_BA0)
    Sleep(500)

    ChrTalk(    #22
        0x102,
        "#1044F#5P提妲，怎么了？\x02",
    )

    CloseMessageWindow()
    Call(0, 9)
    Return()

    # Function_8_A73 end

    def Function_9_BD2(): pass

    label("Function_9_BD2")


    def lambda_BD8():

        label("loc_BD8")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_BD8")

    QueueWorkItem2(0x101, 1, lambda_BD8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C04")

    def lambda_BF6():

        label("loc_BF6")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_BF6")

    QueueWorkItem2(0xF9, 1, lambda_BF6)
    Jump("loc_C15")

    label("loc_C04")


    def lambda_C0A():

        label("loc_C0A")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_C0A")

    QueueWorkItem2(0xF8, 1, lambda_C0A)

    label("loc_C15")

    Sleep(500)

    ChrTalk(    #23
        0x107,
        "#560F#6P嗯、嗯……\x02",
    )

    CloseMessageWindow()

    def lambda_C38():
        OP_6D(-270, 250, 7300, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C38)

    def lambda_C50():
        OP_67(0, 6120, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C50)

    def lambda_C68():
        OP_6B(2620, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C68)

    def lambda_C78():
        OP_6E(302, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_C78)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCD")

    def lambda_C95():
        OP_8E(0xFE, 0x5B4, 0x0, 0x122A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_C95)
    WaitChrThread(0x107, 0x1)

    def lambda_CB5():
        OP_8E(0xFE, 0xFFFFFF38, 0xFA, 0x1D92, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_CB5)
    Jump("loc_D08")

    label("loc_CCD")


    def lambda_CD3():
        OP_8E(0xFE, 0xFFFFF97A, 0x0, 0x1216, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_CD3)
    WaitChrThread(0x107, 0x1)

    def lambda_CF3():
        OP_8E(0xFE, 0xFFFFFF38, 0xFA, 0x1D92, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_CF3)

    label("loc_D08")

    Sleep(500)
    WaitChrThread(0x107, 0x1)
    Sleep(700)
    OP_8C(0x107, 315, 400)
    OP_8E(0x107, 0xFFFFFABA, 0xFA, 0x1ED2, 0xBB8, 0x0)
    OP_8C(0x107, 270, 300)
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)
    OP_8E(0x107, 0xFFFFFA9C, 0xFA, 0x1A0E, 0xBB8, 0x0)
    OP_8C(0x107, 270, 300)
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)
    OP_8E(0x107, 0x9C4, 0x0, 0x1612, 0xFA0, 0x0)
    OP_8C(0x107, 90, 300)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1500)
    OP_8E(0x107, 0x226, 0xFA, 0x1946, 0xBB8, 0x0)
    OP_8E(0x107, 0xA0, 0xFA, 0x2288, 0xBB8, 0x0)
    OP_8C(0x107, 0, 400)
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(    #24
        0x107,
        (
            "#062F#6P那个，那个……\x02\x03",

            "这边是这样的……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9F")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_EDD")

    label("loc_E9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC6")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_EDD")

    label("loc_EC6")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_EDD")

    Jump("loc_F45")

    label("loc_EE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F07")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_F45")

    label("loc_F07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2E")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_F45")

    label("loc_F2E")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_F45")

    Sleep(1000)

    ChrTalk(    #25
        0x101,
        "#1016F#6P我说……提妲？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FA4")

    ChrTalk(    #26
        0x106,
        (
            "#555F#6P真没办法……\x01",
            "又进入那种状态了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA4")


    ChrTalk(    #27
        0x107,
        (
            "#560F#6P因为它不像近来的设备，\x01",
            "没有设计那么复杂的\x01",
            "导力结构……\x02\x03",

            "只要把这里和这里\x01",
            "跟对面连接好的话……\x02\x03",

            "#064F啊，要做成等导力停止现象\x01",
            "结束后马上就能复原的样子……\x02\x03",

            "#062F…………………………………\x02\x03",

            "#061F嗯……好像有办法！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)
    Sleep(500)

    ChrTalk(    #28
        0x107,
        (
            "#560F#2P那个，\x01",
            "说不定\x01",
            "能让泵动起来。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1168")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1127")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1165")

    label("loc_1127")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_114E")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1165")

    label("loc_114E")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1165")

    Jump("loc_11CD")

    label("loc_1168")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118F")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_11CD")

    label("loc_118F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B6")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_11CD")

    label("loc_11B6")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_11CD")

    Sleep(1000)

    ChrTalk(    #29
        0x101,
        "#1004F#6P咦咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#1044F#6P莫非……\x01",
            "你要用『零力场发生器』吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x107,
        (
            "#067F#2P嘿嘿，不是的。\x02\x03",

            "#560F哥哥你也还记得吧？\x01",
            "『内燃引擎』的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x102,
        "#1044F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1015F#6P内燃引擎……\x01",
            "就是上次让工程机械动起来的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x107,
        (
            "#061F#2P嗯⊙\x02\x03",

            "#560F泵装置没有使用和\x01",
            "工程机械一样复杂的结构……\x02\x03",

            "所以只要能让内燃引擎来驱动\x01",
            "依靠导力器驱动的那部分的话，\x01",
            "就能像原来一样工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#1004F#6P原、原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        "#1040F#6P这可真是个盲点呢。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13BE")

    ChrTalk(    #37
        0x106,
        (
            "#051F#6P那么哪儿有那个\x01",
            "内燃引擎呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142F")

    label("loc_13BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13F8")

    ChrTalk(    #38
        0x103,
        (
            "#020F#6P那么哪儿有那个\x01",
            "放在哪里了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142F")

    label("loc_13F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_142F")

    ChrTalk(    #39
        0x108,
        (
            "#070F#6P那么哪儿有那个\x01",
            "内燃引擎呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142F")


    ChrTalk(    #40
        0x107,
        (
            "#560F#2P嗯，我听说飞船坪\x01",
            "保管有内燃引擎。\x02\x03",

            "#061F我想问问维修长\x01",
            "先生就能知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1006F#6P飞船坪的格斯塔夫维修长是吧。\x02\x03",

            "#1015F对了，要让内燃引擎活动\x01",
            "是需要燃料的吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #42
        0x102,
        (
            "#1040F#5P就是『汽油』吧。\x02\x03",

            "说不定还是像上次一样去中央工房\x01",
            "地下打听一下比较好。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-220, 0, 4610, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, -220, 0, 4610, 180)
    SetChrPos(0x1, -220, 0, 4610, 180)
    SetChrPos(0x2, -220, 0, 4610, 180)
    SetChrPos(0x3, -220, 0, 4610, 180)
    OP_69(0x0, 0x0)
    OP_A2(0x200A)
    OP_28(0xC2, 0x1, 0x4)
    OP_28(0xC2, 0x1, 0x100)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_9_BD2 end

    def Function_10_15EC(): pass

    label("Function_10_15EC")

    EventBegin(0x0)
    SetChrPos(0xA, -820, 0, 4090, 315)
    SetChrPos(0xB, -40, 0, 4090, 315)
    SetChrPos(0xC, 700, 0, 4090, 315)
    SetChrPos(0x9, -30, 0, 5200, 90)
    OP_A1(0xA, 0x0)
    OP_72(0x0, 0x4)
    OP_A1(0xB, 0x1)
    OP_72(0x1, 0x4)
    OP_A1(0xC, 0x2)
    OP_72(0x2, 0x4)
    OP_A1(0x9, 0x3)
    OP_72(0x3, 0x4)
    SetChrPos(0x101, 850, 0, 1380, 0)
    SetChrPos(0x102, -350, 0, 1530, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16AE")
    SetChrPos(0xF8, 140, 0, 2750, 180)
    SetChrPos(0xF9, 270, 0, 190, 0)
    Jump("loc_16D0")

    label("loc_16AE")

    SetChrPos(0xF9, 140, 0, 2750, 180)
    SetChrPos(0xF8, 270, 0, 190, 0)

    label("loc_16D0")

    OP_6D(-970, 0, 3460, 0)
    OP_67(0, 5020, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(319, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #43
        0x107,
        (
            "#560F#2P那么材料也齐全了……\x02\x03",

            "#061F赶快开始改造\x01",
            "泵装置吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1006F#6P啊，嗯。\x02\x03",

            "#1016F这倒是好，不过\x01",
            "真的不需要帮忙吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 180, 400)

    ChrTalk(    #45
        0x107,
        (
            "#560F#2P啊……\x01",
            "那么那么……\x02\x03",

            "#061F你们能不能按改造\x01",
            "图纸将零件分别放开？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#1001F#6PＯＫ⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        (
            "#1040F#6P这点忙我们\x01",
            "还是帮得了的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1857")

    ChrTalk(    #48
        0x106,
        "#051F#6P那么就一起来吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_18B9")

    label("loc_1857")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_188B")

    ChrTalk(    #49
        0x103,
        (
            "#021F#6P那么让我也来\x01",
            "帮忙吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18B9")

    label("loc_188B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B9")

    ChrTalk(    #50
        0x108,
        "#070F#6P嗯，让我也来帮忙吧\x02",
    )

    CloseMessageWindow()

    label("loc_18B9")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    OP_6D(-210, 250, 6480, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x9, -20, 250, 8200, 270)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    SetChrPos(0x101, 450, 0, 4800, 0)
    SetChrPos(0x102, -670, 0, 4590, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1969")
    SetChrPos(0xF9, -60, 0, 3240, 0)
    Jump("loc_197A")

    label("loc_1969")

    SetChrPos(0xF8, -60, 0, 3240, 0)

    label("loc_197A")

    SetChrPos(0x107, -10, 250, 6830, 0)
    OP_D2(0x70065, 0x7006D, 0x3)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 3)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #51
        0x107,
        (
            "#062F#6P好……#2620W #20W \x01",
            "#061F嗯，这样一来就完成了。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x107, 65535)
    OP_0D()
    OP_8C(0x107, 180, 400)

    ChrTalk(    #52
        0x101,
        "#1001F#6P太好了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        "#1049F#6P辛苦了，提妲。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A59")

    ChrTalk(    #54
        0x106,
        (
            "#051F#6P你还是那么\x01",
            "手法娴熟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ACA")

    label("loc_1A59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A93")

    ChrTalk(    #55
        0x103,
        (
            "#027F#6P还是和平时一样\x01",
            "心灵手巧啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ACA")

    label("loc_1A93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ACA")

    ChrTalk(    #56
        0x108,
        (
            "#070F#6P还是和平时一样\x01",
            "干得漂亮啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ACA")


    ChrTalk(    #57
        0x107,
        (
            "#067F#2P嘿嘿，还不知道\x01",
            "能不能动……\x02\x03",

            "赶快试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 0, 400)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x107, 3)
    OP_0D()
    Sleep(300)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)
    OP_22(0xA1, 0x1, 0xC8)
    OP_22(0xCF, 0x1, 0x64)

    def lambda_1B39():

        label("loc_1B39")

        OP_7C(0x0, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1B39")

    QueueWorkItem2(0x101, 2, lambda_1B39)
    Sleep(1000)

    ChrTalk(    #58
        0x101,
        "#1004F#6P哇哇……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        (
            "#1040F#6P泵的旋翼\x01",
            "好像开始转动了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_3F(0x40C, 3)
    OP_3F(0x40D, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T3200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_15EC end

    def Function_11_1BB6(): pass

    label("Function_11_1BB6")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C33"),
        (1, "loc_1C39"),
        (SWITCH_DEFAULT, "loc_1C3F"),
    )


    label("loc_1C33")

    OP_A2(0x1200)
    Jump("loc_1C3F")

    label("loc_1C39")

    OP_A2(0x1201)
    Jump("loc_1C3F")

    label("loc_1C3F")

    Return()

    # Function_11_1BB6 end

    def Function_12_1C40(): pass

    label("Function_12_1C40")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_12_1C40 end

    SaveToFile()

Try(main)
